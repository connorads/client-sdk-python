"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .loansummaryreportinfo import LoanSummaryReportInfo, LoanSummaryReportInfoTypedDict
from .loansummaryreportitem import LoanSummaryReportItem, LoanSummaryReportItemTypedDict
from codat_lending.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class LoanSummaryTypedDict(TypedDict):
    report_info: NotRequired[LoanSummaryReportInfoTypedDict]
    report_items: NotRequired[List[LoanSummaryReportItemTypedDict]]
    r"""Returns a summary of all loan activity for that integration type"""


class LoanSummary(BaseModel):
    report_info: Annotated[
        Optional[LoanSummaryReportInfo], pydantic.Field(alias="reportInfo")
    ] = None

    report_items: Annotated[
        Optional[List[LoanSummaryReportItem]], pydantic.Field(alias="reportItems")
    ] = None
    r"""Returns a summary of all loan activity for that integration type"""
