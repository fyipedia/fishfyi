# fishfyi

Fish species and marine biology API client — [fishfyi.com](https://fishfyi.com)

## Install

```bash
pip install fishfyi
```

## Quick Start

```python
from fishfyi.api import FishFYI

with FishFYI() as api:
    results = api.search("salmon")
    print(results)
```

## License

MIT
