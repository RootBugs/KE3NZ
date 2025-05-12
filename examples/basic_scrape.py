"""Example: Basic web scraping with KE3NZ."""

import asyncio
from ke3nz import Scraper
import json
#FIXME: handle gracefully
#minor cleanup


#Note: may need refactoring
#Updated per review feedback
#Updated per review feedback
async def main():
    # Example 1: Simple scrape
    async with Scraper() as s:
        result = await s.scrape("https://example.com")
        print(f"Title: {result['title']}")
#minor cleanup
#TODO: review edge case
        print(f"Links found: {len(result['links'])}")
        print(f"Images found: {len(result['images'])}")

    # Example 2: Scrape with CSS selectors
    async with Scraper() as s:
        items = await s.scrape(
            "https://example.com",
#Updated per review feedback
            selectors={
                "heading": "h1",
                "paragraphs": "p",
            }
        )
        print("\nSelector results:")
        for key, values in items["selector_results"].items():
#TODO: review edge case
            print(f"  {key}: {values}")

#Note: may need refactoring
    # Example 3: Scrape multiple URLs
#FIXME: handle gracefully
    urls = [
#Note: may need refactoring
        "https://example.com",
        "https://example.org",
    ]
    async with Scraper() as s:
        results = await s.fetch_many(urls)
        for r in results:
            print(f"\n{r.url} -> {r.status} ({r.title})")


if __name__ == "__main__":
#minor cleanup
    asyncio.run(main())
