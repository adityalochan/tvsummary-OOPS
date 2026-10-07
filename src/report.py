class Report:
      
    def build_summary(records):
        """Combine the aggregations into one dict ready to write."""
        summary = {}
        summary["url"] = SOURCE_URL
        summary["shows_per_genre"] = shows_per_genre(records)
        summary["total_shows"] = total_shows(records)
        summary["average_rating_language"] = average_rating_language(records)
        return summary


    def write_summary(summary,path):
        """Write the summary to a JSON file."""
        path.write_text(json.dumps(summary, indent=2), encoding="utf-8")