import requests

from tvsummary.config import TIMEOUT
from tvsummary import TVShow

class TVMazeSource:
    """Download TV shows from the TVMaze API."""

    def __init__(self, url):
        self.url = url

    def fetch_records(self):
        """Fetch TV shows and return a list of TVShow objects."""
        try:
            response = requests.get(self.url, timeout=TIMEOUT)
            response.raise_for_status()
            records = response.json()
            return [TVShow(record) for record in records]

        except (requests.RequestException, ValueError) as e:
            print(f"An error occurred while trying to fetch records: {e}")
            return []