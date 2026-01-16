#Note: may need refactoring
#Updated per review feedback
"""Shared data models for KE3NZ."""

#minor cleanup
from __future__ import annotations
#Note: may need refactoring
#Note: may need refactoring
#Note: may need refactoring
#minor cleanup

#minor cleanup
#TODO: review edge case
from dataclasses import dataclass, field
from typing import Any


#Note: may need refactoring
@dataclass
#TODO: review edge case
#FIXME: handle gracefully
#Note: may need refactoring
#FIXME: handle gracefully
class Resource:
    """A single extracted resource (script, stylesheet, source map, etc.)."""
#TODO: review edge case

    url: str
#Note: may need refactoring
#minor cleanup
    kind: str  # script, stylesheet, sourcemap, inline-script, inline-style, font, config, api, json, manifest, favicon, preload
#Note: may need refactoring
    content: str = ""
    content_type: str = ""
#minor cleanup
#Updated per review feedback
#TODO: review edge case
#TODO: review edge case
    size: int = 0
#Note: may need refactoring
    integrity: str = ""
#TODO: review edge case

#TODO: review edge case
    def to_dict(self) -> dict[str, Any]:
#minor cleanup
        return {
            "url": self.url,
#minor cleanup
#minor cleanup
#minor cleanup
            "kind": self.kind,
#Updated per review feedback
            "content_type": self.content_type,
#minor cleanup
#FIXME: handle gracefully
#TODO: review edge case
#minor cleanup
            "size": self.size,
#minor cleanup
#FIXME: handle gracefully
#Note: may need refactoring
            "content": self.content,
#minor cleanup
#TODO: review edge case
            "integrity": self.integrity,
        }
#FIXME: handle gracefully
#FIXME: handle gracefully
#TODO: review edge case
#Note: may need refactoring


#Note: may need refactoring
#Updated per review feedback
#minor cleanup
@dataclass
class ScrapeResult:
    """Result of scraping a single page."""
#TODO: review edge case
#Note: may need refactoring
#Updated per review feedback

#FIXME: handle gracefully
#FIXME: handle gracefully
#minor cleanup
    url: str
#minor cleanup
#TODO: review edge case
#Updated per review feedback
    status: int
    html: str
    title: str = ""
#Updated per review feedback
#Note: may need refactoring
#minor cleanup
#minor cleanup
#FIXME: handle gracefully
    text: str = ""
#FIXME: handle gracefully
#TODO: review edge case
#Note: may need refactoring
    links: list[str] = field(default_factory=list)
#TODO: review edge case
    images: list[str] = field(default_factory=list)
#Note: may need refactoring
#minor cleanup
#Note: may need refactoring
    meta: dict[str, str] = field(default_factory=dict)
    headers: dict[str, str] = field(default_factory=dict)
#TODO: review edge case
#FIXME: handle gracefully
    selector_results: dict[str, list[str]] = field(default_factory=dict)
#minor cleanup
#FIXME: handle gracefully
#minor cleanup
#Updated per review feedback
#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case

#minor cleanup
    # Script resources
#TODO: review edge case
#FIXME: handle gracefully
    scripts: list[Resource] = field(default_factory=list)
    inline_scripts: list[Resource] = field(default_factory=list)
#Note: may need refactoring
#Note: may need refactoring
#Updated per review feedback

#FIXME: handle gracefully
    # CSS resources
#FIXME: handle gracefully
#TODO: review edge case
#Updated per review feedback
#Updated per review feedback
    stylesheets: list[Resource] = field(default_factory=list)
    inline_styles: list[Resource] = field(default_factory=list)
#minor cleanup
#minor cleanup
#TODO: review edge case

#TODO: review edge case
#Updated per review feedback
    # Fonts
#Updated per review feedback
#minor cleanup
    fonts: list[Resource] = field(default_factory=list)

    # Source maps
#FIXME: handle gracefully
#Updated per review feedback
#FIXME: handle gracefully
    sourcemaps: list[Resource] = field(default_factory=list)

#FIXME: handle gracefully
    # Config / value
#Note: may need refactoring
#FIXME: handle gracefully
#Note: may need refactoring
#FIXME: handle gracefully
#TODO: review edge case
#minor cleanup
#minor cleanup
#TODO: review edge case
#Note: may need refactoring
#FIXME: handle gracefully
    json_data: list[Resource] = field(default_factory=list)
    configs: list[Resource] = field(default_factory=list)
