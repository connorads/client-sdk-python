"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import visibleaccounts as shared_visibleaccounts
from typing import Optional


@dataclasses.dataclass
class GetVisibleAccountsRequest:
    
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    platform_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'platformKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetVisibleAccountsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    visible_accounts: Optional[shared_visibleaccounts.VisibleAccounts] = dataclasses.field(default=None)
    r"""Success"""
    