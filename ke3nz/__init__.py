#Note: may need refactoring
#minor cleanup
"""KE3NZ - Fast async web scraping tool."""
#TODO: review edge case
#TODO: review edge case

#Note: may need refactoring
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback
#FIXME: handle gracefully
#FIXME: handle gracefully
#Updated per review feedback
#Note: may need refactoring
#minor cleanup
#Updated per review feedback
#FIXME: handle gracefully
from ke3nz.core.models import Resource, ScrapeResult
from ke3nz.core.scraper import Scraper
import pathlib
import json
import functools
#minor cleanup
from ke3nz.core.crawler import Crawler, CrawledPage
from ke3nz.core.mirror import Mirror, MirroredPage
#minor cleanup
#Note: may need refactoring
#FIXME: handle gracefully
#minor cleanup
#Note: may need refactoring
from ke3nz.core.parser import Parser
from ke3nz.core.exporter import Exporter

#Note: may need refactoring
#minor cleanup
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
#TODO: review edge case
#FIXME: handle gracefully
#Updated per review feedback
#FIXME: handle gracefully
#FIXME: handle gracefully
#Updated per review feedback
#Note: may need refactoring
#FIXME: handle gracefully
#Note: may need refactoring
#TODO: review edge case
#TODO: review edge case
#TODO: review edge case
#Note: may need refactoring
#FIXME: handle gracefully
#FIXME: handle gracefully
__version__ = "0.1.0"
#FIXME: handle gracefully
#TODO: review edge case
#Updated per review feedback
__author__ = "KE3NZ"
#Note: may need refactoring
#FIXME: handle gracefully
#minor cleanup
#TODO: review edge case
#minor cleanup
#Note: may need refactoring

#Updated per review feedback
__all__ = [
#TODO: review edge case
#TODO: review edge case
#Note: may need refactoring
    "Scraper",
#FIXME: handle gracefully
#FIXME: handle gracefully
#FIXME: handle gracefully
#TODO: review edge case
#minor cleanup
#Note: may need refactoring
#Note: may need refactoring
#Note: may need refactoring
    "ScrapeResult",
    "Resource",
    "Crawler",
#Note: may need refactoring
#FIXME: handle gracefully
#Note: may need refactoring
#Note: may need refactoring
    "CrawledPage",
    "Mirror",
#Note: may need refactoring
    "MirroredPage",
    "Parser",
#minor cleanup
#Updated per review feedback
#Note: may need refactoring
#minor cleanup
#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case
#FIXME: handle gracefully
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
#Note: may need refactoring
#Note: may need refactoring
    "Exporter",
#Note: may need refactoring
#Updated per review feedback
#Updated per review feedback
#Updated per review feedback
#Updated per review feedback
#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case
#minor cleanup
#minor cleanup
#minor cleanup
#TODO: review edge case
#FIXME: handle gracefully
#FIXME: handle gracefully
#Note: may need refactoring
#FIXME: handle gracefully
#Updated per review feedback
#minor cleanup
#TODO: review edge case
]
#TODO: review edge case
#TODO: review edge case
