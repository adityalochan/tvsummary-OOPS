import requests
from tvsummary.config import TIMEOUT
        
def fetch_records(url):
    """Download the records and return them as Python objects."""
    try: 
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred while trying to fetch records: {e}")
        return []