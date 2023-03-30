"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class CreateCustomerSourceModifiedDateAddressesTypeEnum(str, Enum):
    r"""Type of the address."""
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomerSourceModifiedDateAddresses:
    
    type: CreateCustomerSourceModifiedDateAddressesTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of the address."""  
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})
    r"""City of the customer address."""  
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""Country of the customer address."""  
    line1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line1'), 'exclude': lambda f: f is None }})
    r"""Line 1 of the customer address."""  
    line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line2'), 'exclude': lambda f: f is None }})
    r"""Line 2 of the customer address."""  
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postalCode'), 'exclude': lambda f: f is None }})
    r"""Postal code or zip code."""  
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Region of the customer address."""  
    
class CreateCustomerSourceModifiedDateContactsAddressTypeEnum(str, Enum):
    r"""Type of the address."""
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomerSourceModifiedDateContactsAddress:
    r"""An object of Address information."""
    
    type: CreateCustomerSourceModifiedDateContactsAddressTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of the address."""  
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})
    r"""City of the customer address."""  
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""Country of the customer address."""  
    line1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line1'), 'exclude': lambda f: f is None }})
    r"""Line 1 of the customer address."""  
    line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line2'), 'exclude': lambda f: f is None }})
    r"""Line 2 of the customer address."""  
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postalCode'), 'exclude': lambda f: f is None }})
    r"""Postal code or zip code."""  
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Region of the customer address."""  
    
class CreateCustomerSourceModifiedDateContactsPhoneTypeEnum(str, Enum):
    r"""Type of phone number."""
    UNKNOWN = "Unknown"
    PRIMARY = "Primary"
    LANDLINE = "Landline"
    MOBILE = "Mobile"
    FAX = "Fax"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomerSourceModifiedDateContactsPhone:
    
    type: CreateCustomerSourceModifiedDateContactsPhoneTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of phone number."""  
    number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number'), 'exclude': lambda f: f is None }})
    r"""Phone number for a customer contact."""  
    
class CreateCustomerSourceModifiedDateContactsStatusEnum(str, Enum):
    r"""Status of customer contacts.
    
    Customers can have multiple contacts.
    """
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomerSourceModifiedDateContacts:
    
    status: CreateCustomerSourceModifiedDateContactsStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Status of customer contacts.
    
    Customers can have multiple contacts.
    """  
    address: Optional[CreateCustomerSourceModifiedDateContactsAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""An object of Address information."""  
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""Email of a contact for a customer."""  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:
    
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
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of a contact for a customer."""  
    phone: Optional[list[CreateCustomerSourceModifiedDateContactsPhone]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""An array of Phone numbers."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomerSourceModifiedDateMetadata:
    
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the record has been deleted in the third-party system this record originated from."""  
    
class CreateCustomerSourceModifiedDateStatusEnum(str, Enum):
    r"""Current state of the customer."""
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomerSourceModifiedDateSupplementalData:
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""
    
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomerSourceModifiedDate:
    r"""> View the coverage for customers in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A customer is a person or organisation that buys goods or services. From the Customers endpoints, you can retrieve a [list of all the customers of a company](https://api.codat.io/swagger/index.html#/Customers/get_companies__companyId__data_customers).
    
    Customers' data links to accounts receivable [invoices](https://docs.codat.io/accounting-api#/schemas/Invoice).
    
    """
    
    status: CreateCustomerSourceModifiedDateStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Current state of the customer."""  
    addresses: Optional[list[CreateCustomerSourceModifiedDateAddresses]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addresses'), 'exclude': lambda f: f is None }})
    r"""An array of Addresses."""  
    contact_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contactName'), 'exclude': lambda f: f is None }})
    r"""Name of the main contact for the identified customer."""  
    contacts: Optional[list[CreateCustomerSourceModifiedDateContacts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contacts'), 'exclude': lambda f: f is None }})
    r"""An array of Contacts."""  
    customer_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerName'), 'exclude': lambda f: f is None }})
    r"""Name of the customer as recorded in the accounting system, typically the company name."""  
    default_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultCurrency'), 'exclude': lambda f: f is None }})
    r"""Default currency the transactional data of the customer is recorded in."""  
    email_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailAddress'), 'exclude': lambda f: f is None }})
    r"""Email address the customer can be contacted by."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the customer, unique to the company in the accounting platform."""  
    metadata: Optional[CreateCustomerSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Phone number the customer can be contacted by."""  
    registration_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('registrationNumber'), 'exclude': lambda f: f is None }})
    r"""Company number. In the UK, this is typically the Companies House company registration number."""  
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    supplemental_data: Optional[CreateCustomerSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""  
    tax_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxNumber'), 'exclude': lambda f: f is None }})
    r"""Company tax number."""  
    

@dataclasses.dataclass
class CreateCustomerRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    request_body: Optional[CreateCustomerSourceModifiedDate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})  
    
class CreateCustomer200ApplicationJSONChangesPushOperationReferenceDataTypeEnum(str, Enum):
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
class CreateCustomer200ApplicationJSONChangesPushOperationReference:
    
    data_type: Optional[CreateCustomer200ApplicationJSONChangesPushOperationReferenceDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Available Data types"""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})  
    
