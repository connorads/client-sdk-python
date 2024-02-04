"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class InvoiceToDataType(str, Enum):
    r"""The type of contact."""
    CUSTOMERS = 'customers'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceTo:
    r"""Unique identifier of the customer the expense is billable to. The invoiceTo object is currently only supported for QBO."""
    data_type: Optional[InvoiceToDataType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""The type of contact."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""identifier of customer."""
    

