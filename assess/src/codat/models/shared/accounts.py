"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import sourceref as shared_sourceref
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Accounts:
    
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountName'), 'exclude': lambda f: f is None }})
    r"""The name of the account according to the provider."""  
    account_provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountProvider'), 'exclude': lambda f: f is None }})
    r"""The bank or other financial institution providing the account."""  
    account_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountType'), 'exclude': lambda f: f is None }})
    r"""The type of banking account, e.g. credit or debit."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.
    
    ## Unknown currencies
    
    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 
    
    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """  
    current_balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentBalance'), 'exclude': lambda f: f is None }})
    r"""The balance of the bank account."""  
    platform_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('platformName'), 'exclude': lambda f: f is None }})
    r"""Name of the banking data source, e.g. \\"Plaid\\"."""  
    source_ref: Optional[shared_sourceref.SourceRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceRef'), 'exclude': lambda f: f is None }})
    r"""A source reference containing the `sourceType` object \\"Banking\\"."""  
    