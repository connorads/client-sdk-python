"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .option import Option
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FeesSupplier:
    selected_supplier_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedSupplierId') }})
    r"""Selected supplier id from the list of supplier records on the accounting software."""
    supplier_options: Optional[List[Option]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplierOptions') }})
    r"""List of supplier options from the list of supplier records on the accounting software."""
    

