"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class PutBankAccountSourceModifiedDateAccountTypeEnum(str, Enum):
    r"""The type of the account."""
    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBankAccountSourceModifiedDateMetadata:
    
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the record has been deleted in the third-party system this record originated from."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBankAccountSourceModifiedDate:
    r"""> **Accessing Bank Accounts through Banking API**
    > 
    > This datatype was originally used for accessing bank account data both in accounting integrations and open banking aggregators. 
    > 
    > To view bank account data through the Banking API, please refer to the new datatype [here](https://docs.codat.io/banking-api#/schemas/Account)
    
    > View the coverage for bank accounts in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A list of bank accounts associated with a company and a specific [data connection](https://api.codat.io/swagger/index.html#/Connection/get_companies__companyId__connections__connectionId_).
    
    Bank accounts data includes:
    * The name and ID of the account in the accounting platform.
    * The currency and balance of the account.
    * The sort code and account number.
    """
    
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountName'), 'exclude': lambda f: f is None }})
    r"""Name of the bank account in the accounting platform."""  
    account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountNumber'), 'exclude': lambda f: f is None }})
    r"""Account number for the bank account.
    
    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.
    
    FreeAgent integrations
    For Credit accounts, only the last four digits are required. For other types, the field is optional.
    """  
    account_type: Optional[PutBankAccountSourceModifiedDateAccountTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountType'), 'exclude': lambda f: f is None }})
    r"""The type of the account."""  
    available_balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('availableBalance'), 'exclude': lambda f: f is None }})
    r"""Total available balance of the bank account as reported by the underlying data source. This may take into account overdrafts or pending transactions for example."""  
    balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance'), 'exclude': lambda f: f is None }})
    r"""Balance of the bank account."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""Base currency of the bank account."""  
    i_ban: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iBan'), 'exclude': lambda f: f is None }})
    r"""International bank account number of the account. Often used when making or receiving international payments."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company in the accounting platform."""  
    institution: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution'), 'exclude': lambda f: f is None }})
    r"""The institution of the bank account."""  
    metadata: Optional[PutBankAccountSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nominalCode'), 'exclude': lambda f: f is None }})
    r"""Code used to identify each nominal account for a business."""  
    overdraft_limit: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('overdraftLimit'), 'exclude': lambda f: f is None }})
    r"""Pre-arranged overdraft limit of the account.
    
    The value is always positive. For example, an overdraftLimit of `1000` means that the balance of the account can go down to `-1000`.
    """  
    sort_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sortCode'), 'exclude': lambda f: f is None }})
    r"""Sort code for the bank account.
    
    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """  
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    

@dataclasses.dataclass
class PutBankAccountRequest:
    
    bank_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'bankAccountId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a bank account"""  
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    force_update: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'forceUpdate', 'style': 'form', 'explode': True }})  
    request_body: Optional[PutBankAccountSourceModifiedDate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBankAccount200ApplicationJSONChangesPushOperationRecordRef:
    
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})  
    
class PutBankAccount200ApplicationJSONChangesTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREATED = "Created"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    ATTACHMENT_UPLOADED = "AttachmentUploaded"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBankAccount200ApplicationJSONChanges:
    
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachmentId'), 'exclude': lambda f: f is None }})  
    record_ref: Optional[PutBankAccount200ApplicationJSONChangesPushOperationRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})  
    type: Optional[PutBankAccount200ApplicationJSONChangesTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})  
    
