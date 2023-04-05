"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createjournalentryresponse as shared_createjournalentryresponse
from ..shared import journalentry as shared_journalentry
from typing import Optional


@dataclasses.dataclass
class CreateJournalEntryRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    journal_entry: Optional[shared_journalentry.JournalEntry] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})  
    

@dataclasses.dataclass
class CreateJournalEntryResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    create_journal_entry_response: Optional[shared_createjournalentryresponse.CreateJournalEntryResponse] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    