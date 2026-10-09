# TV Show Summary

A Python program that retrieves real-world TV show records from a public API, aggregates the data, and writes the results to JSON.

This project builds on Lab 02 by introducing Object-Oriented Programming (OOP), including classes, inheritance, polymorphism, and an installable Python package.

## Data source

The program retrieves TV show records from the public TVMaze API:

https://api.tvmaze.com/shows?page=0

Each record represents a TV show and contains information such as the show's name, language, genres, and rating.

## Setup

This project requires Python 3.11, Conda, and an internet connection to access the TVMaze API.

### 1. Clone the repository

Clone the GitHub repository and navigate to the project directory:

```bash
git clone https://github.com/adityalochan/tvsummary-OOPS.git
cd tvsummary-OOPS
```

### 2. Create the Conda environment

Create the environment using the provided `environment.yml` file:

```bash
conda env create -f environment.yml
```

### 3. Activate the Conda environment

```bash
conda activate tvsummary
```

### 4. Install the dependencies

Install the pinned dependencies from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

### 5. Install the local Python package

Install the `tvsummary` package in editable mode:

```bash
python -m pip install -e .
```

### 6. Verify the package installation

Check that Python can import the installed package:

```bash
python -c "import tvsummary; print(tvsummary.__file__)"
```

The command should display the path to `src/tvsummary/__init__.py` without an import error.

## Run

Run the program from the project root directory:

```bash
python main.py
```

The program downloads TV show records from the TVMaze API, converts them into `TVShow` objects, calculates the aggregations, and writes the results to:

```text
data/processed/summary.json
```

The terminal displays the number of processed records and the location of the generated report.

## Test

Run the offline unit tests:

```bash
python -m unittest discover -s tests
```

The tests use manually created TV show records and do not require an internet connection.

They verify record cleaning and aggregation calculations, including total shows, genre counts, average ratings by language, and unique languages.

## Example output

The following is a shortened example from the previously generated `summary.json` containing 240 TV show records:

```json
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
  },
  "unique_languages": [
    "English",
    "Japanese"
  ]
}
```

The complete output includes all genres and languages present in the downloaded records.

Drama has the highest count with 154 shows, followed by Comedy with 66 shows.

The average rating is calculated separately for each language with valid ratings.

The `unique_languages` field contains a sorted list of languages without duplicates.

Actual results may change when the TVMaze API data changes.

## Data quirks

The previously submitted dataset contains 240 TV show records.

**Multiple genres:** A TV show can belong to more than one genre. The program loops through each show's genres and increases the count for every genre. Therefore, the sum of genre counts can be greater than the total number of shows.

**Missing genres:** Some shows may have an empty or missing genre list. The `TVShow` class converts missing or malformed genre values to an empty list. Shows without genres do not contribute to genre counts but are still included in the total show count.

**Missing ratings:** Some shows have no average rating. The `TVShow` class stores missing or invalid ratings as `None`. These shows are excluded from language-average calculations but remain included in the total show count.

**Missing languages:** The `TVShow` class replaces missing language values with `"Unknown"`. Records with unknown languages are excluded from language-average calculations and the unique-language list.

The missing-value counts should be calculated from the same dataset used to generate the submitted `summary.json`.

## Layout

```text
tvsummary-OOPS/
├── README.md
├── environment.yml
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── main.py
├── data/
│   └── .gitkeep
│   └── summary.json
├── src/
│   └── tvsummary/
│       ├── __init__.py
│       ├── config.py
│       ├── models.py
│       ├── sources.py
│       ├── aggregations.py
│       └── report.py
└── tests/
    └── test_models.py
```

**File responsibilities:**

- `main.py`: Connects the source, aggregation, and reporting components and prints progress messages.
- `config.py`: Stores the TVMaze API URL, request timeout, and output path.
- `models.py`: Defines the `TVShow` record class and handles missing or malformed values.
- `sources.py`: Defines `TVMazeSource`, which downloads records and returns `TVShow` objects.
- `aggregations.py`: Defines the `Aggregation` base class and subclasses for each calculation.
- `report.py`: Builds the summary using aggregation objects and writes the JSON report.
- `__init__.py`: Defines the Python package and its public interface.
- `tests/test_models.py`: Contains offline unit tests.
- `data/raw/`: Reserved for raw data.
- `data/processed/`: Contains the generated JSON summary.

## What moved where

The original Lab 02 functions were reorganized into classes and modules for Lab 03.

| Lab 02 function | Lab 03 location |
|---|---|
| `fetch_records()` | `TVMazeSource.fetch_records()` in `sources.py` |
| `total_shows()` | `TotalShows.calculate()` in `aggregations.py` |
| `shows_per_genre()` | `ShowsPerGenre.calculate()` in `aggregations.py` |
| `average_rating_language()` | `AverageRatingLanguage.calculate()` in `aggregations.py` |
| `unique_languages()` | `UniqueLanguages.calculate()` in `aggregations.py` |
| `build_summary()` | `build_summary()` in `report.py` |
| `write_summary()` | `write_summary()` in `report.py` |

Missing-value checks previously performed during aggregation are now handled in `TVShow.__init__()` in `models.py`.

## Design choices

**List:** The TVMaze API returns multiple TV show records as a list. The `TVMazeSource` class converts these records into a list of `TVShow` objects, allowing the program to process each show consistently.

**Dictionary:** Dictionaries store genre names as keys and their show counts as values. They are also used to group ratings by language and store the calculated averages.

**Set:** A set stores unique languages without duplicates, making it useful for identifying which languages appear in the dataset.

**Set comprehension:** The `UniqueLanguages` aggregation uses a set comprehension to collect valid language values. The result is sorted into a list before being written to JSON.

**Classes:** The `TVShow` class represents an individual show. Its `__init__()` method cleans missing and malformed values so that the aggregation classes can work with predictable attributes.

**Inheritance:** The `Aggregation` base class defines a shared structure for calculating summary statistics. `TotalShows`, `ShowsPerGenre`, `AverageRatingLanguage`, and `UniqueLanguages` inherit from this base class.

**Polymorphism:** Every aggregation subclass overrides the `calculate()` method. The summary builder loops through a list of aggregation objects and calls the same method on each object, allowing each subclass to perform its own calculation.

**Functions and methods:** Each calculation has a separate responsibility. The `calculate()` methods handle individual statistics, while `build_summary()` assembles the results and `write_summary()` saves the JSON file.

**Modules:** The project separates configuration, data retrieval, record modeling, aggregation, and report generation into different Python files to improve readability, testing, and maintenance.

**Extensibility:** Additional summary statistics can be introduced by creating a new subclass of `Aggregation` and adding its object to the list in `build_summary()`, without changing the existing aggregation classes.

## Known limitations

- Results may change when the data returned by TVMaze changes.
- The program requires an internet connection and depends on the TVMaze API being available.
- The program currently retrieves records from one API page rather than the entire TVMaze database.
- Shows with missing or invalid ratings are excluded from language-average calculations.
- Shows without a valid language are excluded from language averages and the unique-language list.
- If the API request fails, the program prints an error message and does not generate a new summary.