class CreateCustomer200ApplicationJSONChangesPushChangeTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREATED = "Created"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    ATTACHMENT_UPLOADED = "AttachmentUploaded"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONChanges:
    
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachmentId'), 'exclude': lambda f: f is None }})  
    record_ref: Optional[CreateCustomer200ApplicationJSONChangesPushOperationReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})  
    type: Optional[CreateCustomer200ApplicationJSONChangesPushChangeTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})  
    
class CreateCustomer200ApplicationJSONSourceModifiedDateAddressesTypeEnum(str, Enum):
    r"""Type of the address."""
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONSourceModifiedDateAddresses:
    
    type: CreateCustomer200ApplicationJSONSourceModifiedDateAddressesTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of the address."""  
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})
    r"""City of the customer address."""  
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""Country of the customer address."""  
    line1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line1'), 'exclude': lambda f: f is None }})
    r"""Line 1 of the customer address."""  
    line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line2'), 'exclude': lambda f: f is None }})
    r"""Line 2 of the customer address."""  
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postalCode'), 'exclude': lambda f: f is None }})
    r"""Postal code or zip code."""  
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Region of the customer address."""  
    
class CreateCustomer200ApplicationJSONSourceModifiedDateContactsAddressTypeEnum(str, Enum):
    r"""Type of the address."""
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONSourceModifiedDateContactsAddress:
    r"""An object of Address information."""
    
    type: CreateCustomer200ApplicationJSONSourceModifiedDateContactsAddressTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of the address."""  
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})
    r"""City of the customer address."""  
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""Country of the customer address."""  
    line1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line1'), 'exclude': lambda f: f is None }})
    r"""Line 1 of the customer address."""  
    line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line2'), 'exclude': lambda f: f is None }})
    r"""Line 2 of the customer address."""  
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postalCode'), 'exclude': lambda f: f is None }})
    r"""Postal code or zip code."""  
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Region of the customer address."""  
    
