"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class DataConnectionStatusEnum(str, Enum):
    r"""The current authorization status of the data connection."""
    PENDING_AUTH = 'PendingAuth'
    LINKED = 'Linked'
    UNLINKED = 'Unlinked'
    DEAUTHORIZED = 'Deauthorized'
