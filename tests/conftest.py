import pytest

from tvsummary.models import TVShow


@pytest.fixture
def sample_shows():
    """Provide sample TV shows for aggregation tests."""
    return [
        TVShow(
            {
                "name": "Show A",
                "language": "English",
                "genres": ["Drama", "Comedy"],
                "rating": {"average": 8.0},
            }
        ),
        TVShow(
            {
                "name": "Show B",
                "language": "English",
                "genres": ["Drama"],
                "rating": {"average": 6.0},
            }
        ),
        TVShow(
            {
                "name": "Show C",
                "language": "Japanese",
                "genres": ["Action"],
                "rating": {"average": 9.0},
            }
        ),
    ]
