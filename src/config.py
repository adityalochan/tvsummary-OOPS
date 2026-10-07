from pathlib import Path

class Config:

    SOURCE_URL = "https://api.tvmaze.com/shows?page=0"
    OUTPUT = Path("summary.json")