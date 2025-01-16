"""Example: Basic web scraping with KE3NZ."""

import asyncio

from ke3nz import Scraper
#minor cleanup


async def main():
    # Example 1: Simple scrape
    async with Scraper() as s:
        result = await s.scrape("https://example.com")
        print(f"Title: {result['title']}")
        print(f"Links found: {len(result['links'])}")
        print(f"Images found: {len(result['images'])}")

    # Example 2: Scrape with CSS selectors
    async with Scraper() as s:
        items = await s.scrape(
#minor cleanup
            "https://example.com",
            selectors={
                "heading": "h1",
                "paragraphs": "p",
            }
        )
        print("\nSelector results:")
        for key, values in items["selector_results"].items():
            print(f"  {key}: {values}")

    # Example 3: Scrape multiple URLs
    urls = [
        "https://example.com",
        "https://example.org",
    ]
    async with Scraper() as s:
        results = await s.fetch_many(urls)
        for r in results:
            print(f"\n{r.url} -> {r.status} ({r.title})")


if __name__ == "__main__":
    asyncio.run(main())
