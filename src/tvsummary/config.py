from pathlib import Path

SOURCE_URL = "https://api.tvmaze.com/shows?page=0"
OUTPUT = Path("data/summary.json")
TIMEOUT = 10