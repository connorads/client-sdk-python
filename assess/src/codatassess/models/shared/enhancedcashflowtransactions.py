"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import datasource as shared_datasource
from ..shared import enhancedcashflowitem as shared_enhancedcashflowitem
from ..shared import reportinfo as shared_reportinfo
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class EnhancedCashFlowTransactions:
    r"""OK"""
    data_sources: Optional[list[shared_datasource.DataSource]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataSources'), 'exclude': lambda f: f is None }})
    report_info: Optional[shared_reportinfo.ReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportInfo'), 'exclude': lambda f: f is None }})
    r"""Report additional information, which is specific to Assess reports"""
    report_items: Optional[list[shared_enhancedcashflowitem.EnhancedCashFlowItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportItems'), 'exclude': lambda f: f is None }})
    

