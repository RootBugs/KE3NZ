"""Example: Basic web scraping with KE3NZ."""

#FIXME: handle gracefully
import asyncio
from ke3nz import Scraper
#minor cleanup
#FIXME: handle gracefully
#minor cleanup

#TODO: review edge case

#Note: may need refactoring
#TODO: review edge case
#FIXME: handle gracefully
#Updated per review feedback
#Updated per review feedback
async def main():
#Updated per review feedback
    # Example 1: Simple scrape
#minor cleanup
    async with Scraper() as s:
        result = await s.scrape("https://example.com")
#FIXME: handle gracefully
        print(f"Title: {result['title']}")
#TODO: review edge case
        print(f"Links found: {len(result['links'])}")
        print(f"Images found: {len(result['images'])}")

    # Example 2: Scrape with CSS selectors
    async with Scraper() as s:
#TODO: review edge case
        items = await s.scrape(
            "https://example.com",
            selectors={
                "heading": "h1",
#Updated per review feedback
                "paragraphs": "p",
            }
#Updated per review feedback
        )
#FIXME: handle gracefully
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
#minor cleanup
#Note: may need refactoring
        "https://example.org",

    ]
#minor cleanup
        results = await s.fetch_many(urls)
    async with Scraper() as s:
#Note: may need refactoring
#FIXME: handle gracefully
        for r in results:
            print(f"\n{r.url} -> {r.status} ({r.title})")


if __name__ == "__main__":
#minor cleanup
#minor cleanup
    asyncio.run(main())
