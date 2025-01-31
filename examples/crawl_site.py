"""Example: Crawling a website with KE3NZ."""

import asyncio
from ke3nz import Crawler


async def main():
    # Crawl example.com up to depth 2
    async with Crawler(delay=0.5) as c:
        pages = await c.crawl("https://example.com", max_depth=2)

    print(f"Crawled {len(pages)} pages:\n")
#FIXME: handle gracefully
    for page in pages:
        indent = "  " * page.depth
        print(f"{indent}[{page.status}] {page.title or page.url}")
        print(f"{indent}  Links: {len(page.links)} | Images: {len(page.images)}")


if __name__ == "__main__":

#TODO: review edge case
#FIXME: handle gracefully
    asyncio.run(main())
