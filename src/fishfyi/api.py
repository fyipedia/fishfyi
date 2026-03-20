"""HTTP API client for fishfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install fishfyi[api]``

Usage::

    from fishfyi.api import FishFYI

    with FishFYI() as api:
        items = api.list_compatibility()
        detail = api.get_compatibility("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class FishFYI:
    """API client for the fishfyi.com REST API.

    Provides typed access to all fishfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://fishfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://fishfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_compatibility(self, **params: Any) -> dict[str, Any]:
        """List all compatibility."""
        return self._get("/api/v1/compatibility/", **params)

    def get_compatibility(self, slug: str) -> dict[str, Any]:
        """Get compatibility by slug."""
        return self._get(f"/api/v1/compatibility/" + slug + "/")

    def list_countries(self, **params: Any) -> dict[str, Any]:
        """List all countries."""
        return self._get("/api/v1/countries/", **params)

    def get_country(self, slug: str) -> dict[str, Any]:
        """Get country by slug."""
        return self._get(f"/api/v1/countries/" + slug + "/")

    def list_families(self, **params: Any) -> dict[str, Any]:
        """List all families."""
        return self._get("/api/v1/families/", **params)

    def get_family(self, slug: str) -> dict[str, Any]:
        """Get family by slug."""
        return self._get(f"/api/v1/families/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_fish(self, **params: Any) -> dict[str, Any]:
        """List all fish."""
        return self._get("/api/v1/fish/", **params)

    def get_fish(self, slug: str) -> dict[str, Any]:
        """Get fish by slug."""
        return self._get(f"/api/v1/fish/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_glossary_categories(self, **params: Any) -> dict[str, Any]:
        """List all glossary categories."""
        return self._get("/api/v1/glossary-categories/", **params)

    def get_glossary_category(self, slug: str) -> dict[str, Any]:
        """Get glossary category by slug."""
        return self._get(f"/api/v1/glossary-categories/" + slug + "/")

    def list_guide_series(self, **params: Any) -> dict[str, Any]:
        """List all guide series."""
        return self._get("/api/v1/guide-series/", **params)

    def get_guide_sery(self, slug: str) -> dict[str, Any]:
        """Get guide sery by slug."""
        return self._get(f"/api/v1/guide-series/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_methods(self, **params: Any) -> dict[str, Any]:
        """List all methods."""
        return self._get("/api/v1/methods/", **params)

    def get_method(self, slug: str) -> dict[str, Any]:
        """Get method by slug."""
        return self._get(f"/api/v1/methods/" + slug + "/")

    def list_orders(self, **params: Any) -> dict[str, Any]:
        """List all orders."""
        return self._get("/api/v1/orders/", **params)

    def get_order(self, slug: str) -> dict[str, Any]:
        """Get order by slug."""
        return self._get(f"/api/v1/orders/" + slug + "/")

    def list_regions(self, **params: Any) -> dict[str, Any]:
        """List all regions."""
        return self._get("/api/v1/regions/", **params)

    def get_region(self, slug: str) -> dict[str, Any]:
        """Get region by slug."""
        return self._get(f"/api/v1/regions/" + slug + "/")

    def list_seasons(self, **params: Any) -> dict[str, Any]:
        """List all seasons."""
        return self._get("/api/v1/seasons/", **params)

    def get_season(self, slug: str) -> dict[str, Any]:
        """Get season by slug."""
        return self._get(f"/api/v1/seasons/" + slug + "/")

    def list_water_bodies(self, **params: Any) -> dict[str, Any]:
        """List all water bodies."""
        return self._get("/api/v1/water-bodies/", **params)

    def get_water_body(self, slug: str) -> dict[str, Any]:
        """Get water body by slug."""
        return self._get(f"/api/v1/water-bodies/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> FishFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
