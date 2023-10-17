"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import profitandlossreport1 as shared_profitandlossreport1
from typing import Optional


@dataclasses.dataclass
class GetProfitAndLossRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    r"""Number of months defining the period of interest."""
    periods_to_compare: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodsToCompare', 'style': 'form', 'explode': True }})
    r"""Number of periods with `periodLength` to compare."""
    start_month: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'startMonth', 'style': 'form', 'explode': True }})
    r"""The month the report starts from."""
    



@dataclasses.dataclass
class GetProfitAndLossResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    profit_and_loss_report: Optional[shared_profitandlossreport1.ProfitAndLossReport1] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

