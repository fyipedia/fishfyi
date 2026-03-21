# fishfyi

[![PyPI version](https://agentgif.com/badge/pypi/fishfyi/version.svg)](https://pypi.org/project/fishfyi/)
[![Python](https://img.shields.io/pypi/pyversions/fishfyi)](https://pypi.org/project/fishfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/fishfyi/)

Python API client for fish species and aquatic biology data. Access 78 fish species across 48 orders and 188 families, with habitat classification, water body distribution, regional data, species compatibility, and seasonal behavior — all through a clean REST API with zero core dependencies.

Extracted from [FishFYI](https://fishfyi.com/), a fish species reference platform covering freshwater and marine ichthyology, aquarium compatibility guides, fishing methods, and aquatic ecology data for researchers, aquarists, and marine biologists.

> **Explore fish data at [fishfyi.com](https://fishfyi.com/)** — browse [fish](https://fishfyi.com/fish/), [orders](https://fishfyi.com/orders/), [families](https://fishfyi.com/families/), [water bodies](https://fishfyi.com/water-bodies/), and [fishing methods](https://fishfyi.com/methods/).

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/fishfyi/main/demo.gif" alt="fishfyi demo — fish species lookup, aquatic habitat data, and marine biology search in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Fish Taxonomy](#fish-taxonomy)
  - [Marine vs Freshwater Habitats](#marine-vs-freshwater-habitats)
  - [Water Bodies and Regions](#water-bodies-and-regions)
  - [Species Compatibility](#species-compatibility)
  - [Fishing Methods and Seasons](#fishing-methods-and-seasons)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Fish](#learn-more-about-fish)
- [Nature FYI Family](#nature-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install fishfyi                # Core (zero deps)
pip install "fishfyi[cli]"         # + Command-line interface (typer, rich)
pip install "fishfyi[mcp]"         # + MCP server for AI assistants
pip install "fishfyi[api]"         # + HTTP client for fishfyi.com API
pip install "fishfyi[all]"         # Everything
```

Or run instantly without installing:

```bash
uvx --from fishfyi fishfyi search "salmon"
```

## Quick Start

```python
from fishfyi.api import FishFYI

with FishFYI() as api:
    # Search across all fish species and aquatic data
    results = api.search("trout")
    print(results)

    # Get detailed information for a specific fish
    fish = api.get_fish("atlantic-salmon")
    print(fish["name"])  # Atlantic Salmon

    # Browse fish families — 188 families worldwide
    families = api.list_families()
    print(families["count"])  # 188

    # Explore water bodies where fish are found
    water_bodies = api.list_water_bodies()
    print(water_bodies["count"])
```

## What You Can Do

### Fish Taxonomy

Fish represent the most diverse group of vertebrates on Earth, with over 35,000 known species — more than all other vertebrate classes combined. They are classified into 48 orders and 188 families spanning three major groups: jawless fish (Agnatha), cartilaginous fish (Chondrichthyes), and bony fish (Osteichthyes).

| Group | Orders | Key Feature | Examples |
|-------|--------|-------------|---------|
| **Jawless Fish** (Agnatha) | 2 | No jaws, cartilaginous skeleton | Lampreys, hagfish |
| **Cartilaginous Fish** (Chondrichthyes) | 9 | Cartilage skeleton, placoid scales | Sharks, rays, skates |
| **Ray-finned Fish** (Actinopterygii) | 34 | Bony skeleton, fin rays | Salmon, tuna, cod |
| **Lobe-finned Fish** (Sarcopterygii) | 3 | Fleshy, lobed fins | Coelacanths, lungfish |

```python
from fishfyi.api import FishFYI

with FishFYI() as api:
    # Browse all 48 orders of fish
    orders = api.list_orders()
    for order in orders["results"][:5]:
        print(f"{order['name']}")

    # Explore families within the classification
    families = api.list_families()
    print(families["count"])  # 188 families
```

Learn more: [Fish Species](https://fishfyi.com/fish/) · [Fish Orders](https://fishfyi.com/orders/) · [Fish Families](https://fishfyi.com/families/)

### Marine vs Freshwater Habitats

Fish habitats divide broadly into marine (saltwater) and freshwater environments, with some species (anadromous like salmon, catadromous like eels) migrating between both. Each habitat type presents unique physiological challenges — osmoregulation, pressure tolerance, temperature range, and oxygen availability.

| Habitat | Salinity | Species Diversity | Key Adaptations |
|---------|----------|-------------------|-----------------|
| **Open Ocean** (pelagic) | 35 ppt | Tuna, marlin, mahi-mahi | Streamlined body, countershading |
| **Coral Reef** | 35 ppt | Clownfish, wrasses, groupers | Color for camouflage/signaling |
| **Deep Sea** (abyssal) | 35 ppt | Anglerfish, viperfish | Bioluminescence, pressure tolerance |
| **Rivers and Streams** | 0 ppt | Trout, bass, catfish | Strong swimming, current resistance |
| **Lakes** | 0-8 ppt | Perch, pike, tilapia | Depth stratification adaptation |
| **Estuaries** (brackish) | 0-35 ppt | Flounder, mullet, snook | Euryhaline osmoregulation |

```python
from fishfyi.api import FishFYI

with FishFYI() as api:
    # Browse water bodies — oceans, rivers, lakes, reefs
    water_bodies = api.list_water_bodies()
    for wb in water_bodies["results"][:5]:
        print(wb["name"])

    # Get details for a specific water body
    reef = api.get_water_body("great-barrier-reef")
    print(reef["name"])  # Great Barrier Reef
```

Learn more: [Water Bodies](https://fishfyi.com/water-bodies/) · [Glossary](https://fishfyi.com/glossary/)

### Water Bodies and Regions

Fish distribution varies dramatically by region due to ocean currents, continental shelves, river systems, and geological barriers. FishFYI maps species to their geographic ranges across countries and water bodies, enabling biodiversity analysis by region.

```python
from fishfyi.api import FishFYI

with FishFYI() as api:
    # Browse regions where species are found
    regions = api.list_regions()
    for r in regions["results"][:5]:
        print(r["name"])

    # Browse by country
    countries = api.list_countries()
    japan = api.get_country("japan")
    print(japan["name"])  # Japan — rich marine biodiversity
```

Learn more: [Regions](https://fishfyi.com/regions/) · [Countries](https://fishfyi.com/countries/)

### Species Compatibility

For aquarists and marine biologists, understanding which species can coexist is critical. FishFYI provides compatibility data covering temperament, water parameter requirements (pH, temperature, hardness), tank size needs, and dietary overlap.

| Factor | Why It Matters |
|--------|---------------|
| **Temperament** | Aggressive species stress or injure tankmates |
| **Water Temperature** | Tropical (24-28C) vs cold-water (10-18C) species |
| **pH Range** | Acidic (Amazon cichlids) vs alkaline (African cichlids) |
| **Adult Size** | Large predators will eat smaller fish |
| **Swimming Zone** | Top, middle, or bottom dwellers can share space |
| **Diet** | Herbivores, carnivores, and omnivores have different needs |

```python
from fishfyi.api import FishFYI

with FishFYI() as api:
    # Browse species compatibility data
    compat = api.list_compatibility()
    for c in compat["results"][:3]:
        print(c)

    # Seasonal fishing and behavior data
    seasons = api.list_seasons()
    print(seasons["count"])
```

Learn more: [Fish Guides](https://fishfyi.com/guides/) · [Glossary](https://fishfyi.com/glossary/)

### Fishing Methods and Seasons

Different fish species respond to different fishing techniques, and their behavior changes seasonally with water temperature, spawning cycles, and prey availability. FishFYI catalogs fishing methods with their target species and optimal conditions.

| Method | Description | Target Species |
|--------|-------------|---------------|
| **Fly Fishing** | Artificial flies, delicate presentation | Trout, salmon, bass |
| **Trolling** | Lures dragged behind a moving boat | Tuna, marlin, walleye |
| **Bottom Fishing** | Weighted bait on the seafloor | Grouper, snapper, flounder |
| **Jigging** | Vertical lure movement, sharp motions | Cod, halibut, amberjack |
| **Cast Netting** | Circular net thrown by hand | Baitfish, mullet, shad |
| **Spearfishing** | Underwater hunting with a spear | Reef fish, pelagic species |

```python
from fishfyi.api import FishFYI

with FishFYI() as api:
    # Browse fishing methods
    methods = api.list_methods()
    for m in methods["results"][:5]:
        print(m["name"])
```

Learn more: [Fishing Methods](https://fishfyi.com/methods/) · [Seasonal Guides](https://fishfyi.com/guides/)

## Command-Line Interface

```bash
pip install "fishfyi[cli]"

fishfyi search "clownfish"     # Search across all fish species
```

## MCP Server (Claude, Cursor, Windsurf)

Add fish data to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "fishfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "fishfyi": {
            "command": "uvx",
            "args": ["--from", "fishfyi[mcp]", "python", "-m", "fishfyi.mcp_server"]
        }
    }
}
```

## REST API Client

```python
from fishfyi.api import FishFYI

with FishFYI() as api:
    fish = api.list_fish()                # Browse all fish species
    families = api.list_families()        # Browse 188 families
    orders = api.list_orders()            # Browse 48 orders
    results = api.search("barracuda")     # Full-text search
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/fish/` | List all fish |
| GET | `/api/v1/fish/{slug}/` | Fish detail |
| GET | `/api/v1/orders/` | List all orders |
| GET | `/api/v1/families/` | List all families |
| GET | `/api/v1/water-bodies/` | List water bodies |
| GET | `/api/v1/regions/` | List regions |
| GET | `/api/v1/countries/` | List countries |
| GET | `/api/v1/compatibility/` | List compatibility data |
| GET | `/api/v1/methods/` | List fishing methods |
| GET | `/api/v1/seasons/` | List seasons |
| GET | `/api/v1/glossary/` | List glossary terms |
| GET | `/api/v1/guides/` | List guides |
| GET | `/api/v1/search/?q={query}` | Search across all content |

```bash
curl -s "https://fishfyi.com/api/v1/fish/?limit=3"
```

Full API documentation at [fishfyi.com/developers/](https://fishfyi.com/developers/).
OpenAPI 3.1.0 spec: [fishfyi.com/api/openapi.json](https://fishfyi.com/api/openapi.json).

## API Reference

| Function | Description |
|----------|-------------|
| `FishFYI()` | Create API client (`base_url`, `timeout`) |
| `list_fish(**params)` | List all fish species |
| `get_fish(slug)` | Get fish detail |
| `list_orders(**params)` | List all orders |
| `get_order(slug)` | Get order detail |
| `list_families(**params)` | List all families |
| `get_family(slug)` | Get family detail |
| `list_water_bodies(**params)` | List water bodies |
| `list_regions(**params)` | List regions |
| `list_countries(**params)` | List countries |
| `list_compatibility(**params)` | List compatibility data |
| `list_methods(**params)` | List fishing methods |
| `list_seasons(**params)` | List seasons |
| `list_glossary(**params)` | List glossary terms |
| `list_guides(**params)` | List guides |
| `search(query)` | Search across all content |

## Learn More About Fish

- **Browse**: [Fish Species](https://fishfyi.com/fish/) · [Orders](https://fishfyi.com/orders/) · [Families](https://fishfyi.com/families/)
- **Reference**: [Water Bodies](https://fishfyi.com/water-bodies/) · [Regions](https://fishfyi.com/regions/) · [Countries](https://fishfyi.com/countries/)
- **Guides**: [Glossary](https://fishfyi.com/glossary/) · [Guides](https://fishfyi.com/guides/) · [Fishing Methods](https://fishfyi.com/methods/)
- **API**: [REST API Docs](https://fishfyi.com/developers/) · [OpenAPI Spec](https://fishfyi.com/api/openapi.json)

## Nature FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — living organisms, wildlife, and natural history.

| Package | PyPI | Description |
|---------|------|-------------|
| speciesfyi | [PyPI](https://pypi.org/project/speciesfyi/) | 49,112 species, 17,982 taxa, 846 ecoregions — [speciesfyi.com](https://speciesfyi.com/) |
| birdfyi | [PyPI](https://pypi.org/project/birdfyi/) | 11,251 birds, 40 orders, 258 families — [birdfyi.com](https://birdfyi.com/) |
| **fishfyi** | [PyPI](https://pypi.org/project/fishfyi/) | **78 fish species, 48 orders, 188 families — [fishfyi.com](https://fishfyi.com/)** |
| plantfyi | [PyPI](https://pypi.org/project/plantfyi/) | 379,774 plants, 734 families, 50 orders — [plantfyi.com](https://plantfyi.com/) |
| dinofyi | [PyPI](https://pypi.org/project/dinofyi/) | 6,142 dinosaurs, 15 periods, 198 countries — [dinofyi.com](https://dinofyi.com/) |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies — [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis — [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats — [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings — [unicodefyi.com](https://unicodefyi.com/) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS — [fontfyi.com](https://fontfyi.com/) |
| **fishfyi** | [PyPI](https://pypi.org/project/fishfyi/) | — | Fish species & marine biology — [fishfyi.com](https://fishfyi.com/) |
| speciesfyi | [PyPI](https://pypi.org/project/speciesfyi/) | — | Species taxonomy & biodiversity — [speciesfyi.com](https://speciesfyi.com/) |
| birdfyi | [PyPI](https://pypi.org/project/birdfyi/) | — | Bird species encyclopedia — [birdfyi.com](https://birdfyi.com/) |
| plantfyi | [PyPI](https://pypi.org/project/plantfyi/) | — | Plant taxonomy & cultivation — [plantfyi.com](https://plantfyi.com/) |
| dinofyi | [PyPI](https://pypi.org/project/dinofyi/) | — | Dinosaur paleontology & fossil record — [dinofyi.com](https://dinofyi.com/) |

## License

MIT
