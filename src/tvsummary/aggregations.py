
def shows_per_genre(records): 
    """Returns the number of shows belonging to each genre """
    counts = {}
    for record in records:
        genres = record["genres"]

        for genre in genres:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def total_shows(records):
    return len(records)

def average_rating_language(records):
    """Returns the overall average rating of shows."""
    total , count = 0, 0
    
    for record in records:
        rating = record["rating"]["average"]

        if rating is not None:
            count += 1
            total += rating
    return total / count  