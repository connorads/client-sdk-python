"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createdirectincomeresponse as shared_createdirectincomeresponse
from ..shared import directincome as shared_directincome
from ..shared import errormessage as shared_errormessage
from typing import Optional


@dataclasses.dataclass
class CreateDirectIncomeRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    direct_income: Optional[shared_directincome.DirectIncome] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    r"""Time limit for the push operation to complete before it is timed out."""
    



@dataclasses.dataclass
class CreateDirectIncomeResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_direct_income_response: Optional[shared_createdirectincomeresponse.CreateDirectIncomeResponse] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

