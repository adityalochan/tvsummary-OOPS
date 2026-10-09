from tvsummary.config import SOURCE_URL, OUTPUT
from tvsummary.sources import fetch_records
from tvsummary.report import build_summary, write_summary

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