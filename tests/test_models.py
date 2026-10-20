import pytest

from tvsummary.models import TVShow


def test_valid_record():
    """Check that valid show values are stored correctly."""
    record = {
        "name": "Example Show",
        "language": "English",
        "genres": ["Drama", "Comedy"],
        "rating": {"average": 8.5},
    }

    show = TVShow(record)

    assert show.name == "Example Show"
    assert show.language == "English"
    assert show.genres == ["Drama", "Comedy"]
    assert show.rating == 8.5


def test_missing_genres():
    """A missing genre list should become an empty list."""
    show = TVShow({"name": "Show A"})

    assert show.genres == []


def test_missing_rating():
    """A missing rating should become None."""
    show = TVShow({"name": "Show B"})

    assert show.rating is None


@pytest.mark.parametrize("genres", [None, "Drama", 123])
def test_malformed_genres(genres):
    """Invalid genre values should become an empty list."""
    show = TVShow({"genres": genres})

    assert show.genres == []


def test_missing_name_and_language():
    """Missing names and languages should use default values."""
    show = TVShow({})

    assert show.name == "Unknown"
    assert show.language == "Unknown"


def test_string_representation():
    """Check that a TV show has a readable description."""
    show = TVShow(
        {
            "name": "Example Show",
            "language": "English",
        }
    )

    assert str(show) == "Example Show (English)"
