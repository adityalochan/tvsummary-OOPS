from tvsummary.config import SOURCE_URL, OUTPUT
from tvsummary.sources import TVMazeSource
from tvsummary.report import build_summary, write_summary

def main():
    """Fetch TV shows and generate the summary."""
    records = TVMazeSource(SOURCE_URL).fetch_records()

    if not records:
        print("No records were downloaded")
        return

    summary = build_summary(records)
    write_summary(summary, OUTPUT)

if __name__ == "__main__":
    main()