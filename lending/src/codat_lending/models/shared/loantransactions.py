"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .loantransactionsreportinfo import LoanTransactionsReportInfo, LoanTransactionsReportInfoTypedDict
from .reportitems import ReportItems, ReportItemsTypedDict
from codat_lending.types import BaseModel
import pydantic
from typing import Any, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class LoanTransactionsTypedDict(TypedDict):
    errors: NotRequired[List[Any]]
    r"""If there are no errors, an empty array is returned."""
    report_info: NotRequired[LoanTransactionsReportInfoTypedDict]
    report_items: NotRequired[List[ReportItemsTypedDict]]
    r"""Contains object of reporting properties. The loan ref will reference a different object depending on the integration type."""
    

class LoanTransactions(BaseModel):
    errors: Optional[List[Any]] = None
    r"""If there are no errors, an empty array is returned."""
    report_info: Annotated[Optional[LoanTransactionsReportInfo], pydantic.Field(alias="reportInfo")] = None
    report_items: Annotated[Optional[List[ReportItems]], pydantic.Field(alias="reportItems")] = None
    r"""Contains object of reporting properties. The loan ref will reference a different object depending on the integration type."""
    