class PutBankAccount200ApplicationJSONSourceModifiedDateAccountTypeEnum(str, Enum):
    r"""The type of the account."""
    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBankAccount200ApplicationJSONSourceModifiedDateMetadata:
    
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the record has been deleted in the third-party system this record originated from."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBankAccount200ApplicationJSONSourceModifiedDate:
    r"""> **Accessing Bank Accounts through Banking API**
    > 
    > This datatype was originally used for accessing bank account data both in accounting integrations and open banking aggregators. 
    > 
    > To view bank account data through the Banking API, please refer to the new datatype [here](https://docs.codat.io/banking-api#/schemas/Account)
    
    > View the coverage for bank accounts in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A list of bank accounts associated with a company and a specific [data connection](https://api.codat.io/swagger/index.html#/Connection/get_companies__companyId__connections__connectionId_).
    
    Bank accounts data includes:
    * The name and ID of the account in the accounting platform.
    * The currency and balance of the account.
    * The sort code and account number.
    """
    
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountName'), 'exclude': lambda f: f is None }})
    r"""Name of the bank account in the accounting platform."""  
    account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountNumber'), 'exclude': lambda f: f is None }})
    r"""Account number for the bank account.
    
    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.
    
    FreeAgent integrations
    For Credit accounts, only the last four digits are required. For other types, the field is optional.
    """  
    account_type: Optional[PutBankAccount200ApplicationJSONSourceModifiedDateAccountTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountType'), 'exclude': lambda f: f is None }})
    r"""The type of the account."""  
    available_balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('availableBalance'), 'exclude': lambda f: f is None }})
    r"""Total available balance of the bank account as reported by the underlying data source. This may take into account overdrafts or pending transactions for example."""  
    balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance'), 'exclude': lambda f: f is None }})
    r"""Balance of the bank account."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""Base currency of the bank account."""  
    i_ban: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iBan'), 'exclude': lambda f: f is None }})
    r"""International bank account number of the account. Often used when making or receiving international payments."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company in the accounting platform."""  
    institution: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution'), 'exclude': lambda f: f is None }})
    r"""The institution of the bank account."""  
    metadata: Optional[PutBankAccount200ApplicationJSONSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nominalCode'), 'exclude': lambda f: f is None }})
    r"""Code used to identify each nominal account for a business."""  
    overdraft_limit: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('overdraftLimit'), 'exclude': lambda f: f is None }})
    r"""Pre-arranged overdraft limit of the account.
    
    The value is always positive. For example, an overdraftLimit of `1000` means that the balance of the account can go down to `-1000`.
    """  
    sort_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sortCode'), 'exclude': lambda f: f is None }})
    r"""Sort code for the bank account.
    
    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """  
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    
class PutBankAccount200ApplicationJSONStatusEnum(str, Enum):
    r"""The status of the push operation."""
    PENDING = "Pending"
    FAILED = "Failed"
    SUCCESS = "Success"
    TIMED_OUT = "TimedOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBankAccount200ApplicationJSONValidationValidationItem:
    
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemId'), 'exclude': lambda f: f is None }})  
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})  
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validatorName'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBankAccount200ApplicationJSONValidation:
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""
    
    errors: Optional[list[PutBankAccount200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})  
    warnings: Optional[list[PutBankAccount200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBankAccount200ApplicationJSON:
    r"""Success"""
    
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId') }})
    r"""Unique identifier for your SMB in Codat."""  
    data_connection_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataConnectionKey') }})
    r"""Unique identifier for a company's data connection."""  
    push_operation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pushOperationKey') }})
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""  
    requested_on_utc: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestedOnUtc') }})
    r"""The datetime when the push was requested."""  
    status: PutBankAccount200ApplicationJSONStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the push operation."""  
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})  
    changes: Optional[list[PutBankAccount200ApplicationJSONChanges]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changes'), 'exclude': lambda f: f is None }})  
    completed_on_utc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completedOnUtc'), 'exclude': lambda f: f is None }})
    r"""The datetime when the push was completed, null if Pending."""  
    data: Optional[PutBankAccount200ApplicationJSONSourceModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""> **Accessing Bank Accounts through Banking API**
    > 
    > This datatype was originally used for accessing bank account data both in accounting integrations and open banking aggregators. 
    > 
    > To view bank account data through the Banking API, please refer to the new datatype [here](https://docs.codat.io/banking-api#/schemas/Account)
    
    > View the coverage for bank accounts in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A list of bank accounts associated with a company and a specific [data connection](https://api.codat.io/swagger/index.html#/Connection/get_companies__companyId__connections__connectionId_).
    
    Bank accounts data includes:
    * The name and ID of the account in the accounting platform.
    * The currency and balance of the account.
    * The sort code and account number.
    """  
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""The type of data being pushed, eg invoices, customers."""  
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage'), 'exclude': lambda f: f is None }})  
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInMinutes'), 'exclude': lambda f: f is None }})  
    timeout_in_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInSeconds'), 'exclude': lambda f: f is None }})  
    validation: Optional[PutBankAccount200ApplicationJSONValidation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""  
    

@dataclasses.dataclass
class PutBankAccountResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    put_bank_account_200_application_json_object: Optional[PutBankAccount200ApplicationJSON] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    