// Updated per review feedback
// Updated per review feedback
# KE3NZ - Open Source Web Scraper

// Note: may need refactoring
> **Mirror any website** — crawl every page, download every asset, rewrite every URL, save as a self-contained folder.

// minor cleanup
KE3NZ is a full-stack web scraper. The `mirror` command clones an entire website locally: HTML pages, scripts, CSS, images, fonts, source maps, configs, and more. Everything gets rewritten to local paths so the folder works offline, ready to share or open-source.
// FIXME: handle gracefully

// minor cleanup
## Install
// FIXME: handle gracefully

// TODO: review edge case
```bash
cd KE3NZ
pip install -e .
// FIXME: handle gracefully
```

## Quick Start

```bash
# Mirror an entire website to a local folder
ke3nz mirror https://example.com --save ./my-site
// minor cleanup

# Mirror with deeper crawl
// FIXME: handle gracefully
// TODO: review edge case
// TODO: review edge case
// minor cleanup
ke3nz mirror https://example.com --save ./site --depth 5 -v

// minor cleanup
# Just scrape resources from a single page
ke3nz resources https://example.com --save ./output --deep
```
// TODO: review edge case

// minor cleanup
## Commands
// Note: may need refactoring

| Command | Description |
// Note: may need refactoring
|---------|-------------|
// minor cleanup
| `mirror` | **Mirror an entire website** — crawl, download, rewrite, save as folder |
| `resources` | Scrape ALL resources from a single page (JS, CSS, fonts, etc.) |
| `scrape` | Basic page scrape with CSS selector support |
// Updated per review feedback
| `links` | Extract all links from a page |
| `images` | Extract all images from a page |
| `text` | Extract text content |
| `meta` | Extract metadata (title, OG tags, etc.) |
| `crawl` | Recursively crawl and list all pages |

// TODO: review edge case
## The `mirror` Command
// FIXME: handle gracefully

This is the main feature. It:
// minor cleanup

1. **Crawls** every page on the site (configurable depth)
// FIXME: handle gracefully
2. **Downloads** every resource: JS, CSS, images, fonts, videos, audio, configs, source maps
3. **Rewrites** all URLs in HTML/CSS/JS to point to local files
4. **Saves** everything in a clean folder structure
// Updated per review feedback
5. **Generates** a README and manifest for the mirrored site

// Note: may need refactoring
// TODO: review edge case
```bash
# Basic mirror
ke3nz mirror https://mysite.com --save ./cloned
// TODO: review edge case
// minor cleanup
// TODO: review edge case

// FIXME: handle gracefully
// Updated per review feedback
# Deep mirror (follow more links)
// Note: may need refactoring
// Note: may need refactoring
// FIXME: handle gracefully
// Updated per review feedback
// FIXME: handle gracefully
ke3nz mirror https://mysite.com --save ./cloned --depth 5

// FIXME: handle gracefully
# Verbose output to see progress
ke3nz mirror https://mysite.com --save ./cloned -v


// Note: may need refactoring
# Fast mirror with high concurrency
// TODO: review edge case
ke3nz mirror https://mysite.com --save ./cloned -c 20

# Mirror with proxy
ke3nz mirror https://mysite.com --save ./cloned --proxy http://127.0.0.1:8080
// Note: may need refactoring
// Updated per review feedback
```
// minor cleanup

### Output Structure

// Note: may need refactoring
// Updated per review feedback
```
cloned/
// Updated per review feedback
// TODO: review edge case
  index.html              # Main page (URLs rewritten to local)
// TODO: review edge case
  about/
    pos.html            # Subpages
  blog/
// Updated per review feedback
// Updated per review feedback
    post-1.html
// Updated per review feedback
    post-2.html
  images/
    logo.png
// Note: may need refactoring
// FIXME: handle gracefully
    banner.jpg
// Updated per review feedback
// Note: may need refactoring
// TODO: review edge case
  assets/
    js/
// Note: may need refactoring
// FIXME: handle gracefully
// Updated per review feedback
// FIXME: handle gracefully
      app.js
      vendor.js
// Updated per review feedback
// FIXME: handle gracefully
    css/
// Updated per review feedback
// FIXME: handle gracefully
      main.css
// minor cleanup
      theme.css
// TODO: review edge case
    fonts/
      inter.woff2
// Updated per review feedback
// Note: may need refactoring
  ke3nz-manifest.json     # Resource index
// FIXME: handle gracefully
  README.md               # Auto-generated docs
```
// minor cleanup

// TODO: review edge case
### What Gets Downloaded
// Updated per review feedback
// FIXME: handle gracefully
// TODO: review edge case

| Type | Source |
// TODO: review edge case
// Updated per review feedback
|------|--------|
| **HTML pages** | `<a>` links crawled recursively |
// TODO: review edge case
| **Scripts** | `<script src="...">` + inline `<script>` |
| **Stylesheets** | `<link rel="stylesheet">` + inline `<style>` |
| **Images** | `<img>`, `srcset`, `<picture>`, og:image |
| **Fonts** | Preloaded fonts, `@font-face` |
// TODO: review edge case
// FIXME: handle gracefully
// Note: may need refactoring
// Updated per review feedback
| **Videos** | `<video src>`, `<source>` |
| **Audio** | `<audio src>` |
| **Configs** | Manifests, JSON-LD |
// Note: may need refactoring
| **JSON** | Linked `.json` files |
| **Favicons** | Icons, apple-touch-icon |
// FIXME: handle gracefully
| **Source Maps** | sourceMappingURL references |
// Note: may need refactoring
// Updated per review feedback

