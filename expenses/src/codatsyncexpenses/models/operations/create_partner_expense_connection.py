"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import dataconnection as shared_dataconnection
from ..shared import schema as shared_schema
from typing import Optional


@dataclasses.dataclass
class CreatePartnerExpenseConnectionRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreatePartnerExpenseConnectionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    data_connection: Optional[shared_dataconnection.DataConnection] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    