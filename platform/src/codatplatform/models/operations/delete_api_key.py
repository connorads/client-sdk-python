"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class DeleteAPIKeyRequest:
    api_key_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiKeyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for api key."""
    




@dataclasses.dataclass
class DeleteAPIKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

