"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentIDRequest:
    
    bill_payment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'billPaymentId', 'style': 'simple', 'explode': False }})  
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONChangesPushOperationReferenceDataTypeEnum(str, Enum):
    r"""Available Data types"""
    ACCOUNT_TRANSACTIONS = "accountTransactions"
    BALANCE_SHEET = "balanceSheet"
    BANK_ACCOUNTS = "bankAccounts"
    BANK_TRANSACTIONS = "bankTransactions"
    BILL_CREDIT_NOTES = "billCreditNotes"
    BILL_PAYMENTS = "billPayments"
    BILLS = "bills"
    CASH_FLOW_STATEMENT = "cashFlowStatement"
    CHART_OF_ACCOUNTS = "chartOfAccounts"
    COMPANY = "company"
    CREDIT_NOTES = "creditNotes"
    CUSTOMERS = "customers"
    DIRECT_COSTS = "directCosts"
    DIRECT_INCOMES = "directIncomes"
    INVOICES = "invoices"
    ITEMS = "items"
    JOURNAL_ENTRIES = "journalEntries"
    JOURNALS = "journals"
    PAYMENT_METHODS = "paymentMethods"
    PAYMENTS = "payments"
    PROFIT_AND_LOSS = "profitAndLoss"
    PURCHASE_ORDERS = "purchaseOrders"
    SALES_ORDERS = "salesOrders"
    SUPPLIERS = "suppliers"
    TAX_RATES = "taxRates"
    TRACKING_CATEGORIES = "trackingCategories"
    TRANSFERS = "transfers"
    BANKING_ACCOUNT_BALANCES = "banking-accountBalances"
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTION_CATEGORIES = "banking-transactionCategories"
    BANKING_TRANSACTIONS = "banking-transactions"
    COMMERCE_COMPANY_INFO = "commerce-companyInfo"
    COMMERCE_CUSTOMERS = "commerce-customers"
    COMMERCE_DISPUTES = "commerce-disputes"
    COMMERCE_LOCATIONS = "commerce-locations"
    COMMERCE_ORDERS = "commerce-orders"
    COMMERCE_PAYMENT_METHODS = "commerce-paymentMethods"
    COMMERCE_PAYMENTS = "commerce-payments"
    COMMERCE_PRODUCT_CATEGORIES = "commerce-productCategories"
    COMMERCE_PRODUCTS = "commerce-products"
    COMMERCE_TAX_COMPONENTS = "commerce-taxComponents"
    COMMERCE_TRANSACTIONS = "commerce-transactions"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONChangesPushOperationReference:
    
    data_type: Optional[DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONChangesPushOperationReferenceDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Available Data types"""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})  
    
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONChangesPushChangeTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREATED = "Created"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    ATTACHMENT_UPLOADED = "AttachmentUploaded"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONChanges:
    
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachmentId'), 'exclude': lambda f: f is None }})  
    record_ref: Optional[DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONChangesPushOperationReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})  
    type: Optional[DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONChangesPushChangeTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})  
    
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONDataTypeEnum(str, Enum):
    r"""The type of data being pushed, eg invoices, customers."""
    ACCOUNT_TRANSACTIONS = "accountTransactions"
    BALANCE_SHEET = "balanceSheet"
    BANK_ACCOUNTS = "bankAccounts"
    BANK_TRANSACTIONS = "bankTransactions"
    BILL_CREDIT_NOTES = "billCreditNotes"
    BILL_PAYMENTS = "billPayments"
    BILLS = "bills"
    CASH_FLOW_STATEMENT = "cashFlowStatement"
    CHART_OF_ACCOUNTS = "chartOfAccounts"
    COMPANY = "company"
    CREDIT_NOTES = "creditNotes"
    CUSTOMERS = "customers"
    DIRECT_COSTS = "directCosts"
    DIRECT_INCOMES = "directIncomes"
    INVOICES = "invoices"
    ITEMS = "items"
    JOURNAL_ENTRIES = "journalEntries"
    JOURNALS = "journals"
    PAYMENT_METHODS = "paymentMethods"
    PAYMENTS = "payments"
    PROFIT_AND_LOSS = "profitAndLoss"
    PURCHASE_ORDERS = "purchaseOrders"
    SALES_ORDERS = "salesOrders"
    SUPPLIERS = "suppliers"
    TAX_RATES = "taxRates"
    TRACKING_CATEGORIES = "trackingCategories"
    TRANSFERS = "transfers"
    BANKING_ACCOUNT_BALANCES = "banking-accountBalances"
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTION_CATEGORIES = "banking-transactionCategories"
    BANKING_TRANSACTIONS = "banking-transactions"
    COMMERCE_COMPANY_INFO = "commerce-companyInfo"
    COMMERCE_CUSTOMERS = "commerce-customers"
    COMMERCE_DISPUTES = "commerce-disputes"
    COMMERCE_LOCATIONS = "commerce-locations"
    COMMERCE_ORDERS = "commerce-orders"
    COMMERCE_PAYMENT_METHODS = "commerce-paymentMethods"
    COMMERCE_PAYMENTS = "commerce-payments"
    COMMERCE_PRODUCT_CATEGORIES = "commerce-productCategories"
    COMMERCE_PRODUCTS = "commerce-products"
    COMMERCE_TAX_COMPONENTS = "commerce-taxComponents"
    COMMERCE_TRANSACTIONS = "commerce-transactions"

class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONPushOperationStatusEnum(str, Enum):
    r"""The status of the push operation."""
    PENDING = "Pending"
    FAILED = "Failed"
    SUCCESS = "Success"
    TIMED_OUT = "TimedOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONValidationValidationItem:
    
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemId'), 'exclude': lambda f: f is None }})  
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})  
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validatorName'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONValidation:
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""
    
    errors: Optional[list[DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})  
    warnings: Optional[list[DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSON:
    r"""OK"""
    
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId') }})
    r"""Unique identifier for your SMB in Codat."""  
    data_connection_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataConnectionKey') }})
    r"""Unique identifier for a company's data connection."""  
    push_operation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pushOperationKey') }})
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""  
    requested_on_utc: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestedOnUtc') }})
    r"""The datetime when the push was requested."""  
    status: DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONPushOperationStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the push operation."""  
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})  
    changes: Optional[list[DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONChanges]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changes'), 'exclude': lambda f: f is None }})  
    completed_on_utc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completedOnUtc'), 'exclude': lambda f: f is None }})
    r"""The datetime when the push was completed, null if Pending."""  
    data_type: Optional[DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""The type of data being pushed, eg invoices, customers."""  
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage'), 'exclude': lambda f: f is None }})  
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInMinutes'), 'exclude': lambda f: f is None }})  
    timeout_in_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInSeconds'), 'exclude': lambda f: f is None }})  
    validation: Optional[DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSONValidation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""  
    

@dataclasses.dataclass
class DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentIDResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    delete_companies_company_id_connections_connection_id_push_bill_payments_bill_payment_id_200_application_json_object: Optional[DeleteCompaniesCompanyIDConnectionsConnectionIDPushBillPaymentsBillPaymentID200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    