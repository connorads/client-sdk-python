"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .integrationtype import IntegrationType
from .transactionstatus import TransactionStatus
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Transaction:
    integration_type: Optional[IntegrationType] = dataclasses.field(default=IntegrationType.EXPENSES, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrationType') }})
    r"""Type of transaction that has been processed e.g. Expense or Bank Feed."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""Metadata such as validation errors or the resulting record created in the accounting software."""
    status: Optional[TransactionStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Status of the transaction."""
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactionId') }})
    r"""Your unique idenfier of the transaction."""
    