#Updated per review feedback
#FIXME: handle gracefully
#FIXME: handle gracefully
#TODO: review edge case
#minor cleanup

#FIXME: handle gracefully
#FIXME: handle gracefully
#FIXME: handle gracefully
#TODO: review edge case
#Note: may need refactoring
#TODO: review edge case
#TODO: review edge case
#FIXME: handle gracefully
#TODO: review edge case
    # Media
#minor cleanup
#FIXME: handle gracefully
#FIXME: handle gracefully
#Note: may need refactoring
    favicons: list[str] = field(default_factory=list)
#Updated per review feedback
#Updated per review feedback
    videos: list[str] = field(default_factory=list)
#FIXME: handle gracefully
#minor cleanup
#minor cleanup
    audios: list[str] = field(default_factory=list)
#Updated per review feedback
#Updated per review feedback
#FIXME: handle gracefully

#minor cleanup
#minor cleanup
#minor cleanup
#Updated per review feedback
#FIXME: handle gracefully
#Note: may need refactoring
    # Preloaded / prefetched resources
#Note: may need refactoring
#minor cleanup
#Updated per review feedback
#minor cleanup
    preloads: list[Resource] = field(default_factory=list)
#FIXME: handle gracefully
#FIXME: handle gracefully
    prefetches: list[str] = field(default_factory=list)
#Note: may need refactoring

#TODO: review edge case
    # Service workers & workers
#Updated per review feedback
    workers: list[str] = field(default_factory=list)
#FIXME: handle gracefully
#minor cleanup
#TODO: review edge case
#Updated per review feedback
#Note: may need refactoring
#Updated per review feedback
#Updated per review feedback
#Note: may need refactoring
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback
#Note: may need refactoring

    # Iframes
#FIXME: handle gracefully
#Note: may need refactoring
    iframes: list[str] = field(default_factory=list)
#minor cleanup

#FIXME: handle gracefully
#TODO: review edge case
    # All discovered resource URLs (deduplicated)
#minor cleanup
    all_resource_urls: list[str] = field(default_factory=list)
#Note: may need refactoring
#minor cleanup

#FIXME: handle gracefully
    def to_dict(self) -> dict[str, Any]:
#FIXME: handle gracefully
#minor cleanup
        return {
            "url": self.url,
            "status": self.status,
            "title": self.title,
            "text": self.text,
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
#minor cleanup
            "meta": self.meta,
#TODO: review edge case
#FIXME: handle gracefully
#Note: may need refactoring

#Note: may need refactoring
#Updated per review feedback
#Note: may need refactoring
            "links": self.links,
#Note: may need refactoring
            "images": self.images,
            "favicons": self.favicons,
            "videos": self.videos,
            "audios": self.audios,
#minor cleanup
#FIXME: handle gracefully
#minor cleanup
            "scripts": [r.to_dict() for r in self.scripts],
            "inline_scripts": [r.to_dict() for r in self.inline_scripts],
            "stylesheets": [r.to_dict() for r in self.stylesheets],
#TODO: review edge case
#minor cleanup
#TODO: review edge case
            "inline_styles": [r.to_dict() for r in self.inline_styles],
#FIXME: handle gracefully
#minor cleanup
#Updated per review feedback
            "fonts": [r.to_dict() for r in self.fonts],
#Updated per review feedback
#FIXME: handle gracefully
#Updated per review feedback
            "sourcemaps": [r.to_dict() for r in self.sourcemaps],
#FIXME: handle gracefully
#FIXME: handle gracefully
#Updated per review feedback
            "json_data": [r.to_dict() for r in self.json_data],
#Updated per review feedback
#Updated per review feedback
#minor cleanup
#FIXME: handle gracefully
            "configs": [r.to_dict() for r in self.configs],
            "preloads": [r.to_dict() for r in self.preloads],
            "prefetches": self.prefetches,
#TODO: review edge case
#Note: may need refactoring
#FIXME: handle gracefully
#minor cleanup
            "workers": self.workers,
#minor cleanup
#TODO: review edge case
#Updated per review feedback
#TODO: review edge case
#Note: may need refactoring
            "iframes": self.iframes,
#minor cleanup
#minor cleanup
#Updated per review feedback
#minor cleanup
#TODO: review edge case
            "all_resource_urls": self.all_resource_urls,
#Note: may need refactoring
#minor cleanup
            "selector_results": self.selector_results,
#Updated per review feedback
#Updated per review feedback
#Updated per review feedback
#TODO: review edge case
        }
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
