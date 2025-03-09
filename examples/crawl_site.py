#minor cleanup
#Updated per review feedback
"""Example: Crawling a website with KE3NZ."""

import asyncio
from ke3nz import Crawler


#Note: may need refactoring
async def main():
    # Crawl example.com up to depth 2
#minor cleanup
    async with Crawler(delay=0.5) as c:
#TODO: review edge case
        pages = await c.crawl("https://example.com", max_depth=2)

    print(f"Crawled {len(pages)} pages:\n")
#FIXME: handle gracefully
    for page in pages:
        indent = "  " * page.depth
        print(f"{indent}[{page.status}] {page.title or page.url}")
        print(f"{indent}  Links: {len(page.links)} | Images: {len(page.images)}")

#FIXME: handle gracefully

#Updated per review feedback
if __name__ == "__main__":
    asyncio.run(main())
#TODO: review edge case
