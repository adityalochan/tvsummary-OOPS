from sources import fetch_records
from report import build_summary, write_summary
from config import SOURCE_URL, OUTPUT

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