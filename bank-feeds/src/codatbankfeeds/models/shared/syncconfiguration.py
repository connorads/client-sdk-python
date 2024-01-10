"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .syncasbankfeeds import SyncAsBankFeeds
from .syncasexpenses import SyncAsExpenses
from codatbankfeeds import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncConfiguration:
    sync_as_bank_feeds: Optional[SyncAsBankFeeds] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncAsBankFeeds'), 'exclude': lambda f: f is None }})
    sync_as_expenses: Optional[SyncAsExpenses] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncAsExpenses'), 'exclude': lambda f: f is None }})
    

