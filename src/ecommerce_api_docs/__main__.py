#!/usr/bin/env python3
"""
Entry point for running the ecommerce-api-docs package as a module.
Usage: python -m ecommerce_api_docs or uv run python -m ecommerce_api_docs
"""

from .utils.cli import create_cli


def main():
    """Main entry point for the CLI application."""
    cli = create_cli()
    cli()


if __name__ == "__main__":
    main() 