from src.tvsummary.config import SOURCE_URL, OUTPUT
from src.tvsummary.sources import fetch_records
from src.tvsummary.report import build_summary, write_summary

def main():
    """Fetch TV shows and generate the summary."""
    records = fetch_records(SOURCE_URL)

    if not records:
        print("No records were downloaded")
        return

    summary = build_summary(records)
    write_summary(summary, OUTPUT)


if __name__ == "__main__":
    main()