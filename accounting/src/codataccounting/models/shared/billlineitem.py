"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountref as shared_accountref
from ..shared import itemref as shared_itemref
from ..shared import propertiestracking as shared_propertiestracking
from ..shared import taxrateref as shared_taxrateref
from ..shared import trackingcategoryref as shared_trackingcategoryref
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BillLineItem:
    
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})

    r"""Number of units of goods or services received."""
    unit_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitAmount') }})

    r"""Price of each unit of goods or services."""
    account_ref: Optional[shared_accountref.AccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})

    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})

    r"""Friendly name of the goods or services received."""
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAmount'), 'exclude': lambda f: f is None }})

    r"""Numerical value of any discounts applied.
    
    Do not use to apply discounts in Oracle NetSuite—see Oracle NetSuite integration reference.
    """
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'exclude': lambda f: f is None }})

    is_direct_cost: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDirectCost'), 'exclude': lambda f: f is None }})

    item_ref: Optional[shared_itemref.ItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemRef'), 'exclude': lambda f: f is None }})

    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'exclude': lambda f: f is None }})

    r"""Amount of the line, inclusive of discounts but exclusive of tax."""
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'exclude': lambda f: f is None }})

    r"""Amount of tax for the line."""
    tax_rate_ref: Optional[shared_taxrateref.TaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateRef'), 'exclude': lambda f: f is None }})

    r"""Data types that reference a tax rate, for example invoice and bill line items, use a taxRateRef that includes the ID and name of the linked tax rate.
    
    Found on:
    
    - Bill line items
    - Bill Credit Note line items
    - Credit Note line items
    - Direct incomes line items
    - Invoice line items
    - Items
    """
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})

    r"""Total amount of the line, including tax."""
    tracking: Optional[shared_propertiestracking.Propertiestracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})

    r"""Categories, and a project and customer, against which the item is tracked."""
    tracking_category_refs: Optional[list[shared_trackingcategoryref.TrackingCategoryRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})

    r"""Collection of categories against which this item is tracked."""
    