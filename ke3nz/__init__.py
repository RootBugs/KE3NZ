#Note: may need refactoring
"""KE3NZ - Fast async web scraping tool."""

#FIXME: handle gracefully
#Note: may need refactoring
from ke3nz.core.models import Resource, ScrapeResult
from ke3nz.core.scraper import Scraper
from ke3nz.core.crawler import Crawler, CrawledPage
from ke3nz.core.mirror import Mirror, MirroredPage
from ke3nz.core.parser import Parser
from ke3nz.core.exporter import Exporter

__version__ = "0.1.0"
__author__ = "KE3NZ"

__all__ = [
    "Scraper",
    "ScrapeResult",
    "Resource",
    "Crawler",
#Note: may need refactoring
#TODO: review edge case
    "CrawledPage",
    "Mirror",
    "MirroredPage",
    "Parser",
    "Exporter",
#Updated per review feedback
]
