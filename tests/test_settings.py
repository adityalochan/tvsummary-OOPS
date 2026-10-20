from pathlib import Path

import pytest

from tvsummary.errors import InvalidSettingsError
from tvsummary.settings import load_settings


def test_valid_settings(tmp_path: Path) -> None:
    config_file = tmp_path / "settings.toml"
    config_file.write_text(
        """
[app]
source_url = "https://example.com/shows"
timeout = 10.0
output_folder = "data/processed"
random_seed = 42
sample_size = 5
log_level = "INFO"
""",
        encoding="utf-8",
    )

    settings = load_settings(config_file)

    assert settings.source_url == "https://example.com/shows"
    assert settings.timeout == 10.0
    assert settings.random_seed == 42
    assert settings.sample_size == 5


def test_missing_settings_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.toml"

    with pytest.raises(InvalidSettingsError, match="Could not read settings file"):
        load_settings(missing_file)


def test_missing_required_setting(tmp_path: Path) -> None:
    config_file = tmp_path / "settings.toml"
    config_file.write_text(
        """
[app]
source_url = "https://example.com/shows"
""",
        encoding="utf-8",
    )

    with pytest.raises(InvalidSettingsError, match="missing required values"):
        load_settings(config_file)
