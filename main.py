from tvsummary import SOURCE_URL, OUTPUT
from tvsummary import TVMazeSource
from tvsummary import build_summary, write_summary


def main():
    """Connect the source, aggregations, and report."""
    print("Downloading TV show records...")

    records = TVMazeSource(SOURCE_URL).fetch_records()

    if not records:
        print("No records were downloaded. Summary not generated.")
        return

    summary = build_summary(records)
    write_summary(summary, OUTPUT)

    print(f"Processed {len(records)} TV shows.")
    print(f"Summary saved to {OUTPUT}")


if __name__ == "__main__":
    main()