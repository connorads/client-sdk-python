"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import banktransactions as shared_banktransactions
from ..shared import createbanktransactionsresponse as shared_createbanktransactionsresponse
from ..shared import schema as shared_schema
from typing import Optional


@dataclasses.dataclass
class CreateBankTransactionsRequest:
    
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an account"""
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    allow_sync_on_push_complete: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'allowSyncOnPushComplete', 'style': 'form', 'explode': True }})
    bank_transactions: Optional[shared_banktransactions.BankTransactions] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CreateBankTransactionsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_bank_transactions_response: Optional[shared_createbanktransactionsresponse.CreateBankTransactionsResponse] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    