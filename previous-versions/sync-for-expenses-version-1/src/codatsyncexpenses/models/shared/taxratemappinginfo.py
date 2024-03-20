"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from enum import Enum
from typing import List, Optional

class TaxRateMappingInfoValidTransactionTypes(str, Enum):
    PAYMENT = 'Payment'
    REFUND = 'Refund'
    REWARD = 'Reward'
    CHARGEBACK = 'Chargeback'
    TRANSFER_IN = 'TransferIn'
    TRANSFER_OUT = 'TransferOut'
    ADJUSTMENT_IN = 'AdjustmentIn'
    ADJUSTMENT_OUT = 'AdjustmentOut'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxRateMappingInfo:
    UNSET='__SPEAKEASY_UNSET__'
    code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is TaxRateMappingInfo.UNSET }})
    r"""Code for the tax rate from the accounting platform."""
    effective_tax_rate: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('effectiveTaxRate'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Effective tax rate."""
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is TaxRateMappingInfo.UNSET }})
    r"""Unique identifier of tax rate."""
    name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is TaxRateMappingInfo.UNSET }})
    r"""Name of the tax rate in the accounting platform."""
    total_tax_rate: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalTaxRate'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Total (not compounded) sum of the components of a tax rate."""
    valid_transaction_types: Optional[List[TaxRateMappingInfoValidTransactionTypes]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validTransactionTypes'), 'exclude': lambda f: f is TaxRateMappingInfo.UNSET }})
    r"""Supported transaction types for the account."""
    

