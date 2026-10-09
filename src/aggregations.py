
def shows_per_genre(records): 
    """Returns the number of shows belonging to each genre """
    counts = {}
    for record in records:
        genres = record["genres"]

        for genre in genres:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def total_shows(records):
    """Return the total number of TV show records."""
    return len(records)

def average_rating_language(records):
    """Return the average show rating for each language."""
    ratings = {}

    for record in records:
        language = record.get("language")
        rating = record.get("rating", {}).get("average")

        if not language or not isinstance(rating, (int, float)):
            continue

        if language not in ratings:
            ratings[language] = []

        ratings[language].append(rating)

    averages = {}

    for language, values in ratings.items():
        averages[language] = sum(values) / len(values)

    return averages

def unique_languages(records):
    """Return a set of unique languages in the TV show records."""
    return {
        record["language"]
        for record in records
        if record.get("language")
    }