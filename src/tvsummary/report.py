"""Create and save the TV show summary."""

import json
import logging
from pathlib import Path
from typing import Any

from tvsummary.aggregations import (
    AverageRatingLanguage,
    ShowsPerGenre,
    TotalShows,
    UniqueLanguages,
)
from tvsummary.models import TVShow

logger = logging.getLogger(__name__)


def build_summary(records: list[TVShow], source_url: str) -> dict[str, Any]:
    """Calculate the summary from the TV show records."""
    summary: dict[str, Any] = {"url": source_url}

    aggregations = [
        ShowsPerGenre(),
        TotalShows(),
        AverageRatingLanguage(),
        UniqueLanguages(),
    ]

    for aggregation in aggregations:
        summary[aggregation.name] = aggregation.calculate(records)

    logger.info("Summary created for %s shows", len(records))

    return summary


def write_summary(summary: dict[str, Any], path: Path) -> None:
    """Save the summary as a JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)

    logger.info("Summary saved to %s", path)
