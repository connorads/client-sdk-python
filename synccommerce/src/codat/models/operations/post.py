"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class PostRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONFeesAccountsAccountOptions:
    
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification'), 'exclude': lambda f: f is None }})
    r"""Classification of the type of G/L account."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the account."""  
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nominalCode'), 'exclude': lambda f: f is None }})
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONFeesAccounts:
    r"""G/L account object for configuration."""
    
    account_options: Optional[list[Post200ApplicationJSONFeesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountOptions'), 'exclude': lambda f: f is None }})
    r"""Object containing account options."""  
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('descriptionText'), 'exclude': lambda f: f is None }})
    r"""Descriprtive text for sales configuration section."""  
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labelText'), 'exclude': lambda f: f is None }})
    r"""Label text for sales configuration section."""  
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    r"""Required section to be configured for sync."""  
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    r"""Selected account id from the list of available accounts."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONFeesFeesSupplierSupplierOptions:
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the option."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name value of the option."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONFeesFeesSupplier:
    
    selected_supplier_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedSupplierId'), 'exclude': lambda f: f is None }})
    r"""Selected supplier id from the list of supplier records on the accounting software."""  
    supplier_options: Optional[list[Post200ApplicationJSONFeesFeesSupplierSupplierOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplierOptions'), 'exclude': lambda f: f is None }})
    r"""List of supplier options from the list of supplier records on the accounting software."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONFees:
    
    accounts: Optional[dict[str, Post200ApplicationJSONFeesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts'), 'exclude': lambda f: f is None }})  
    fees_supplier: Optional[Post200ApplicationJSONFeesFeesSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feesSupplier'), 'exclude': lambda f: f is None }})  
    sync_fees: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncFees'), 'exclude': lambda f: f is None }})
    r"""Boolean indicator to enable syncing fees."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONNewPaymentsAccountsAccountOptions:
    
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification'), 'exclude': lambda f: f is None }})
    r"""Classification of the type of G/L account."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the account."""  
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nominalCode'), 'exclude': lambda f: f is None }})
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONNewPaymentsAccounts:
    r"""G/L account object for configuration."""
    
    account_options: Optional[list[Post200ApplicationJSONNewPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountOptions'), 'exclude': lambda f: f is None }})
    r"""Object containing account options."""  
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('descriptionText'), 'exclude': lambda f: f is None }})
    r"""Descriprtive text for sales configuration section."""  
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labelText'), 'exclude': lambda f: f is None }})
    r"""Label text for sales configuration section."""  
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    r"""Required section to be configured for sync."""  
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    r"""Selected account id from the list of available accounts."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONNewPayments:
    
    accounts: Optional[dict[str, Post200ApplicationJSONNewPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts'), 'exclude': lambda f: f is None }})  
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncPayments'), 'exclude': lambda f: f is None }})
    r"""Boolean indicator for syncing payments."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONPaymentsAccountsAccountOptions:
    
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification'), 'exclude': lambda f: f is None }})
    r"""Classification of the type of G/L account."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the account."""  
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nominalCode'), 'exclude': lambda f: f is None }})
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONPaymentsAccounts:
    r"""G/L account object for configuration."""
    
    account_options: Optional[list[Post200ApplicationJSONPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountOptions'), 'exclude': lambda f: f is None }})
    r"""Object containing account options."""  
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('descriptionText'), 'exclude': lambda f: f is None }})
    r"""Descriprtive text for sales configuration section."""  
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labelText'), 'exclude': lambda f: f is None }})
    r"""Label text for sales configuration section."""  
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    r"""Required section to be configured for sync."""  
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    r"""Selected account id from the list of available accounts."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONPayments:
    
    accounts: Optional[dict[str, Post200ApplicationJSONPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts'), 'exclude': lambda f: f is None }})  
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncPayments'), 'exclude': lambda f: f is None }})
    r"""Boolean indicator for syncing sales."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesAccountsAccountOptions:
    
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classification'), 'exclude': lambda f: f is None }})
    r"""Classification of the type of G/L account."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the account, unique for the company."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the account."""  
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nominalCode'), 'exclude': lambda f: f is None }})
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesAccounts:
    r"""G/L account object for configuration."""
    
    account_options: Optional[list[Post200ApplicationJSONSalesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountOptions'), 'exclude': lambda f: f is None }})
    r"""Object containing account options."""  
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('descriptionText'), 'exclude': lambda f: f is None }})
    r"""Descriprtive text for sales configuration section."""  
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labelText'), 'exclude': lambda f: f is None }})
    r"""Label text for sales configuration section."""  
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    r"""Required section to be configured for sync."""  
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    r"""Selected account id from the list of available accounts."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesGroupingGroupingLevelsInvoiceLevel:
    
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groupByOptions'), 'exclude': lambda f: f is None }})
    r"""Options for grouping sales."""  
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedGroupByOptions'), 'exclude': lambda f: f is None }})
    r"""Selected array of grouping options."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesGroupingGroupingLevelsInvoiceLineLevel:
    
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groupByOptions'), 'exclude': lambda f: f is None }})
    r"""Options for grouping on invoice lines."""  
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedGroupByOptions'), 'exclude': lambda f: f is None }})
    r"""Invoice line level selection."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesGroupingGroupingLevels:
    
    invoice_level: Optional[Post200ApplicationJSONSalesGroupingGroupingLevelsInvoiceLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceLevel'), 'exclude': lambda f: f is None }})  
    invoice_line_level: Optional[Post200ApplicationJSONSalesGroupingGroupingLevelsInvoiceLineLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceLineLevel'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesGroupingGroupingPeriod:
    
    grouping_period_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groupingPeriodOptions'), 'exclude': lambda f: f is None }})
    r"""Array of grouping period options."""  
    selected_grouping_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedGroupingPeriod'), 'exclude': lambda f: f is None }})
    r"""Grouping period i.e. Daily sales."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesGrouping:
    
    grouping_levels: Optional[Post200ApplicationJSONSalesGroupingGroupingLevels] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groupingLevels'), 'exclude': lambda f: f is None }})  
    grouping_period: Optional[Post200ApplicationJSONSalesGroupingGroupingPeriod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groupingPeriod'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesInvoiceStatus:
    
    invoice_status_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceStatusOptions'), 'exclude': lambda f: f is None }})
    r"""Options for invoice statuses."""  
    selected_invoice_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedInvoiceStatus'), 'exclude': lambda f: f is None }})
    r"""Selected option for invoice status for invoice to be synced."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesNewTaxRatesAccountingTaxRateOptions:
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the option."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name value of the option."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesNewTaxRatesCommerceTaxRateOptions:
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the option."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name value of the option."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesNewTaxRatesDefaultZeroTaxRateOptions:
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the option."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name value of the option."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesNewTaxRatesTaxRateMappings:
    
    selected_accounting_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedAccountingTaxRateId'), 'exclude': lambda f: f is None }})
    r"""Selected tax rate id from the list of tax rates on the accounting software."""  
    selected_commerce_tax_rate_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedCommerceTaxRateIds'), 'exclude': lambda f: f is None }})
    r"""Selected tax component id from the list of tax components on the commerce software."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesNewTaxRates:
    
    accounting_tax_rate_options: Optional[list[Post200ApplicationJSONSalesNewTaxRatesAccountingTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountingTaxRateOptions'), 'exclude': lambda f: f is None }})
    r"""Array of accounting tax rate options."""  
    commerce_tax_rate_options: Optional[list[Post200ApplicationJSONSalesNewTaxRatesCommerceTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commerceTaxRateOptions'), 'exclude': lambda f: f is None }})
    r"""Array of tax component options."""  
    default_zero_tax_rate_options: Optional[list[Post200ApplicationJSONSalesNewTaxRatesDefaultZeroTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultZeroTaxRateOptions'), 'exclude': lambda f: f is None }})
    r"""Default zero tax rate selected for sync."""  
    selected_default_zero_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedDefaultZeroTaxRateId'), 'exclude': lambda f: f is None }})
    r"""Default tax rate selected for sync."""  
    tax_rate_mappings: Optional[list[Post200ApplicationJSONSalesNewTaxRatesTaxRateMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateMappings'), 'exclude': lambda f: f is None }})
    r"""Array of tax component to rate mapppings."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesSalesCustomerCustomerOptions:
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the option."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name value of the option."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesSalesCustomer:
    
    customer_options: Optional[list[Post200ApplicationJSONSalesSalesCustomerCustomerOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerOptions'), 'exclude': lambda f: f is None }})
    r"""List of customer options from the list of customer records on the accounting software."""  
    selected_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedCustomerId'), 'exclude': lambda f: f is None }})
    r"""Selected customer id from the list of customer records on the accounting software."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesTaxRatesTaxRateOptions:
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the option."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name value of the option."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSalesTaxRates:
    
    selected_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedTaxRateId'), 'exclude': lambda f: f is None }})
    r"""Selected tax rate id from the list of tax rates on the accounting software."""  
    tax_rate_options: Optional[list[Post200ApplicationJSONSalesTaxRatesTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateOptions'), 'exclude': lambda f: f is None }})
    r"""Array of tax rate options object."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSONSales:
    
    accounts: Optional[dict[str, Post200ApplicationJSONSalesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts'), 'exclude': lambda f: f is None }})  
    grouping: Optional[Post200ApplicationJSONSalesGrouping] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grouping'), 'exclude': lambda f: f is None }})  
    invoice_status: Optional[Post200ApplicationJSONSalesInvoiceStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceStatus'), 'exclude': lambda f: f is None }})  
    new_tax_rates: Optional[Post200ApplicationJSONSalesNewTaxRates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newTaxRates'), 'exclude': lambda f: f is None }})  
    sales_customer: Optional[Post200ApplicationJSONSalesSalesCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('salesCustomer'), 'exclude': lambda f: f is None }})  
    sync_sales: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncSales'), 'exclude': lambda f: f is None }})
    r"""Boolean indicator for syncing sales."""  
    tax_rates: Optional[dict[str, Post200ApplicationJSONSalesTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRates'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Post200ApplicationJSON:
    r"""Success"""
    
    fees: Optional[Post200ApplicationJSONFees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fees'), 'exclude': lambda f: f is None }})  
    new_payments: Optional[Post200ApplicationJSONNewPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newPayments'), 'exclude': lambda f: f is None }})  
    payments: Optional[Post200ApplicationJSONPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payments'), 'exclude': lambda f: f is None }})  
    sales: Optional[Post200ApplicationJSONSales] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sales'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class PostResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    post_200_application_json_object: Optional[Post200ApplicationJSON] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    