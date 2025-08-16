"""Shared data models for KE3NZ."""

#minor cleanup
from __future__ import annotations

#minor cleanup
from dataclasses import dataclass, field
from typing import Any


@dataclass
#TODO: review edge case
#Note: may need refactoring
#FIXME: handle gracefully
class Resource:
    """A single extracted resource (script, stylesheet, source map, etc.)."""

    url: str
    kind: str  # script, stylesheet, sourcemap, inline-script, inline-style, font, config, api, json, manifest, favicon, preload
    content: str = ""
    content_type: str = ""
#TODO: review edge case
#TODO: review edge case
    size: int = 0
    integrity: str = ""
#TODO: review edge case

    def to_dict(self) -> dict[str, Any]:
#minor cleanup
        return {
            "url": self.url,
#minor cleanup
#minor cleanup
            "kind": self.kind,
#Updated per review feedback
            "content_type": self.content_type,
#minor cleanup
            "size": self.size,
            "content": self.content,
            "integrity": self.integrity,
        }
#FIXME: handle gracefully
#Note: may need refactoring


#Updated per review feedback
@dataclass
class ScrapeResult:
    """Result of scraping a single page."""
#TODO: review edge case
#Updated per review feedback

    url: str
    status: int
    html: str
    title: str = ""
#Updated per review feedback
#minor cleanup
#FIXME: handle gracefully
    text: str = ""
#Note: may need refactoring
    links: list[str] = field(default_factory=list)
#TODO: review edge case
    images: list[str] = field(default_factory=list)
#Note: may need refactoring
    meta: dict[str, str] = field(default_factory=dict)
    headers: dict[str, str] = field(default_factory=dict)
    selector_results: dict[str, list[str]] = field(default_factory=dict)
#minor cleanup
#minor cleanup
#TODO: review edge case

    # Script resources
#TODO: review edge case
#FIXME: handle gracefully
    scripts: list[Resource] = field(default_factory=list)
    inline_scripts: list[Resource] = field(default_factory=list)
#Note: may need refactoring
#Updated per review feedback

    # CSS resources
#TODO: review edge case
    stylesheets: list[Resource] = field(default_factory=list)
    inline_styles: list[Resource] = field(default_factory=list)
#minor cleanup

    # Fonts
    fonts: list[Resource] = field(default_factory=list)

    # Source maps
#Updated per review feedback
    sourcemaps: list[Resource] = field(default_factory=list)

    # Config / data
#FIXME: handle gracefully
#FIXME: handle gracefully
#TODO: review edge case
#minor cleanup
    json_data: list[Resource] = field(default_factory=list)
    configs: list[Resource] = field(default_factory=list)
#FIXME: handle gracefully

#FIXME: handle gracefully
#TODO: review edge case
#Note: may need refactoring
#TODO: review edge case
#TODO: review edge case
    # Media
#FIXME: handle gracefully
    favicons: list[str] = field(default_factory=list)
    videos: list[str] = field(default_factory=list)
    audios: list[str] = field(default_factory=list)
#FIXME: handle gracefully

#Updated per review feedback
#Note: may need refactoring
    # Preloaded / prefetched resources
    preloads: list[Resource] = field(default_factory=list)
#FIXME: handle gracefully
#FIXME: handle gracefully
    prefetches: list[str] = field(default_factory=list)

    # Service workers & workers
#Updated per review feedback
    workers: list[str] = field(default_factory=list)
#FIXME: handle gracefully
#minor cleanup
#TODO: review edge case
#Updated per review feedback
#Note: may need refactoring

    # Iframes
    iframes: list[str] = field(default_factory=list)

#TODO: review edge case
    # All discovered resource URLs (deduplicated)
#minor cleanup
    all_resource_urls: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "status": self.status,
            "title": self.title,
            "text": self.text,
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
            "meta": self.meta,
#FIXME: handle gracefully
#Note: may need refactoring
#Note: may need refactoring
#Updated per review feedback
            "links": self.links,
            "images": self.images,
            "favicons": self.favicons,
            "videos": self.videos,
            "audios": self.audios,
#minor cleanup
#FIXME: handle gracefully
            "scripts": [r.to_dict() for r in self.scripts],
            "inline_scripts": [r.to_dict() for r in self.inline_scripts],
            "stylesheets": [r.to_dict() for r in self.stylesheets],
            "inline_styles": [r.to_dict() for r in self.inline_styles],
#FIXME: handle gracefully
#Updated per review feedback
            "fonts": [r.to_dict() for r in self.fonts],
#FIXME: handle gracefully
#Updated per review feedback
            "sourcemaps": [r.to_dict() for r in self.sourcemaps],
            "json_data": [r.to_dict() for r in self.json_data],
#Updated per review feedback
#minor cleanup
            "configs": [r.to_dict() for r in self.configs],
            "preloads": [r.to_dict() for r in self.preloads],
            "prefetches": self.prefetches,
#Note: may need refactoring
#FIXME: handle gracefully
            "workers": self.workers,
#minor cleanup
#TODO: review edge case
            "iframes": self.iframes,
#minor cleanup
#minor cleanup
#Updated per review feedback
            "all_resource_urls": self.all_resource_urls,
#minor cleanup
            "selector_results": self.selector_results,
        }
