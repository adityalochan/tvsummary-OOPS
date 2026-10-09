class TVShow:
    """Represent one TV show with cleaned data."""

    def __init__(self, record):
        self.name = record.get("name") or "Unknown"
        self.language = record.get("language") or "Unknown"

        genres = record.get("genres")
        self.genres = genres if isinstance(genres, list) else []

        rating = record.get("rating") or {}
        average = rating.get("average") if isinstance(rating, dict) else None
        self.rating = average if isinstance(average, (int, float)) else None

    def __str__(self):
        """Return a readable description of the TV show."""
        return f"{self.name} ({self.language})"