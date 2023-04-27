"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import syncflowurl as shared_syncflowurl
from typing import Optional


@dataclasses.dataclass
class GetSyncFlowURLRequest:
    
    accounting_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountingKey', 'style': 'simple', 'explode': False }})

    r"""Accounting platform key"""
    commerce_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'commerceKey', 'style': 'simple', 'explode': False }})

    r"""Commerce platform key"""
    merchant_identifier: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'merchantIdentifier', 'style': 'form', 'explode': True }})

    r"""Identifier for your merchant, can be the merchant name or Codat company id."""
    

@dataclasses.dataclass
class GetSyncFlowURLResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    sync_flow_url: Optional[shared_syncflowurl.SyncFlowURL] = dataclasses.field(default=None)

    r"""Success"""
    