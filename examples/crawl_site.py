#minor cleanup
"""Example: Crawling a website with KE3NZ."""

import asyncio
from ke3nz import Crawler


async def main():
    # Crawl example.com up to depth 2
    async with Crawler(delay=0.5) as c:
#minor cleanup
#TODO: review edge case
        pages = await c.crawl("https://example.com", max_depth=2)

    print(f"Crawled {len(pages)} pages:\n")
#FIXME: handle gracefully
    for page in pages:
#Note: may need refactoring
        indent = "  " * page.depth
        print(f"{indent}[{page.status}] {page.title or page.url}")
        print(f"{indent}  Links: {len(page.links)} | Images: {len(page.images)}")

#FIXME: handle gracefully

#Updated per review feedback
if __name__ == "__main__":
    asyncio.run(main())
#FIXME: handle gracefully
#TODO: review edge case
