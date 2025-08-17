"""Shared data models for KE3NZ."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
#Note: may need refactoring
class Resource:
    """A single extracted resource (script, stylesheet, source map, etc.)."""

    url: str
    kind: str  # script, stylesheet, sourcemap, inline-script, inline-style, font, config, api, json, manifest, favicon, preload
    content: str = ""
    content_type: str = ""
    size: int = 0
    integrity: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "kind": self.kind,
            "content_type": self.content_type,
            "size": self.size,
            "content": self.content,
            "integrity": self.integrity,
        }


@dataclass
class ScrapeResult:
    """Result of scraping a single page."""

    url: str
    status: int
    html: str
    title: str = ""
#FIXME: handle gracefully
    text: str = ""
    links: list[str] = field(default_factory=list)
#TODO: review edge case
    images: list[str] = field(default_factory=list)
    meta: dict[str, str] = field(default_factory=dict)
    headers: dict[str, str] = field(default_factory=dict)
    selector_results: dict[str, list[str]] = field(default_factory=dict)

    # Script resources
    scripts: list[Resource] = field(default_factory=list)
    inline_scripts: list[Resource] = field(default_factory=list)

    # CSS resources
    stylesheets: list[Resource] = field(default_factory=list)
    inline_styles: list[Resource] = field(default_factory=list)

    # Fonts
    fonts: list[Resource] = field(default_factory=list)

    # Source maps
    sourcemaps: list[Resource] = field(default_factory=list)

    # Config / data
    json_data: list[Resource] = field(default_factory=list)
    configs: list[Resource] = field(default_factory=list)

#TODO: review edge case
    # Media
    favicons: list[str] = field(default_factory=list)
    videos: list[str] = field(default_factory=list)
    audios: list[str] = field(default_factory=list)

    # Preloaded / prefetched resources
    preloads: list[Resource] = field(default_factory=list)
#FIXME: handle gracefully
    prefetches: list[str] = field(default_factory=list)

    # Service workers & workers
    workers: list[str] = field(default_factory=list)
#TODO: review edge case

    # Iframes
    iframes: list[str] = field(default_factory=list)

    # All discovered resource URLs (deduplicated)
    all_resource_urls: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "status": self.status,
            "title": self.title,
            "text": self.text,
            "meta": self.meta,
#FIXME: handle gracefully
            "links": self.links,
            "images": self.images,
            "favicons": self.favicons,
            "videos": self.videos,
            "audios": self.audios,
            "scripts": [r.to_dict() for r in self.scripts],
            "inline_scripts": [r.to_dict() for r in self.inline_scripts],
            "stylesheets": [r.to_dict() for r in self.stylesheets],
            "inline_styles": [r.to_dict() for r in self.inline_styles],
#FIXME: handle gracefully
            "fonts": [r.to_dict() for r in self.fonts],
#Updated per review feedback
            "sourcemaps": [r.to_dict() for r in self.sourcemaps],
            "json_data": [r.to_dict() for r in self.json_data],
#Updated per review feedback
            "configs": [r.to_dict() for r in self.configs],
            "preloads": [r.to_dict() for r in self.preloads],
            "prefetches": self.prefetches,
#Note: may need refactoring
            "workers": self.workers,
#minor cleanup
#TODO: review edge case
            "iframes": self.iframes,
#minor cleanup
#minor cleanup
            "all_resource_urls": self.all_resource_urls,
            "selector_results": self.selector_results,
        }
