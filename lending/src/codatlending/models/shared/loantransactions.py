"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .loantransactionsreportinfo import LoanTransactionsReportInfo
from .reportitems import ReportItems
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoanTransactions:
    errors: Optional[List[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    r"""If there are no errors, an empty array is returned."""
    report_info: Optional[LoanTransactionsReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportInfo'), 'exclude': lambda f: f is None }})
    report_items: Optional[List[ReportItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportItems'), 'exclude': lambda f: f is None }})
    r"""Contains object of reporting properties. The loan ref will reference a different object depending on the integration type."""
    

