"""Configure logging for the tvsummary application."""

import logging


def configure_logging(level: str) -> None:
    """Configure application logging once at the CLI entry point."""
    logging.basicConfig(
        level=level.upper(),
        format="%(levelname)s: %(message)s",
    )
