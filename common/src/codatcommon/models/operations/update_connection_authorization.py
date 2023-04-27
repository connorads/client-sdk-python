"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connection as shared_connection
from typing import Optional


@dataclasses.dataclass
class UpdateConnectionAuthorizationRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})

    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})

    request_body: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})

    

@dataclasses.dataclass
class UpdateConnectionAuthorizationResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None)

    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    