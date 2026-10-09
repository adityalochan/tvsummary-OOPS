import json

from tvsummary import SOURCE_URL
from tvsummary import (
    TotalShows,
    ShowsPerGenre,
    AverageRatingLanguage,
    UniqueLanguages,
)

def build_summary(records):
    """Build a summary using aggregation objects."""
    summary = {"url": SOURCE_URL}

    aggregations = [
        ShowsPerGenre(),
        TotalShows(),
        AverageRatingLanguage(),
        UniqueLanguages(),
    ]

    for aggregation in aggregations:
        summary[aggregation.name] = aggregation.calculate(records)

    return summary


def write_summary(summary, path):
    """Write the summary to a JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2), encoding="utf-8")