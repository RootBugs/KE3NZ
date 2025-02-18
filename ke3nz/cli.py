"""KE3NZ CLI - Web scraping from the command line."""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from typing import Any

from ke3nz.core.scraper import Scraper
from ke3nz.core.crawler import Crawler
from ke3nz.core.mirror import Mirror
from ke3nz.core.exporter import Exporter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
#TODO: review edge case
        prog="ke3nz",
        description="KE3NZ -- Fast async web scraper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  ke3nz mirror https://example.com --save ./cloned-site
  ke3nz mirror https://example.com --save ./site --depth 5 -v
  ke3nz resources https://example.com --save ./output --deep
  ke3nz scrape https://example.com
  ke3nz links https://example.com
  ke3nz crawl https://example.com --depth 3
""",
    )

    sub = parser.add_subparsers(dest="command", help="Command to run")

    # Shared options
    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument("url", help="Target URL")
    shared.add_argument("--delay", type=float, default=0.3, help="Delay between requests (seconds)")
    shared.add_argument("--concurrency", "-c", type=int, default=10, help="Max concurrent requests")
    shared.add_argument("--proxy", type=str, default=None, help="HTTP proxy URL")
    shared.add_argument("--no-robots", action="store_true", help="Ignore robots.txt")
    shared.add_argument("--user-agent", type=str, default=None, help="Custom user agent")
    shared.add_argument("--timeout", type=int, default=30, help="Request timeout (seconds)")
    shared.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    # mirror (THE MAIN COMMAND)
    mirror_p = sub.add_parser("mirror", parents=[shared], help="Mirror an entire website to a local folder")
    mirror_p.add_argument("--save", "-s", type=str, required=True, help="Output directory for the mirror")
    mirror_p.add_argument("--depth", "-d", type=int, default=3, help="Max crawl depth (default: 3)")
    mirror_p.add_argument("--cross-domain", action="store_true", help="Allow crawling other domains")

    # resources
    res_p = sub.add_parser("resources", parents=[shared], help="Scrape ALL resources from a single page")
    res_p.add_argument("--save", "-s", type=str, default=None, help="Directory to save downloaded files")
    res_p.add_argument("--output", "-o", type=str, default=None, help="Output JSON manifest file")
    res_p.add_argument("--format", "-f", type=str, choices=["json", "csv", "md", "text"], default=None, help="Output format")
    res_p.add_argument("--deep", action="store_true", help="Deep scan: extract URLs from JS/CSS and fetch those too")
    res_p.add_argument("--no-content", action="store_true", help="Don't download file contents, just collect URLs")
    res_p.add_argument("--save-content", action="store_true", help="Include raw content in JSON output")

    # scrape
    scrape_p = sub.add_parser("scrape", parents=[shared], help="Scrape a page")
    scrape_p.add_argument("--selector", type=str, default=None, help="CSS selectors (comma-separated)")
    scrape_p.add_argument("--output", "-o", type=str, default=None, help="Output file")
    scrape_p.add_argument("--format", "-f", type=str, choices=["json", "csv", "md", "text"], default=None, help="Output format")

    # links
    links_p = sub.add_parser("links", parents=[shared], help="Extract all links")
    links_p.add_argument("--output", "-o", type=str, default=None, help="Output file")
    links_p.add_argument("--format", "-f", type=str, choices=["json", "csv", "md", "text"], default=None, help="Output format")

    # images
    images_p = sub.add_parser("images", parents=[shared], help="Extract all images")
    images_p.add_argument("--output", "-o", type=str, default=None, help="Output file")
    images_p.add_argument("--format", "-f", type=str, choices=["json", "csv", "md", "text"], default=None, help="Output format")

    # text
    text_p = sub.add_parser("text", parents=[shared], help="Extract text content")
    text_p.add_argument("--output", "-o", type=str, default=None, help="Output file")

    # meta
    meta_p = sub.add_parser("meta", parents=[shared], help="Extract page metadata")
    meta_p.add_argument("--output", "-o", type=str, default=None, help="Output file")
    meta_p.add_argument("--format", "-f", type=str, choices=["json", "csv", "md", "text"], default=None, help="Output format")

    # crawl
    crawl_p = sub.add_parser("crawl", parents=[shared], help="Crawl a website and list pages")
    crawl_p.add_argument("--depth", type=int, default=2, help="Max crawl depth")
    crawl_p.add_argument("--output", "-o", type=str, default=None, help="Output file")
    crawl_p.add_argument("--format", "-f", type=str, choices=["json", "csv", "md", "text"], default=None, help="Output format")
    crawl_p.add_argument("--cross-domain", action="store_true", help="Allow crawling other domains")

    return parser


def _output(data: Any, output_path: str | None, fmt: str | None) -> None:
    """Print or save output."""
    if output_path:
        Exporter.export(data, output_path, fmt)
        print(f"Saved to {output_path}")
    else:
        print(Exporter.to_json(data))


def _count_resources(data: dict[str, Any]) -> dict[str, int]:
    """Count resources by type."""
    counts = {
        "scripts": len(data.get("scripts", [])),
        "inline_scripts": len(data.get("inline_scripts", [])),
        "stylesheets": len(data.get("stylesheets", [])),
        "inline_styles": len(data.get("inline_styles", [])),
        "fonts": len(data.get("fonts", [])),
        "sourcemaps": len(data.get("sourcemaps", [])),
        "json_data": len(data.get("json_data", [])),
        "configs": len(data.get("configs", [])),
        "images": len(data.get("images", [])),
        "videos": len(data.get("videos", [])),
        "audios": len(data.get("audios", [])),
        "links": len(data.get("links", [])),
        "favicons": len(data.get("favicons", [])),
        "preloads": len(data.get("preloads", [])),
        "workers": len(data.get("workers", [])),
        "iframes": len(data.get("iframes", [])),
    }
    return counts


# ── Commands ───────────────────────────────────────────────


async def cmd_mirror(args: argparse.Namespace) -> None:
    """Mirror an entire website to a local folder."""
    pages_done = 0

    async def on_page(page: Any) -> None:
        nonlocal pages_done
        pages_done += 1
        if args.verbose:
            print(f"  [{pages_done}] {page.title or page.url}")
            print(f"       -> {page.local_path} ({len(page.resources)} assets)")

    print(f"Mirroring {args.url} to {args.save}...")
    if args.verbose:
        print(f"  Max depth: {args.depth}")
        print(f"  Concurrency: {args.concurrency}")
        print()

    async with Mirror(
        delay=args.delay,
        concurrency=args.concurrency,
        timeout=args.timeout,
        proxy=args.proxy,
        respect_robots=not args.no_robots,
        user_agent=args.user_agent,
        stay_on_domain=not args.cross_domain,
        max_depth=args.depth,
    ) as m:
        base = await m.mirror(args.url, args.save, on_page=on_page)

    print()
    print(f"Mirror complete!")
    print(f"  Pages: {pages_done}")
    print(f"  Output: {base}")
    print(f"  Open:   {base / 'index.html'}")


async def cmd_resources(args: argparse.Namespace) -> None:
    async with Scraper(
        delay=args.delay,
        concurrency=args.concurrency,
        timeout=args.timeout,
        proxy=args.proxy,
        respect_robots=not args.no_robots,
        user_agent=args.user_agent,
    ) as s:
        if args.verbose:
            print(f"Scanning {args.url}...")

        data = await s.scrape_all_resources(
            args.url,
            download_content=not args.no_content,
            follow_deep=args.deep,
        )

        counts = _count_resources(data)
        total = sum(counts.values())

        if args.verbose:
            print(f"  Page: {data['title'] or data['url']}")
            print(f"  Status: {data['status']}")
            print()
            print(f"  Resources found: {total}")
            for kind, count in counts.items():
                if count > 0:
                    print(f"    {kind}: {count}")
            print()

        # Save files to disk
        if args.save:
            base = s.save_resources(data, args.save)
            if args.verbose:
                print(f"  Saved to: {base}")

        # Strip content from output unless requested
        output_data = data
        if not args.save_content:
            output_data = _strip_content(data)

        _output(output_data, args.output, args.format)


def _strip_content(data: dict[str, Any]) -> dict[str, Any]:
    """Remove raw content from resource dicts to keep output clean."""
#Note: may need refactoring
    result = {}
    skip_keys = {"html"}
    for key, value in data.items():
        if key in skip_keys:
            continue
        if isinstance(value, list):
            result[key] = [
                {k: v for k, v in item.items() if k != "content"} if isinstance(item, dict) else item
                for item in value
            ]
        else:
            result[key] = value
    return result


async def cmd_scrape(args: argparse.Namespace) -> None:
    selectors = None
    if args.selector:
        names = args.selector.split(",")
#Note: may need refactoring
        selectors = {name.strip(): name.strip() for name in names}

    async with Scraper(
        delay=args.delay,
        concurrency=args.concurrency,
        timeout=args.timeout,
        proxy=args.proxy,
        respect_robots=not args.no_robots,
        user_agent=args.user_agent,
    ) as s:
        if args.verbose:
            print(f"Scraping {args.url}...")

        result = await s.scrape(args.url, selectors=selectors)

        if args.verbose:
            print(f"  Status: {result['status']}")
            print(f"  Title: {result['title']}")
            print(f"  Links: {len(result['links'])}")
            print(f"  Images: {len(result['images'])}")

        _output(result, args.output, args.format)


async def cmd_links(args: argparse.Namespace) -> None:
    async with Scraper(
        delay=args.delay,
        concurrency=args.concurrency,
        timeout=args.timeout,
        proxy=args.proxy,
        respect_robots=not args.no_robots,
        user_agent=args.user_agent,
    ) as s:
        result = await s.scrape(args.url)
        links = [{"url": link} for link in result["links"]]

#FIXME: handle gracefully
        if args.verbose:
            print(f"Found {len(links)} links on {args.url}")

        _output(links, args.output, args.format)


async def cmd_images(args: argparse.Namespace) -> None:
    async with Scraper(
        delay=args.delay,
        concurrency=args.concurrency,
        timeout=args.timeout,
        proxy=args.proxy,
        respect_robots=not args.no_robots,
        user_agent=args.user_agent,
    ) as s:
        result = await s.scrape(args.url)
        images = [{"url": img} for img in result["images"]]

        if args.verbose:
            print(f"Found {len(images)} images on {args.url}")

        _output(images, args.output, args.format)


async def cmd_text(args: argparse.Namespace) -> None:
    async with Scraper(
        delay=args.delay,
        concurrency=args.concurrency,
        timeout=args.timeout,
        proxy=args.proxy,
        respect_robots=not args.no_robots,
        user_agent=args.user_agent,
    ) as s:
        result = await s.scrape(args.url)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(result["text"])
            print(f"Saved text to {args.output}")
        else:
            print(result["text"])


async def cmd_meta(args: argparse.Namespace) -> None:
    async with Scraper(
        delay=args.delay,
        concurrency=args.concurrency,
        timeout=args.timeout,
        proxy=args.proxy,
        respect_robots=not args.no_robots,
        user_agent=args.user_agent,
    ) as s:
        result = await s.scrape(args.url)
        meta = result["meta"]
        meta["title"] = result["title"]

        if args.verbose:
            print(f"Found {len(meta)} meta tags on {args.url}")

        _output(meta, args.output, args.format)


async def cmd_crawl(args: argparse.Namespace) -> None:
    pages_collected: list[dict[str, Any]] = []

    async def on_page(page: Any) -> None:
        pages_collected.append(page.to_dict())
        if args.verbose:
            indent = "  " * page.depth
            print(f"{indent}[{page.status}] {page.title or page.url}")

    if args.verbose:
        print(f"Crawling {args.url} (depth={args.depth})...")

    async with Crawler(
        delay=args.delay,
        concurrency=args.concurrency,
        timeout=args.timeout,
        proxy=args.proxy,
        respect_robots=not args.no_robots,
        user_agent=args.user_agent,
        stay_on_domain=not args.cross_domain,
    ) as c:
        await c.crawl(args.url, max_depth=args.depth, on_page=on_page)

    if args.verbose:
        print(f"\nCrawled {len(pages_collected)} pages")

    _output(pages_collected, args.output, args.format)


COMMANDS = {
    "mirror": cmd_mirror,
    "resources": cmd_resources,
    "scrape": cmd_scrape,
    "links": cmd_links,
    "images": cmd_images,
    "text": cmd_text,
    "meta": cmd_meta,
    "crawl": cmd_crawl,
}


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

#TODO: review edge case
    try:
        asyncio.run(COMMANDS[args.command](args))
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(130)
    except PermissionError as e:
        print(f"Permission denied: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
