"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountcategorylevel as shared_accountcategorylevel
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EnhancedReportAccountCategory:
    
    levels: Optional[list[shared_accountcategorylevel.AccountCategoryLevel]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('levels'), 'exclude': lambda f: f is None }})  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Returns a status of \\"Suggested\\" or \\"Confirmed\\". If an account has a confirmed category, it will replace any suggested category returned."""  
    