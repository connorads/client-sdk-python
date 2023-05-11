"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createcreditnoteresponse as shared_createcreditnoteresponse
from ..shared import creditnote as shared_creditnote
from typing import Optional


@dataclasses.dataclass
class CreateCreditNoteRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    credit_note: Optional[shared_creditnote.CreditNote] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CreateCreditNoteResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_credit_note_response: Optional[shared_createcreditnoteresponse.CreateCreditNoteResponse] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    