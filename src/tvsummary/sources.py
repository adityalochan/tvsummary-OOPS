"""Download and validate TV show records from TVMaze."""

import logging
from typing import Any

import requests

from tvsummary.config import TIMEOUT
from tvsummary.errors import DownloadError, MalformedResponseError
from tvsummary.models import TVShow

logger = logging.getLogger(__name__)


class TVMazeSource:
    """Download TV shows from the TVMaze API."""

    def __init__(self, url: str, timeout: float = TIMEOUT) -> None:
        self.url = url
        self.timeout = timeout

    def fetch_records(self) -> list[TVShow]:
        """Fetch TV shows and return cleaned TVShow objects."""
        logger.info("Downloading TV show records from %s", self.url)

        try:
            response = requests.get(self.url, timeout=self.timeout)
            response.raise_for_status()
        except requests.RequestException as error:
            logger.error("TVMaze download failed: %s", error)
            raise DownloadError("Could not download TV show records") from error

        try:
            records: Any = response.json()
        except ValueError as error:
            logger.error("TVMaze returned invalid JSON: %s", error)
            raise MalformedResponseError("TVMaze returned invalid JSON") from error

        if not isinstance(records, list):
            logger.error("TVMaze response is not a list")
            raise MalformedResponseError("TVMaze response must be a list")

        if not all(isinstance(record, dict) for record in records):
            logger.error("TVMaze response contains invalid show records")
            raise MalformedResponseError(
                "TVMaze response contains invalid show records"
            )

        logger.info("Downloaded %s TV show records", len(records))
        return [TVShow(record) for record in records]
