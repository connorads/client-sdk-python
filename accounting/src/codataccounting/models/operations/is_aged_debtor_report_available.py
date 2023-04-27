"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class IsAgedDebtorReportAvailableRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})

    

@dataclasses.dataclass
class IsAgedDebtorReportAvailableResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    is_aged_debtor_report_available_200_application_json_boolean: Optional[bool] = dataclasses.field(default=None)

    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    