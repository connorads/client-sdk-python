"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bill as shared_bill
from typing import Optional


@dataclasses.dataclass
class GetBillRequest:
    
    bill_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'billId', 'style': 'simple', 'explode': False }})

    r"""Unique identifier for a bill"""
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})

    

@dataclasses.dataclass
class GetBillResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    bill: Optional[shared_bill.Bill] = dataclasses.field(default=None)

    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    