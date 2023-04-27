"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import billlineitem as shared_billlineitem
from ..shared import billstatus_enum as shared_billstatus_enum
from ..shared import metadata as shared_metadata
from ..shared import paymentallocationpayment as shared_paymentallocationpayment
from ..shared import purchaseorderref as shared_purchaseorderref
from ..shared import supplierref as shared_supplierref
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BillPaymentAllocationAllocation:
    
    allocated_on_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allocatedOnDate'), 'exclude': lambda f: f is None }})

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
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})

    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.
    
    ## Unknown currencies
    
    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 
    
    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyRate'), 'exclude': lambda f: f is None }})

    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.
    
    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.  
    
    Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places). 
    
    For accounting platforms which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.
    
    ## Examples with base currency of GBP
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |
    
    ## Examples with base currency of USD
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |
    """
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})

    r"""The total amount that has been allocated."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BillPaymentAllocation:
    
    allocation: BillPaymentAllocationAllocation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allocation') }})

    payment: shared_paymentallocationpayment.PaymentAllocationPayment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment') }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BillSupplementalData:
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""
    
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BillWithholdingTax:
    
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})

    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Bill:
    r"""> **Invoices or bills?**
    >
    > We distinguish between invoices where the company *owes money* vs. *is owed money*. If the company has received an invoice, and owes money to someone else (accounts payable) we call this a Bill.
    >
    > See [Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) for the accounts receivable equivalent of bills.
    
    View the coverage for bills in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    In Codat, a bill contains details of:
    * When the bill was recorded in the accounting system.
    * How much the bill is for and the currency of the amount.
    * Who the bill was received from — the *supplier*.
    * What the bill is for — the *line items*.
    
    Some accounting platforms give a separate name to purchases where the payment is made immediately, such as something bought with a credit card or online payment. One example of this would be QuickBooks Online's *expenses*.
    
    You can find these types of transactions in our [Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) data model.
    """
    
    issue_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issueDate') }})

    status: shared_billstatus_enum.BillStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})

    r"""Current state of the bill."""
    sub_total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal') }})

    r"""Total amount of the bill, excluding any taxes."""
    tax_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount') }})

    r"""Amount of tax on the bill."""
    total_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount') }})

    r"""Amount of the bill, including tax."""
    amount_due: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amountDue'), 'exclude': lambda f: f is None }})

    r"""Amount outstanding on the bill."""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})

    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.
    
    ## Unknown currencies
    
    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 
    
    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyRate'), 'exclude': lambda f: f is None }})

    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.
    
    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.  
    
    Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places). 
    
    For accounting platforms which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.
    
    ## Examples with base currency of GBP
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |
    
    ## Examples with base currency of USD
    
    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |
    """
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is None }})

    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})

    r"""Identifier for the bill, unique for the company in the accounting platform."""
    line_items: Optional[list[shared_billlineitem.BillLineItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems'), 'exclude': lambda f: f is None }})

    r"""Array of Bill line items."""
    metadata: Optional[shared_metadata.Metadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})

    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})

    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('note'), 'exclude': lambda f: f is None }})

    r"""Any private, company notes about the bill, such as payment information."""
    payment_allocations: Optional[list[BillPaymentAllocation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentAllocations'), 'exclude': lambda f: f is None }})

    r"""An array of payment allocations."""
    purchase_order_refs: Optional[list[shared_purchaseorderref.PurchaseOrderRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purchaseOrderRefs'), 'exclude': lambda f: f is None }})

    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is None }})

    r"""User-friendly reference for the bill."""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})

    supplemental_data: Optional[BillSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})

    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""
    supplier_ref: Optional[shared_supplierref.SupplierRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplierRef'), 'exclude': lambda f: f is None }})

    r"""Reference to the supplier the record relates to."""
    withholding_tax: Optional[list[BillWithholdingTax]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('withholdingTax'), 'exclude': lambda f: f is None }})

    