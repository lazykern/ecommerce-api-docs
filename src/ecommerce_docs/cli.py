"""Project CLI for scraping and generating docs (uv-friendly)."""

import click

from ecommerce_docs.platforms.lazada import guide_builder as lazada_guide_builder
from ecommerce_docs.platforms.lazada import openapi_builder as lazada_openapi_builder
from ecommerce_docs.platforms.lazada import scraper as lazada_scraper
from ecommerce_docs.platforms.shopee import guide_builder
from ecommerce_docs.platforms.shopee import openapi_builder
from ecommerce_docs.platforms.shopee import scraper as shopee_scraper
from ecommerce_docs.platforms.tiktok import guide_builder as tiktok_guide_builder
from ecommerce_docs.platforms.tiktok import scraper as tiktok_scraper


@click.group()
def app() -> None:
    """Scrape and generate API docs."""
    # No-op; subcommands implement functionality.
    return


@app.group()
def scrape() -> None:
    """Scrape raw docs for a platform."""
    return


@app.group()
def build() -> None:
    """Build processed artifacts (OpenAPI, guides)."""
    return


@scrape.command("shopee")
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


@scrape.command("lazada")
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


@scrape.command("tiktok")
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


@build.command("shopee-openapi")
@click.option(
    "--apis-dir",
    type=click.Path(exists=True, file_okay=False),
    default=str(openapi_builder.DEFAULT_APIS_DIR),
    show_default=True,
)
@click.option(
    "--output-file",
    type=click.Path(dir_okay=False),
    default=str(openapi_builder.DEFAULT_OUTPUT_FILE),
    show_default=True,
)
def generate_shopee_openapi(apis_dir: str, output_file: str) -> None:
    """Generate the Shopee OpenAPI spec from scraped JSON."""
    openapi_builder.main(apis_dir=apis_dir, output_file=output_file)


@build.command("shopee-guides")
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


@build.command("lazada-openapi")
@click.option(
    "--apis-dir",
    type=click.Path(exists=True, file_okay=False),
    default=str(lazada_openapi_builder.DEFAULT_APIS_DIR),
    show_default=True,
)
@click.option(
    "--output-file",
    type=click.Path(dir_okay=False),
    default=str(lazada_openapi_builder.DEFAULT_OUTPUT_FILE),
    show_default=True,
)
def generate_lazada_openapi(apis_dir: str, output_file: str) -> None:
    """Generate the Lazada OpenAPI spec from scraped JSON."""
    lazada_openapi_builder.main(apis_dir=apis_dir, output_file=output_file)


@build.command("lazada-guides")
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


@build.command("tiktok-guides")
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
