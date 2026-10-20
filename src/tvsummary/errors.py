"""Custom exceptions used by the tvsummary package."""


class TVSummaryError(Exception):
    """Base exception for expected package failures."""


class DownloadError(TVSummaryError):
    """Raised when TV show records cannot be downloaded."""


class MalformedResponseError(TVSummaryError):
    """Raised when the API response contains invalid data."""


class InvalidSettingsError(TVSummaryError):
    """Raised when the application settings are invalid."""
