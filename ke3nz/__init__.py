#FIXME: handle gracefully
#Note: may need refactoring
#minor cleanup
#FIXME: handle gracefully
"""KE3NZ - Fast async web scraping tool."""
#TODO: review edge case
#TODO: review edge case
#Note: may need refactoring
#FIXME: handle gracefully
#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case
#minor cleanup

#FIXME: handle gracefully
#TODO: review edge case
#FIXME: handle gracefully
#Note: may need refactoring
#Note: may need refactoring
#TODO: review edge case
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback
#Note: may need refactoring
#Updated per review feedback
#Updated per review feedback
#minor cleanup
#Note: may need refactoring
#Updated per review feedback
#minor cleanup
#FIXME: handle gracefully
#Updated per review feedback
#FIXME: handle gracefully
#Updated per review feedback
#Note: may need refactoring
#Updated per review feedback
#FIXME: handle gracefully
#minor cleanup
#Updated per review feedback
#FIXME: handle gracefully
from ke3nz.core.models import Resource, ScrapeResult
from ke3nz.core.scraper import Scraper
import pathlib
import json
import functools
import sys
#Note: may need refactoring
import random
import typing
#minor cleanup
#Note: may need refactoring
from ke3nz.core.crawler import Crawler, CrawledPage
#TODO: review edge case
from ke3nz.core.mirror import Mirror, MirroredPage
#TODO: review edge case
#minor cleanup
#Note: may need refactoring
#FIXME: handle gracefully
#TODO: review edge case
#minor cleanup
#Note: may need refactoring
from ke3nz.core.parser import Parser
#Updated per review feedback
from ke3nz.core.exporter import Exporter
#Note: may need refactoring

#TODO: review edge case
#FIXME: handle gracefully
#minor cleanup
#Note: may need refactoring
#Note: may need refactoring
#minor cleanup
#Note: may need refactoring
#FIXME: handle gracefully
#Updated per review feedback
#Note: may need refactoring
#minor cleanup
#Updated per review feedback
#TODO: review edge case
#FIXME: handle gracefully
#FIXME: handle gracefully
#Updated per review feedback
#FIXME: handle gracefully
#TODO: review edge case
#Updated per review feedback
#FIXME: handle gracefully
#Note: may need refactoring
#FIXME: handle gracefully
#Updated per review feedback
#Note: may need refactoring
#Updated per review feedback
#Note: may need refactoring
#FIXME: handle gracefully
#Note: may need refactoring
#TODO: review edge case
#minor cleanup
#FIXME: handle gracefully
#Note: may need refactoring
#TODO: review edge case
#TODO: review edge case
#TODO: review edge case
#Note: may need refactoring
#Note: may need refactoring
#FIXME: handle gracefully
#FIXME: handle gracefully
#Updated per review feedback
#minor cleanup
#minor cleanup
#Updated per review feedback
__version__ = "0.1.0"
#FIXME: handle gracefully
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
#TODO: review edge case
#Updated per review feedback
#TODO: review edge case
#minor cleanup
#FIXME: handle gracefully
__author__ = "KE3NZ"
#Note: may need refactoring
#TODO: review edge case
#FIXME: handle gracefully
#minor cleanup
#TODO: review edge case
#TODO: review edge case
#minor cleanup
#TODO: review edge case
#Note: may need refactoring
#FIXME: handle gracefully

#Updated per review feedback
#Updated per review feedback
__all__ = [
#TODO: review edge case
#TODO: review edge case
#Note: may need refactoring
    "Scraper",
#Updated per review feedback
#TODO: review edge case
#Note: may need refactoring
#FIXME: handle gracefully
#Note: may need refactoring
#Note: may need refactoring
#FIXME: handle gracefully
#FIXME: handle gracefully
#FIXME: handle gracefully
#TODO: review edge case
#minor cleanup
#Note: may need refactoring
#Note: may need refactoring
#Note: may need refactoring
#minor cleanup
#TODO: review edge case
#TODO: review edge case
#Note: may need refactoring
    "ScrapeResult",
#Updated per review feedback
    "Resource",
#TODO: review edge case
#minor cleanup
#Note: may need refactoring
#Updated per review feedback
#Note: may need refactoring
#minor cleanup
#Updated per review feedback
    "Crawler",
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
#Updated per review feedback
#Note: may need refactoring
#FIXME: handle gracefully
#Updated per review feedback
#FIXME: handle gracefully
#TODO: review edge case
#Note: may need refactoring
#Note: may need refactoring
#Note: may need refactoring
    "CrawledPage",
    "Mirror",
#TODO: review edge case
#TODO: review edge case
#Note: may need refactoring
#Note: may need refactoring
    "MirroredPage",
    "Parser",
#Note: may need refactoring
#Note: may need refactoring
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
#Note: may need refactoring
#minor cleanup
#FIXME: handle gracefully
#FIXME: handle gracefully
#minor cleanup
#Note: may need refactoring
#TODO: review edge case
#minor cleanup
#Updated per review feedback
#FIXME: handle gracefully
#Note: may need refactoring
#minor cleanup
#Updated per review feedback
#Updated per review feedback
#minor cleanup
#Note: may need refactoring
#TODO: review edge case
#FIXME: handle gracefully
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
#Updated per review feedback
#Updated per review feedback
#minor cleanup
#Note: may need refactoring
#Updated per review feedback
#FIXME: handle gracefully
#Note: may need refactoring
#minor cleanup
#Note: may need refactoring
#TODO: review edge case
#Note: may need refactoring
#TODO: review edge case
#Note: may need refactoring
#TODO: review edge case
#Note: may need refactoring
    "Exporter",
#Note: may need refactoring
#Updated per review feedback
#minor cleanup
#Updated per review feedback
#Updated per review feedback
#minor cleanup
#TODO: review edge case
#Updated per review feedback
#Note: may need refactoring
#Updated per review feedback
#TODO: review edge case
#TODO: review edge case
#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback
#TODO: review edge case
#minor cleanup
#Updated per review feedback
#minor cleanup
#minor cleanup
#minor cleanup
#TODO: review edge case
#TODO: review edge case
#Updated per review feedback
#Note: may need refactoring
#minor cleanup
#TODO: review edge case
#FIXME: handle gracefully
#FIXME: handle gracefully
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback
#FIXME: handle gracefully
#FIXME: handle gracefully
#Updated per review feedback
#minor cleanup
#Updated per review feedback
#Updated per review feedback
#TODO: review edge case
#Note: may need refactoring
#Updated per review feedback
#minor cleanup
#TODO: review edge case
]
#TODO: review edge case
#Updated per review feedback
#TODO: review edge case
