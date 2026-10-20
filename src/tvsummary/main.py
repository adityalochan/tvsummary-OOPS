"""Command-line entry point for tvsummary."""

import argparse
import logging
import random
import sys
from pathlib import Path

from tvsummary.errors import TVSummaryError
from tvsummary.logging_setup import configure_logging
from tvsummary.report import build_summary, write_summary
from tvsummary.run_info import write_run_info
from tvsummary.settings import load_settings
from tvsummary.sources import TVMazeSource

logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    """Run the program and return an exit code."""
    parser = argparse.ArgumentParser(description="Summarize TVMaze shows")
    parser.add_argument(
        "--config",
        default="config/tvsummary.toml",
        help="Path to the TOML settings file",
    )
    args = parser.parse_args(argv)

    try:
        settings = load_settings(Path(args.config))
        configure_logging(settings.log_level)

        source = TVMazeSource(settings.source_url, settings.timeout)
        records = source.fetch_records()

        if not records:
            raise TVSummaryError("No TV shows were downloaded")

        summary = build_summary(records, settings.source_url)

        rng = random.Random(settings.random_seed)
        sample_size = min(settings.sample_size, len(records))
        featured = rng.sample(records, sample_size)
        summary["featured_shows"] = [show.name for show in featured]

        output_path = settings.output_folder / "summary.json"
        write_summary(summary, output_path)
        write_run_info(settings, settings.output_folder)

        logger.info("Processed %s TV shows", len(records))
        return 0

    except TVSummaryError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
