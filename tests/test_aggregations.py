from tvsummary.aggregations import (
    AverageRatingLanguage,
    ShowsPerGenre,
    TotalShows,
    UniqueLanguages,
)


def test_total_shows(sample_shows):
    assert TotalShows().calculate(sample_shows) == 3


def test_shows_per_genre(sample_shows):
    assert ShowsPerGenre().calculate(sample_shows) == {
        "Drama": 2,
        "Comedy": 1,
        "Action": 1,
    }


def test_average_rating_language(sample_shows):
    assert AverageRatingLanguage().calculate(sample_shows) == {
        "English": 7.0,
        "Japanese": 9.0,
    }


def test_unique_languages(sample_shows):
    assert UniqueLanguages().calculate(sample_shows) == [
        "English",
        "Japanese",
    ]
