from tvsummary.models import TVShow
from tvsummary.sources import TVMazeSource
from tvsummary.aggregations import (
    Aggregation,
    TotalShows,
    ShowsPerGenre,
    AverageRatingLanguage,
    UniqueLanguages,
)
from tvsummary.report import build_summary, write_summary