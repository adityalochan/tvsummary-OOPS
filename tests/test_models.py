import unittest

from tvsummary.models import TVShow
from tvsummary.aggregations import (
    TotalShows,
    ShowsPerGenre,
    AverageRatingLanguage,
    UniqueLanguages,
)


class TestTVShow(unittest.TestCase):
    """Test TV show record cleaning."""

    def test_valid_record(self):
        record = {
            "name": "Example Show",
            "language": "English",
            "genres": ["Drama", "Comedy"],
            "rating": {"average": 8.5},
        }

        show = TVShow(record)

        self.assertEqual(show.name, "Example Show")
        self.assertEqual(show.language, "English")
        self.assertEqual(show.genres, ["Drama", "Comedy"])
        self.assertEqual(show.rating, 8.5)

    def test_missing_and_malformed_values(self):
        record = {
            "name": None,
            "language": None,
            "genres": "Drama",
            "rating": None,
        }

        show = TVShow(record)

        self.assertEqual(show.name, "Unknown")
        self.assertEqual(show.language, "Unknown")
        self.assertEqual(show.genres, [])
        self.assertIsNone(show.rating)


class TestAggregations(unittest.TestCase):
    """Test aggregations with offline sample records."""

    def setUp(self):
        self.records = [
            TVShow({
                "name": "Show A",
                "language": "English",
                "genres": ["Drama", "Comedy"],
                "rating": {"average": 8.0},
            }),
            TVShow({
                "name": "Show B",
                "language": "English",
                "genres": ["Drama"],
                "rating": {"average": 6.0},
            }),
            TVShow({
                "name": "Show C",
                "language": "Japanese",
                "genres": ["Action"],
                "rating": {"average": 9.0},
            }),
        ]

    def test_total_shows(self):
        self.assertEqual(TotalShows().calculate(self.records), 3)

    def test_shows_per_genre(self):
        self.assertEqual(
            ShowsPerGenre().calculate(self.records),
            {"Drama": 2, "Comedy": 1, "Action": 1},
        )

    def test_average_rating_language(self):
        self.assertEqual(
            AverageRatingLanguage().calculate(self.records),
            {"English": 7.0, "Japanese": 9.0},
        )

    def test_unique_languages(self):
        self.assertEqual(
            UniqueLanguages().calculate(self.records),
            ["English", "Japanese"],
        )


if __name__ == "__main__":
    unittest.main()