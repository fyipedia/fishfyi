"""Command-line interface for fishfyi."""

from __future__ import annotations

import json

import typer

from fishfyi.api import FishFYI

app = typer.Typer(help="FishFYI — Fish species and marine biology API client.")


@app.command()
def search(query: str) -> None:
    """Search fishfyi.com."""
    with FishFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))
