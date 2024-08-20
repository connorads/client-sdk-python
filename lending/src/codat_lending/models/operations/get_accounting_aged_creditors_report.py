"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from datetime import date
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetAccountingAgedCreditorsReportRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    number_of_periods: NotRequired[int]
    r"""Number of periods to include in the report."""
    period_length_days: NotRequired[int]
    r"""The length of period in days."""
    report_date: NotRequired[date]
    r"""Date the report is generated up to."""
    

class GetAccountingAgedCreditorsReportRequest(BaseModel):
    company_id: Annotated[str, pydantic.Field(alias="companyId"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Unique identifier for a company."""
    number_of_periods: Annotated[Optional[int], pydantic.Field(alias="numberOfPeriods"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Number of periods to include in the report."""
    period_length_days: Annotated[Optional[int], pydantic.Field(alias="periodLengthDays"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""The length of period in days."""
    report_date: Annotated[Optional[date], pydantic.Field(alias="reportDate"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Date the report is generated up to."""
    
