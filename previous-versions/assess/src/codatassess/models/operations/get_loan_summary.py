"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import loansummary as shared_loansummary
from enum import Enum
from typing import Optional

class GetLoanSummarySourceType(str, Enum):
    r"""Data source type."""
    BANKING = 'banking'
    COMMERCE = 'commerce'
    ACCOUNTING = 'accounting'


@dataclasses.dataclass
class GetLoanSummaryRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    source_type: GetLoanSummarySourceType = dataclasses.field(metadata={'query_param': { 'field_name': 'sourceType', 'style': 'form', 'explode': True }})
    r"""Data source type."""
    



@dataclasses.dataclass
class GetLoanSummaryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    loan_summary: Optional[shared_loansummary.LoanSummary] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

