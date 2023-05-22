"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import addresstype as shared_addresstype
from ..shared import phonenumbertype as shared_phonenumbertype
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompanyDatasetAddresses:
    
    type: shared_addresstype.AddressType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of the address"""
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
class CompanyDatasetPhone:
    
    number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number') }})
    r"""A phone number."""
    type: shared_phonenumbertype.PhoneNumberType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of phone number"""
    
class CompanyDatasetWeblinkType(str, Enum):
    r"""The type of the weblink."""
    WEBSITE = 'Website'
    SOCIAL = 'Social'
    UNKNOWN = 'Unknown'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompanyDatasetWeblink:
    r"""Weblink associated with the company."""
    
    type: Optional[CompanyDatasetWeblinkType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of the weblink."""
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""The full URL for the weblink."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompanyDataset:
    r"""> View the coverage for company info in the <a className=\\"external\\" href=\\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=cashFlowStatement\\" target=\\"_blank\\">Data coverage explorer</a>.
    
    Company info provides standard details about a linked company such as their address, phone number, and company registration.
    
    > **Company information or companies?**
    > 
    > Company information is standard information that is held in the accounting platform about a company. `Companies` is an endpoint that lists businesses in the Codat system that have linked and shared their data sources.
    """
    
    accounting_platform_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountingPlatformRef'), 'exclude': lambda f: f is None }})
    r"""Identifier or reference for the company in the accounting platform."""
    addresses: Optional[list[CompanyDatasetAddresses]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addresses'), 'exclude': lambda f: f is None }})
    r"""An array of Addresses."""
    base_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('baseCurrency'), 'exclude': lambda f: f is None }})
    r"""Currency set in the accounting platform of the linked company. Used by the currency rate."""
    company_legal_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyLegalName'), 'exclude': lambda f: f is None }})
    r"""Registered legal name of the linked company."""
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyName'), 'exclude': lambda f: f is None }})
    r"""Name of the linked company."""
    created_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdDate'), 'exclude': lambda f: f is None }})
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
    financial_year_start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('financialYearStartDate'), 'exclude': lambda f: f is None }})
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
    ledger_lock_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ledgerLockDate'), 'exclude': lambda f: f is None }})
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
    phone_numbers: Optional[list[CompanyDatasetPhone]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phoneNumbers'), 'exclude': lambda f: f is None }})
    r"""An array of phone numbers."""
    registration_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('registrationNumber'), 'exclude': lambda f: f is None }})
    r"""Registration number given to the linked company by the companies authority in the country of origin. In the UK this is Companies House."""
    source_urls: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceUrls'), 'exclude': lambda f: f is None }})
    r"""URL addresses for the accounting source.
    
    For example, for Xero integrations two URLs are returned. These have many potential use cases, such as [deep linking](https://developer.xero.com/documentation/api-guides/deep-link-xero).
    """
    tax_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxNumber'), 'exclude': lambda f: f is None }})
    r"""Company tax number."""
    web_links: Optional[list[CompanyDatasetWeblink]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webLinks'), 'exclude': lambda f: f is None }})
    r"""An array of weblinks."""
    