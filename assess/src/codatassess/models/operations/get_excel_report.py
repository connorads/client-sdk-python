"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import excelreporttype as shared_excelreporttype
from ..shared import schema as shared_schema
from typing import Optional



@dataclasses.dataclass
class GetExcelReportRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    report_type: shared_excelreporttype.ExcelReportType = dataclasses.field(metadata={'query_param': { 'field_name': 'reportType', 'style': 'form', 'explode': True }})
    r"""The type of report you want to generate and download."""
    




@dataclasses.dataclass
class GetExcelReport200ApplicationOctetStream:
    r"""OK"""
    




@dataclasses.dataclass
class GetExcelReportResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    

