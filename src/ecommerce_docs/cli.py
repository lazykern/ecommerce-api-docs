"""Project CLI for scraping and generating docs (uv-friendly)."""

import click

from ecommerce_docs.platforms.lazada import guide_builder as lazada_guide_builder
from ecommerce_docs.platforms.lazada import scraper as lazada_scraper
from ecommerce_docs.platforms.shopee import guide_builder
from ecommerce_docs.platforms.shopee import scraper as shopee_scraper
from ecommerce_docs.platforms.tiktok import guide_builder as tiktok_guide_builder
from ecommerce_docs.platforms.tiktok import scraper as tiktok_scraper


@click.group()
def app() -> None:
    """Usage: ecomdocs {partner} [command] ..."""


# ---------------------------------------------------------------------------
# Shopee
# ---------------------------------------------------------------------------
@app.group()
def shopee() -> None:
    """Shopee commands."""
    return


@shopee.command("scrape")
@click.option("--workers", type=int, default=None, help="Override worker count.")
@click.option(
    "--output-dir",
    type=click.Path(file_okay=False, dir_okay=True),
    default=None,
    help="Where to store raw Shopee scrape output.",
)
def scrape_shopee(workers: int | None, output_dir: str | None) -> None:
    """Run the Shopee scraper (guides + APIs)."""
    shopee_scraper.main(workers=workers or shopee_scraper.MAX_WORKERS, output_dir=output_dir)


@shopee.command("build-guides")
@click.option(
    "--input-dir",
    type=click.Path(exists=True, file_okay=False),
    default=str(guide_builder.DEFAULT_INPUT_DIR),
    show_default=True,
)
@click.option(
    "--output-dir",
    type=click.Path(dir_okay=True, file_okay=False),
    default=str(guide_builder.DEFAULT_OUTPUT_DIR),
    show_default=True,
)
def generate_shopee_guides(input_dir: str, output_dir: str) -> None:
    """Normalize Shopee developer guides into Markdown + metadata."""
    guide_builder.main(input_dir=input_dir, output_dir=output_dir)


# ---------------------------------------------------------------------------
# Lazada
# ---------------------------------------------------------------------------
@app.group()
def lazada() -> None:
    """Lazada commands."""
    return


@lazada.command("scrape")
@click.option("--workers", type=int, default=None, help="Override worker count.")
@click.option(
    "--output-dir",
    type=click.Path(file_okay=False, dir_okay=True),
    default=None,
    help="Where to store raw Lazada scrape output.",
)
def scrape_lazada(workers: int | None, output_dir: str | None) -> None:
    """Run the Lazada scraper (guides + APIs)."""
    lazada_scraper.main(workers=workers or lazada_scraper.MAX_WORKERS, output_dir=output_dir)


@lazada.command("build-guides")
@click.option(
    "--input-dir",
    type=click.Path(exists=True, file_okay=False),
    default=str(lazada_guide_builder.DEFAULT_INPUT_DIR),
    show_default=True,
)
@click.option(
    "--output-dir",
    type=click.Path(dir_okay=True, file_okay=False),
    default=str(lazada_guide_builder.DEFAULT_OUTPUT_DIR),
    show_default=True,
)
def generate_lazada_guides(input_dir: str, output_dir: str) -> None:
    """Normalize Lazada developer guides into Markdown + metadata."""
    lazada_guide_builder.main(input_dir=input_dir, output_dir=output_dir)


# ---------------------------------------------------------------------------
# TikTok Shop
# ---------------------------------------------------------------------------
@app.group()
def tiktok() -> None:
    """TikTok Shop commands."""
    return


@tiktok.command("scrape")
@click.option("--workers", type=int, default=None, help="Override worker count.")
@click.option(
    "--output-dir",
    type=click.Path(file_okay=False, dir_okay=True),
    default=None,
    help="Where to store raw TikTok Shop scrape output.",
)
def scrape_tiktok(workers: int | None, output_dir: str | None) -> None:
    """Run the TikTok Shop scraper (docs + specs)."""
    tiktok_scraper.main(workers=workers or tiktok_scraper.MAX_WORKERS, output_dir=output_dir)


@tiktok.command("build-guides")
@click.option(
    "--input-dir",
    type=click.Path(exists=True, file_okay=False),
    default=str(tiktok_guide_builder.DEFAULT_INPUT_DIR),
    show_default=True,
)
@click.option(
    "--output-dir",
    type=click.Path(dir_okay=True, file_okay=False),
    default=str(tiktok_guide_builder.DEFAULT_OUTPUT_DIR),
    show_default=True,
)
def generate_tiktok_guides(input_dir: str, output_dir: str) -> None:
    """Normalize TikTok Shop guides into Markdown + metadata."""
    tiktok_guide_builder.main(input_dir=input_dir, output_dir=output_dir)


if __name__ == "__main__":
    app()
