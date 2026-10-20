"""Aggregation classes for TV show summaries."""

from typing import Any

from tvsummary.models import TVShow


class Aggregation:
    """Base class for TV show aggregations."""

    def __init__(self, name: str) -> None:
        self.name = name

    def calculate(self, records: list[TVShow]) -> Any:
        """Calculate a summary value."""
        raise NotImplementedError("Subclasses must implement calculate().")


class TotalShows(Aggregation):
    """Count the total number of TV shows."""

    def __init__(self) -> None:
        super().__init__("total_shows")

    def calculate(self, records: list[TVShow]) -> int:
        return len(records)


class ShowsPerGenre(Aggregation):
    """Count how many TV shows belong to each genre."""

    def __init__(self) -> None:
        super().__init__("shows_per_genre")

    def calculate(self, records: list[TVShow]) -> dict[str, int]:
        counts: dict[str, int] = {}

        for show in records:
            for genre in show.genres:
                counts[genre] = counts.get(genre, 0) + 1

        return counts


class AverageRatingLanguage(Aggregation):
    """Calculate the average rating for each language."""

    def __init__(self) -> None:
        super().__init__("average_rating_language")

    def calculate(self, records: list[TVShow]) -> dict[str, float]:
        totals: dict[str, float] = {}
        counts: dict[str, int] = {}

        for show in records:
            if show.language == "Unknown" or show.rating is None:
                continue

            language = show.language
            totals[language] = totals.get(language, 0) + show.rating
            counts[language] = counts.get(language, 0) + 1

        return {language: totals[language] / counts[language] for language in totals}


class UniqueLanguages(Aggregation):
    """Collect the unique languages in the TV show records."""

    def __init__(self) -> None:
        super().__init__("unique_languages")

    def calculate(self, records: list[TVShow]) -> list[str]:
        return sorted({show.language for show in records if show.language != "Unknown"})
