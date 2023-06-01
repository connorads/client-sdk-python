"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import creditnote as shared_creditnote
from ..shared import schema as shared_schema
from ..shared import updatecreditnoteresponse as shared_updatecreditnoteresponse
from typing import Optional


@dataclasses.dataclass
class UpdateCreditNoteRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    credit_note_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'creditNoteId', 'style': 'simple', 'explode': False }})
    credit_note: Optional[shared_creditnote.CreditNote] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    force_update: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'forceUpdate', 'style': 'form', 'explode': True }})
    r"""When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check."""
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class UpdateCreditNoteResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    update_credit_note_response: Optional[shared_updatecreditnoteresponse.UpdateCreditNoteResponse] = dataclasses.field(default=None)
    r"""Success"""
    