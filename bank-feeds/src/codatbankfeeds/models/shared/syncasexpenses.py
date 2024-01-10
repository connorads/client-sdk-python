"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .bankaccountoption import BankAccountOption
from .configurationcustomer import ConfigurationCustomer
from .configurationsupplier import ConfigurationSupplier
from codatbankfeeds import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncAsExpenses:
    bank_account_options: Optional[List[BankAccountOption]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankAccountOptions'), 'exclude': lambda f: f is None }})
    customer: Optional[ConfigurationCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer'), 'exclude': lambda f: f is None }})
    enable_sync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableSync'), 'exclude': lambda f: f is None }})
    r"""True if expense sync is enabled."""
    selected_bank_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedBankAccountId'), 'exclude': lambda f: f is None }})
    r"""The bank account ID being synced."""
    supplier: Optional[ConfigurationSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplier'), 'exclude': lambda f: f is None }})
    

