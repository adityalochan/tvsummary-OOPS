# Aggregating Records - TV Show Summary
Python program that retrieves real-world records from a public API, aggregates the data, and writes the results to JSON

## Data source
https://api.tvmaze.com/shows?page=0

Each record represents a TV show and contains information such as the show's name, language, genres, rating,

## Setup

This project requires Python 3.11 and uses the TVMaze API.

Clone the repository and open the project directory:
```bash
git clone https://github.com/adityalochan/tvsummary-OOPS.git
cd tvsummary-OOPS
```

Create and activate a Python virtual environment:

**macOS / Linux**
```bash
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
```

**Windows PowerShell**
```
.venv/bin/activate # Windows: .venv\Scripts\activate
```

Install the dependencies and local Python packages: 
```
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Run
Run the program from the project root directory:
```bash
python main.py
```

The program downloads TV show records, calculates the aggregations, and writes the results to summary.json.

Example output

The following is a shortened example from the current summary.json:

## Example output
{
  "url": "https://api.tvmaze.com/shows?page=0",
  "shows_per_genre": {
    "Drama": 154,
    "Comedy": 66,
    "Crime": 57,
    "Action": 55,
    "Thriller": 41
  },
  "total_shows": 240,
  "average_rating_language": {
    "English": 7.5806034482758635,
    "Japanese": 7.875
  }
}

The complete output includes all genres.

Drama has the highest count with 154 shows, followed by Comedy with 66 shows.

The average rating is calculated separately for each language with valid ratings.

## Data quirks
The dataset contains 240 TV show records in the submitted summary.

Multiple genres: A TV show can belong to more than one genre. The program loops through each show's genres and increases the count for every genre. Therefore, the sum of genre counts can be greater than the total number of shows.

Missing genres: Some shows may have an empty or missing genre list. Shows without genres do not contribute to genre counts but are still included in the total show count. Count to verify: [number of shows without genres].

Missing ratings: Some shows have no average rating. These shows are excluded from the language-average calculation to avoid invalid arithmetic, but they are still included in the total show count. Count to verify: [number of shows without valid ratings].

Missing languages: Records without a valid language are excluded from the language-average calculation. Count to verify: [number of shows without languages].

The missing-value counts must be calculated from the same dataset used to generate the submitted summary.json.


## Design choices
**List**: The API returns multiple TV show records as a list, allowing the program to process each record in a loop.

**Dictionary**: A dictionary stores genre names as keys and their show counts as values. Dictionaries are also used to group ratings by language and store the calculated averages.

**Set**: A set stores unique languages without duplicates, making it useful for checking which languages appear in the dataset.

**Set comprehension**: The unique_languages() function uses a set comprehension to extract valid language values from the records in a concise way.

**Functions**: Each aggregation has a separate responsibility. shows_per_genre() counts shows by genre, total_shows() counts records, and average_rating_language() calculates averages grouped by language.

**Modules**: The project separates configuration, data retrieval, aggregation, and report generation into different Python files to improve readability and maintenance.

## Known limitations
-Results may change when the data returned by TVMaze changes.

-The program requires an internet connection and depends on the TVMaze API being available.

-Shows with missing or invalid ratings are not included in language-average calculations.