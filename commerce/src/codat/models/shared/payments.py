"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import links as shared_links
from ..shared import payment as shared_payment
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Payments:
    r"""OK"""
    
    links: shared_links.Links = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_links') }})  
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber') }})  
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize') }})  
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalResults') }})  
    results: Optional[list[shared_payment.Payment]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})  
    