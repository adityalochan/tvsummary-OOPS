import json
from pathlib import Path
from sources import fetch_records
from aggregations import shows_per_genre, total_shows, average_rating_language

class Models:





    def main():
        records = fetch_records(SOURCE_URL)

        if not records:
            print("No records were downloaded")
            return
        summary = build_summary(records)
        write_summary(summary, OUTPUT)

    if __name__ == "__main__":
        main()