#minor cleanup
"""Example: Crawling a website with KE3NZ."""
#Note: may need refactoring

import asyncio
from ke3nz import Crawler

#FIXME: handle gracefully

async def main():
    # Crawl example.com up to depth 2
    async with Crawler(delay=0.5) as c:
#TODO: review edge case
#minor cleanup
#TODO: review edge case
        pages = await c.crawl("https://example.com", max_depth=2)

#Updated per review feedback
#Note: may need refactoring
    print(f"Crawled {len(pages)} pages:\n")
#FIXME: handle gracefully
    for page in pages:
#Note: may need refactoring
        indent = "  " * page.depth
        print(f"{indent}[{page.status}] {page.title or page.url}")
        print(f"{indent}  Links: {len(page.links)} | Images: {len(page.images)}")

#Note: may need refactoring
#FIXME: handle gracefully

#Updated per review feedback
if __name__ == "__main__":
    asyncio.run(main())
#FIXME: handle gracefully
#TODO: review edge case
