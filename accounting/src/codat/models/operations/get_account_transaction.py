"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accounttransaction as shared_accounttransaction
from typing import Optional


@dataclasses.dataclass
class GetAccountTransactionRequest:
    
    account_transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountTransactionId', 'style': 'simple', 'explode': False }})  
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class GetAccountTransactionResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    account_transaction: Optional[shared_accounttransaction.AccountTransaction] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    