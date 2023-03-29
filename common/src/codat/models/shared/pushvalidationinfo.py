"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import pushfieldvalidation as shared_pushfieldvalidation
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PushValidationInfo:
    
    information: Optional[list[shared_pushfieldvalidation.PushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information'), 'exclude': lambda f: f is None }})  
    warnings: Optional[list[shared_pushfieldvalidation.PushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})  
    