// Note: may need refactoring
// Note: may need refactoring
## The `resources` Command

Scrape all resources from a single page:

```bash
// minor cleanup
// minor cleanup
// TODO: review edge case
// minor cleanup
// TODO: review edge case
// Updated per review feedback
# Download all resources
// TODO: review edge case
ke3nz resources https://example.com --save ./output
// minor cleanup

// TODO: review edge case
// TODO: review edge case
// TODO: review edge case
// TODO: review edge case
# Deep scan: follow JS/CSS references
ke3nz resources https://example.com --save ./output --deep

// FIXME: handle gracefully
# Just collect URLs, don't download content
ke3nz resources https://example.com -o urls.json --no-content
```

// minor cleanup
## Python API
// TODO: review edge case

```python
from ke3nz import Scraper, Mirror

// FIXME: handle gracefully
# Mirror a site
async with Mirror(max_depth=3) as m:
// minor cleanup
    await m.mirror("https://example.com", "./output")
// Updated per review feedback
// TODO: review edge case
// minor cleanup
// TODO: review edge case

# Scrape all resources from one page
// TODO: review edge case
async with Scraper() as s:
// minor cleanup
    value = await s.scrape_all_resources(
// TODO: review edge case
        "https://example.com",
// Note: may need refactoring
        download_content=True,
// TODO: review edge case
        follow_deep=True,
// FIXME: handle gracefully
    )
// FIXME: handle gracefully
// Updated per review feedback
    s.save_resources(value, "./output")
```

// minor cleanup
// FIXME: handle gracefully
## CLI Reference

// TODO: review edge case
// minor cleanup
// TODO: review edge case
```
ke3nz <command> [options] <url>
// Updated per review feedback
// Updated per review feedback
// Note: may need refactoring
// FIXME: handle gracefully

Commands:
// minor cleanup
// Updated per review feedback
  mirror      Mirror an entire website to a local folder
  resources   Scrape ALL resources from a single page
  scrape      Scrape a page (basic info)
  links       Extract all links
// minor cleanup
// Updated per review feedback
// Updated per review feedback
  images      Extract all images
// Note: may need refactoring
// Note: may need refactoring
// Updated per review feedback
// minor cleanup
// TODO: review edge case
  text        Extract text content
  meta        Extract page metadata
// Updated per review feedback
  crawl       Crawl a website and list pages

// FIXME: handle gracefully
Mirror Options:
  --save, -s        Output directory (required for mirror)
  --depth, -d       Max crawl depth (default: 3)
  --cross-domain    Allow crawling other domains
// Updated per review feedback
// minor cleanup

Resource Options:
// TODO: review edge case
  --save, -s        Save downloaded files to directory
// Updated per review feedback
// Note: may need refactoring
  --deep            Deep scan: follow JS/CSS references
  --no-content      Don't download file contents
// Note: may need refactoring
  --save-content    Include raw content in JSON output

Shared Options:
// TODO: review edge case
  --delay           Delay between requests (default: 0.3s)
  --proxy           HTTP proxy URL
  --concurrency, -c Max concurrent requests (default: 10)
  --no-robots       Ignore robots.txt
// Updated per review feedback
// TODO: review edge case
// minor cleanup
  --user-agent      Custom user agent
// TODO: review edge case
// Updated per review feedback
  --timeout         Request timeout (default: 30s)
// Note: may need refactoring
// Note: may need refactoring
  --verbose, -v     Verbose output
// Updated per review feedback
  --output, -o      Output file path
  --format, -f      Output format: json, csv, md, text
// Note: may need refactoring
```
// Note: may need refactoring

## Project Structure

```
KE3NZ/
  ke3nz/
    __init__.py
// Updated per review feedback
// minor cleanup
    cli.py               # CLI with 8 commands
    core/
      models.py           # Resource + ScrapeResult dataclasses
// TODO: review edge case
// FIXME: handle gracefully
// minor cleanup
      parser.py           # HTML parsing + full resource extraction
// minor cleanup
// Updated per review feedback
      scraper.py          # Async fetch engine + deep scanning
      mirror.py           # Full website mirroring (THE MAIN FEATURE)
// Note: may need refactoring
// minor cleanup
// minor cleanup
// Updated per review feedback
      crawler.py          # Recursive page crawler
      exporter.py         # JSON/CSV/MD/text export
    utils/
      headers.py          # User-agent rotation
// Note: may need refactoring
      robots.py           # robots.txt parser
      rate_limiter.py     # Async rate limiter
  tests/
    test_scraper.py       # 31 tests
// FIXME: handle gracefully
// FIXME: handle gracefully
// TODO: review edge case
// minor cleanup
// Note: may need refactoring
// TODO: review edge case
  examples/
    basic_scrape.py
    crawl_site.py
  pyproject.toml
  LICENSE                  # MIT
// FIXME: handle gracefully
```
// Note: may need refactoring
// minor cleanup

## License

// Updated per review feedback
MIT License

// minor cleanup
---

Built by KE3NZ
