"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatcommon import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SyncSettingDataType(str, Enum):
    r"""Available Data types"""
    ACCOUNT_TRANSACTIONS = 'accountTransactions'
    BALANCE_SHEET = 'balanceSheet'
    BANK_ACCOUNTS = 'bankAccounts'
    BANK_TRANSACTIONS = 'bankTransactions'
    BILL_CREDIT_NOTES = 'billCreditNotes'
    BILL_PAYMENTS = 'billPayments'
    BILLS = 'bills'
    CASH_FLOW_STATEMENT = 'cashFlowStatement'
    CHART_OF_ACCOUNTS = 'chartOfAccounts'
    COMPANY = 'company'
    CREDIT_NOTES = 'creditNotes'
    CUSTOMERS = 'customers'
    DIRECT_COSTS = 'directCosts'
    DIRECT_INCOMES = 'directIncomes'
    INVOICES = 'invoices'
    ITEMS = 'items'
    JOURNAL_ENTRIES = 'journalEntries'
    JOURNALS = 'journals'
    PAYMENT_METHODS = 'paymentMethods'
    PAYMENTS = 'payments'
    PROFIT_AND_LOSS = 'profitAndLoss'
    PURCHASE_ORDERS = 'purchaseOrders'
    SALES_ORDERS = 'salesOrders'
    SUPPLIERS = 'suppliers'
    TAX_RATES = 'taxRates'
    TRACKING_CATEGORIES = 'trackingCategories'
    TRANSFERS = 'transfers'
    BANKING_ACCOUNT_BALANCES = 'banking-accountBalances'
    BANKING_ACCOUNTS = 'banking-accounts'
    BANKING_TRANSACTION_CATEGORIES = 'banking-transactionCategories'
    BANKING_TRANSACTIONS = 'banking-transactions'
    COMMERCE_COMPANY_INFO = 'commerce-companyInfo'
    COMMERCE_CUSTOMERS = 'commerce-customers'
    COMMERCE_DISPUTES = 'commerce-disputes'
    COMMERCE_LOCATIONS = 'commerce-locations'
    COMMERCE_ORDERS = 'commerce-orders'
    COMMERCE_PAYMENT_METHODS = 'commerce-paymentMethods'
    COMMERCE_PAYMENTS = 'commerce-payments'
    COMMERCE_PRODUCT_CATEGORIES = 'commerce-productCategories'
    COMMERCE_PRODUCTS = 'commerce-products'
    COMMERCE_TAX_COMPONENTS = 'commerce-taxComponents'
    COMMERCE_TRANSACTIONS = 'commerce-transactions'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SyncSetting:
    r"""Describes how often, and how much history, should be fetched for the given data type when a pull operation is queued."""
    
    data_type: SyncSettingDataType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType') }})
    r"""Available Data types"""
    fetch_on_first_link: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fetchOnFirstLink') }})
    r"""Whether this data type should be queued after a company has authorized a connection."""
    sync_order: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncOrder') }})
    sync_schedule: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncSchedule') }})
    r"""Number of hours after which this data type should be refreshed."""
    is_locked: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isLocked'), 'exclude': lambda f: f is None }})
    months_to_sync: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('monthsToSync'), 'exclude': lambda f: f is None }})
    r"""Months of data to fetch, for report data types (`balanceSheet` & `profitAndLoss`) only."""
    sync_from_utc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncFromUtc'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:
    
    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```
    
    
    
    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:
    
    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`
    
    > Time zones
    > 
    > Not all dates from Codat will contain information about time zones.  
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """
    sync_from_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncFromWindow'), 'exclude': lambda f: f is None }})
    r"""Number of months of data to be fetched. Set this *or* `syncFromUTC`"""
    