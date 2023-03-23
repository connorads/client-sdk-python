"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ListBankingTransactionsRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    page: int = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""  
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""  
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""  
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""  
    
class ListBankingTransactions200ApplicationJSONSourceModifiedDateCodeEnum(str, Enum):
    r"""Code to identify the underlying transaction."""
    UNKNOWN = "Unknown"
    FEE = "Fee"
    PAYMENT = "Payment"
    CASH = "Cash"
    TRANSFER = "Transfer"
    INTEREST = "Interest"
    CASHBACK = "Cashback"
    CHEQUE = "Cheque"
    DIRECT_DEBIT = "DirectDebit"
    PURCHASE = "Purchase"
    STANDING_ORDER = "StandingOrder"
    ADJUSTMENT = "Adjustment"
    CREDIT = "Credit"
    OTHER = "Other"
    NOT_SUPPORTED = "NotSupported"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingTransactions200ApplicationJSONSourceModifiedDateTransactionCategoryRef:
    r"""An object of bank transaction category reference data."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique category reference id for the bank transaction."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The category name reference for the bank transaction."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingTransactions200ApplicationJSONSourceModifiedDate:
    r"""The Banking Transactions data type provides an immutable source of up-to-date information on income and expenditure.
    
    View the coverage for banking transactions in the [Data Coverage Explorer](https://knowledge.codat.io/supported-features/banking?view=tab-by-data-type&dataType=banking-transactions).
    """
    
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId') }})
    r"""The unique identifier of the bank account."""  
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""The currency of the bank transaction."""  
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique identifier of the bank transaction."""  
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""The amount of the bank transaction."""  
    authorized_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorizedDate'), 'exclude': lambda f: f is None }})
    r"""The date the bank transaction was authorized."""  
    code: Optional[ListBankingTransactions200ApplicationJSONSourceModifiedDateCodeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""Code to identify the underlying transaction."""  
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the bank transaction."""  
    merchant_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchantName'), 'exclude': lambda f: f is None }})
    r"""The name of the merchant."""  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    posted_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postedDate'), 'exclude': lambda f: f is None }})
    r"""The date the bank transaction was cleared."""  
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    transaction_category_ref: Optional[ListBankingTransactions200ApplicationJSONSourceModifiedDateTransactionCategoryRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactionCategoryRef'), 'exclude': lambda f: f is None }})
    r"""An object of bank transaction category reference data."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListBankingTransactions200ApplicationJSON:
    r"""Success"""
    
    results: Optional[ListBankingTransactions200ApplicationJSONSourceModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    r"""The Banking Transactions data type provides an immutable source of up-to-date information on income and expenditure.
    
    View the coverage for banking transactions in the [Data Coverage Explorer](https://knowledge.codat.io/supported-features/banking?view=tab-by-data-type&dataType=banking-transactions).
    """  
    

@dataclasses.dataclass
class ListBankingTransactionsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    list_banking_transactions_200_application_json_object: Optional[ListBankingTransactions200ApplicationJSON] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    