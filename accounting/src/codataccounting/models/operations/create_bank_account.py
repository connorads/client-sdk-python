"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bankaccount as shared_bankaccount
from ..shared import createbankaccountresponse as shared_createbankaccountresponse
from ..shared import schema as shared_schema
from typing import Optional


@dataclasses.dataclass
class CreateBankAccountRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    allow_sync_on_push_complete: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'allowSyncOnPushComplete', 'style': 'form', 'explode': True }})
    bank_account: Optional[shared_bankaccount.BankAccount] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CreateBankAccountResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_bank_account_response: Optional[shared_createbankaccountresponse.CreateBankAccountResponse] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    