class CreateCustomer200ApplicationJSONSourceModifiedDateContactsPhoneTypeEnum(str, Enum):
    r"""Type of phone number."""
    UNKNOWN = "Unknown"
    PRIMARY = "Primary"
    LANDLINE = "Landline"
    MOBILE = "Mobile"
    FAX = "Fax"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONSourceModifiedDateContactsPhone:
    
    type: CreateCustomer200ApplicationJSONSourceModifiedDateContactsPhoneTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of phone number."""  
    number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number'), 'exclude': lambda f: f is None }})
    r"""Phone number for a customer contact."""  
    
class CreateCustomer200ApplicationJSONSourceModifiedDateContactsStatusEnum(str, Enum):
    r"""Status of customer contacts.
    
    Customers can have multiple contacts.
    """
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONSourceModifiedDateContacts:
    
    status: CreateCustomer200ApplicationJSONSourceModifiedDateContactsStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Status of customer contacts.
    
    Customers can have multiple contacts.
    """  
    address: Optional[CreateCustomer200ApplicationJSONSourceModifiedDateContactsAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""An object of Address information."""  
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""Email of a contact for a customer."""  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:
    
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
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of a contact for a customer."""  
    phone: Optional[list[CreateCustomer200ApplicationJSONSourceModifiedDateContactsPhone]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""An array of Phone numbers."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONSourceModifiedDateMetadata:
    
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the record has been deleted in the third-party system this record originated from."""  
    
class CreateCustomer200ApplicationJSONSourceModifiedDateStatusEnum(str, Enum):
    r"""Current state of the customer."""
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONSourceModifiedDateSupplementalData:
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""
    
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONSourceModifiedDate:
    r"""> View the coverage for customers in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A customer is a person or organisation that buys goods or services. From the Customers endpoints, you can retrieve a [list of all the customers of a company](https://api.codat.io/swagger/index.html#/Customers/get_companies__companyId__data_customers).
    
    Customers' data links to accounts receivable [invoices](https://docs.codat.io/accounting-api#/schemas/Invoice).
    
    """
    
    status: CreateCustomer200ApplicationJSONSourceModifiedDateStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Current state of the customer."""  
    addresses: Optional[list[CreateCustomer200ApplicationJSONSourceModifiedDateAddresses]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addresses'), 'exclude': lambda f: f is None }})
    r"""An array of Addresses."""  
    contact_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contactName'), 'exclude': lambda f: f is None }})
    r"""Name of the main contact for the identified customer."""  
    contacts: Optional[list[CreateCustomer200ApplicationJSONSourceModifiedDateContacts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contacts'), 'exclude': lambda f: f is None }})
    r"""An array of Contacts."""  
    customer_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerName'), 'exclude': lambda f: f is None }})
    r"""Name of the customer as recorded in the accounting system, typically the company name."""  
    default_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultCurrency'), 'exclude': lambda f: f is None }})
    r"""Default currency the transactional data of the customer is recorded in."""  
    email_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailAddress'), 'exclude': lambda f: f is None }})
    r"""Email address the customer can be contacted by."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the customer, unique to the company in the accounting platform."""  
    metadata: Optional[CreateCustomer200ApplicationJSONSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Phone number the customer can be contacted by."""  
    registration_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('registrationNumber'), 'exclude': lambda f: f is None }})
    r"""Company number. In the UK, this is typically the Companies House company registration number."""  
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    supplemental_data: Optional[CreateCustomer200ApplicationJSONSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""  
    tax_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxNumber'), 'exclude': lambda f: f is None }})
    r"""Company tax number."""  
    
class CreateCustomer200ApplicationJSONDataTypeEnum(str, Enum):
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

class CreateCustomer200ApplicationJSONPushOperationStatusEnum(str, Enum):
    r"""The status of the push operation."""
    PENDING = "Pending"
    FAILED = "Failed"
    SUCCESS = "Success"
    TIMED_OUT = "TimedOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONValidationValidationItem:
    
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemId'), 'exclude': lambda f: f is None }})  
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})  
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validatorName'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSONValidation:
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""
    
    errors: Optional[list[CreateCustomer200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})  
    warnings: Optional[list[CreateCustomer200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCustomer200ApplicationJSON:
    r"""Success"""
    
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId') }})
    r"""Unique identifier for your SMB in Codat."""  
    data_connection_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataConnectionKey') }})
    r"""Unique identifier for a company's data connection."""  
    push_operation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pushOperationKey') }})
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""  
    requested_on_utc: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestedOnUtc') }})
    r"""The datetime when the push was requested."""  
    status: CreateCustomer200ApplicationJSONPushOperationStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the push operation."""  
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})  
    changes: Optional[list[CreateCustomer200ApplicationJSONChanges]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changes'), 'exclude': lambda f: f is None }})  
    completed_on_utc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completedOnUtc'), 'exclude': lambda f: f is None }})
    r"""The datetime when the push was completed, null if Pending."""  
    data: Optional[CreateCustomer200ApplicationJSONSourceModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""> View the coverage for customers in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=customers\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A customer is a person or organisation that buys goods or services. From the Customers endpoints, you can retrieve a [list of all the customers of a company](https://api.codat.io/swagger/index.html#/Customers/get_companies__companyId__data_customers).
    
    Customers' data links to accounts receivable [invoices](https://docs.codat.io/accounting-api#/schemas/Invoice).
    
    """  
    data_type: Optional[CreateCustomer200ApplicationJSONDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""The type of data being pushed, eg invoices, customers."""  
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage'), 'exclude': lambda f: f is None }})  
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInMinutes'), 'exclude': lambda f: f is None }})  
    timeout_in_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInSeconds'), 'exclude': lambda f: f is None }})  
    validation: Optional[CreateCustomer200ApplicationJSONValidation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""  
    

@dataclasses.dataclass
class CreateCustomerResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    create_customer_200_application_json_object: Optional[CreateCustomer200ApplicationJSON] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    