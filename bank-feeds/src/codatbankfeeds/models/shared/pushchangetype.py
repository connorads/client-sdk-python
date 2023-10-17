"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class PushChangeType(str, Enum):
    r"""Type of change being applied to record in third party platform."""
    UNKNOWN = 'Unknown'
    CREATED = 'Created'
    MODIFIED = 'Modified'
    DELETED = 'Deleted'
    ATTACHMENT_UPLOADED = 'AttachmentUploaded'
