"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connection as shared_connection
from ..shared import errormessage as shared_errormessage
from codatcommon import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UnlinkConnectionRequestBody:
    
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UnlinkConnectionRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    request_body: Optional[UnlinkConnectionRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UnlinkConnectionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None)
    r"""OK"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your `query` parameter was not correctly formed"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    