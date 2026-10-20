"""Offline tests for TVMazeSource."""

from unittest.mock import Mock

import pytest
import requests

from tvsummary.errors import DownloadError, MalformedResponseError
from tvsummary.sources import TVMazeSource


def test_download_failure(monkeypatch):
    """Network errors should become package-specific errors."""

    def fake_get(url, timeout):
        raise requests.ConnectionError("Network unavailable")

    monkeypatch.setattr("tvsummary.sources.requests.get", fake_get)

    with pytest.raises(DownloadError, match="Could not download"):
        TVMazeSource("https://example.com/shows", 10.0).fetch_records()


def test_invalid_json(monkeypatch):
    """Invalid JSON should raise MalformedResponseError."""
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.side_effect = ValueError("Invalid JSON")

    monkeypatch.setattr(
        "tvsummary.sources.requests.get",
        lambda url, timeout: response,
    )

    with pytest.raises(MalformedResponseError, match="invalid JSON"):
        TVMazeSource("https://example.com/shows", 10.0).fetch_records()

def test_invalid_response_structure(monkeypatch):
    """A JSON object is not a valid list of show records."""
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {"name": "Not a list"}

    monkeypatch.setattr(
        "tvsummary.sources.requests.get",
        lambda url, timeout: response,
    )

    with pytest.raises(MalformedResponseError, match="must be a list"):
        TVMazeSource("https://example.com/shows", 10.0).fetch_records()
