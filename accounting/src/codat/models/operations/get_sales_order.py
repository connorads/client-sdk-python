"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class GetSalesOrderRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    sales_order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'salesOrderId', 'style': 'simple', 'explode': False }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateCustomerRef:
    r"""The customer that the sales order is recorded against in the accounting system."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyName'), 'exclude': lambda f: f is None }})  
    
class GetSalesOrderSourceModifiedDateInvoicingStatusEnum(str, Enum):
    r"""If the sales order is converted to an invoice, or will be in future, the invoicingStatus field indicates the current stage of the invoicing process."""
    UNKNOWN = "Unknown"
    PARTIALLY_INVOICED = "PartiallyInvoiced"
    INVOICED = "Invoiced"
    NOT_INVOICED = "NotInvoiced"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItemsAccountRef:
    r"""Reference to the account to which the line item is linked."""
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' from the Accounts data type."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""'name' from the Accounts data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItemsItemRef:
    r"""Reference to the product or inventory item to which the line item is linked."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItemsTaxRateRef:
    r"""Reference to the tax rate to which the line item is linked."""
    
    effective_tax_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('effectiveTaxRate'), 'exclude': lambda f: f is None }})
    r"""Applicable tax rate."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' from the 'taxRates' data type."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""'name' from the 'taxRates' data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItemsTracking:
    
    record_refs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRefs'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateLineItems:
    
    account_ref: Optional[GetSalesOrderSourceModifiedDateLineItemsAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the account to which the line item is linked."""  
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the goods or services that have been ordered."""  
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAmount'), 'exclude': lambda f: f is None }})
    r"""Value of any discounts applied."""  
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    r"""Percentage rate (from 0 to 100) of any discounts applied to the unit amount."""  
    item_ref: Optional[GetSalesOrderSourceModifiedDateLineItemsItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the product or inventory item to which the line item is linked."""  
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'exclude': lambda f: f is None }})
    r"""Number of units that have been ordered."""  
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'exclude': lambda f: f is None }})
    r"""Amount of the line, inclusive of discounts but exclusive of tax."""  
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'exclude': lambda f: f is None }})
    r"""Amount of tax for the line."""  
    tax_rate_ref: Optional[GetSalesOrderSourceModifiedDateLineItemsTaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the tax rate to which the line item is linked."""  
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of the line, inclusive of discounts and tax."""  
    tracking: Optional[GetSalesOrderSourceModifiedDateLineItemsTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})  
    unit_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitAmount'), 'exclude': lambda f: f is None }})
    r"""Price of each unit."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateMetadata:
    
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is None }})  
    
class GetSalesOrderSourceModifiedDateShipToAddressTypeEnum(str, Enum):
    r"""Type of the address."""
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateShipToAddress:
    r"""Delivery address for any goods that have been ordered."""
    
    type: GetSalesOrderSourceModifiedDateShipToAddressTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
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
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateShipToContact:
    r"""Details of the named contact at the delivery address."""
    
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""Email address of the contact at the delivery address."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the contact at the delivery address."""  
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Phone number of the contact at the delivery address."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDateShipTo:
    r"""Delivery details for any goods that have been ordered."""
    
    address: Optional[GetSalesOrderSourceModifiedDateShipToAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""Delivery address for any goods that have been ordered."""  
    contact: Optional[GetSalesOrderSourceModifiedDateShipToContact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contact'), 'exclude': lambda f: f is None }})
    r"""Details of the named contact at the delivery address."""  
    
class GetSalesOrderSourceModifiedDateStatusEnum(str, Enum):
    r"""Current state of the sales order."""
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    OPEN = "Open"
    CLOSED = "Closed"
    VOID = "Void"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSalesOrderSourceModifiedDate:
    r"""> View the coverage for sales orders in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=salesOrders\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A sales order represents a customer's intention to purchase goods or services from a seller and usually includes information such as the expected delivery date and shipping details. This information can be used to provide visibility on a business's expected receivables and to track sales through the full procurement process.
    
    A sales order is typically converted to an [invoice](https://docs.codat.io/accounting-api#/schemas/Invoice) after approval.
    """
    
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""Currency of the sales order."""  
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
    customer_purchase_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerPurchaseOrderNumber'), 'exclude': lambda f: f is None }})
    r"""A customer-supplied identifier for the purchase order in the customer's system."""  
    customer_ref: Optional[GetSalesOrderSourceModifiedDateCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    r"""The customer that the sales order is recorded against in the accounting system."""  
    expected_delivery_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expectedDeliveryDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Expected delivery date for any goods that have been ordered."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the sales order, unique for the company in the accounting platform."""  
    invoicing_status: Optional[GetSalesOrderSourceModifiedDateInvoicingStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoicingStatus'), 'exclude': lambda f: f is None }})
    r"""If the sales order is converted to an invoice, or will be in future, the invoicingStatus field indicates the current stage of the invoicing process."""  
    issue_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issueDate'), 'exclude': lambda f: f is None }})
    r"""Date of the sales order as recorded in the accounting platform."""  
    line_items: Optional[list[GetSalesOrderSourceModifiedDateLineItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems'), 'exclude': lambda f: f is None }})
    r"""An array of line items."""  
    metadata: Optional[GetSalesOrderSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('note'), 'exclude': lambda f: f is None }})
    r"""Any additional information associated with the sales order."""  
    sales_order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('salesOrderNumber'), 'exclude': lambda f: f is None }})
    r"""Friendly reference for the sales order, commonly generated by the accounting platform."""  
    ship_to: Optional[GetSalesOrderSourceModifiedDateShipTo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipTo'), 'exclude': lambda f: f is None }})
    r"""Delivery details for any goods that have been ordered."""  
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    status: Optional[GetSalesOrderSourceModifiedDateStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Current state of the sales order."""  
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'exclude': lambda f: f is None }})
    r"""Total amount of the sales order, including discounts but excluding tax."""  
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of the sales order, including discounts and tax."""  
    total_discount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalDiscount'), 'exclude': lambda f: f is None }})
    r"""	
    Total value of any discounts applied to the sales order.
    """  
    total_tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalTaxAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of tax included in the sales order."""  
    

@dataclasses.dataclass
class GetSalesOrderResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    source_modified_date: Optional[GetSalesOrderSourceModifiedDate] = dataclasses.field(default=None)
    r"""Success"""  
    