"""Load and validate application settings from TOML."""

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from tvsummary.errors import InvalidSettingsError


@dataclass(frozen=True)
class Settings:
    """Validated settings for a tvsummary run."""

    source_url: str
    timeout: float
    output_folder: Path
    random_seed: int
    sample_size: int
    log_level: str


def load_settings(path: Path) -> Settings:
    """Read a TOML file and return validated settings."""
    try:
        with path.open("rb") as file:
            document = tomllib.load(file)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise InvalidSettingsError(f"Could not read settings file: {path}") from error

    try:
        app: Any = document["app"]

        source_url = app["source_url"]
        timeout = app["timeout"]
        output_folder = app["output_folder"]
        random_seed = app["random_seed"]
        sample_size = app["sample_size"]
        log_level = app["log_level"]
    except (KeyError, TypeError) as error:
        raise InvalidSettingsError(
            "Settings file is missing required values"
        ) from error

    if not isinstance(source_url, str) or not source_url.strip():
        raise InvalidSettingsError("source_url must be a non-empty string")

    if (
        isinstance(timeout, bool)
        or not isinstance(timeout, (int, float))
        or timeout <= 0
    ):
        raise InvalidSettingsError("timeout must be a positive number")

    if not isinstance(output_folder, str) or not output_folder.strip():
        raise InvalidSettingsError("output_folder must be a non-empty string")

    if isinstance(random_seed, bool) or not isinstance(random_seed, int):
        raise InvalidSettingsError("random_seed must be an integer")

    if (
        isinstance(sample_size, bool)
        or not isinstance(sample_size, int)
        or sample_size < 0
    ):
        raise InvalidSettingsError("sample_size must be a non-negative integer")

    if not isinstance(log_level, str) or log_level.upper() not in {
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    }:
        raise InvalidSettingsError("log_level must be a valid logging level")

    return Settings(
        source_url=source_url,
        timeout=float(timeout),
        output_folder=Path(output_folder),
        random_seed=random_seed,
        sample_size=sample_size,
        log_level=log_level.upper(),
    )
