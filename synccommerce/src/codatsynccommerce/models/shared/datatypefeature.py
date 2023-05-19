"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import supportedfeature as shared_supportedfeature
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DataTypeFeatureDataType(str, Enum):
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
class DataTypeFeature:
    r"""Describes support for a given datatype and associated operations"""
    
    supported_features: list[shared_supportedfeature.SupportedFeature] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supportedFeatures') }})
    data_type: Optional[DataTypeFeatureDataType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Available Data types"""
    