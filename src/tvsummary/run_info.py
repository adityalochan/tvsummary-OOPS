"""Save information about how the program was run."""

import json
import platform
from dataclasses import asdict
from importlib.metadata import version
from pathlib import Path

from tvsummary.settings import Settings


def write_run_info(settings: Settings, output_folder: Path) -> None:
    """Save settings and software versions to a JSON file."""
    settings_data = asdict(settings)
    settings_data["output_folder"] = str(settings.output_folder)

    info = {
        "settings": settings_data,
        "python_version": platform.python_version(),
        "pytest_version": version("pytest"),
        "mypy_version": version("mypy"),
        "ruff_version": version("ruff"),
    }

    output_folder.mkdir(parents=True, exist_ok=True)
    output_path = output_folder / "run_info.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(info, file, indent=2)
