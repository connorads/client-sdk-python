"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetAccountsForEnhancedBalanceSheetRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    r"""The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods."""  
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    r"""The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccountsForEnhancedBalanceSheetEnhancedReportReportInfo:
    
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyName'), 'exclude': lambda f: f is None }})
    r"""Company name the report was generated for."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.
    
    ## Unknown currencies
    
    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 
    
    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """  
    generated_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generatedDate'), 'exclude': lambda f: f is None }})
    r"""The date the report was generated."""  
    report_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportName'), 'exclude': lambda f: f is None }})
    r"""The name of the report."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccountsForEnhancedBalanceSheetEnhancedReportReportItemsAccountCategoryLevels:
    
    confidence: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confidence'), 'exclude': lambda f: f is None }})  
    level_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('levelName'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccountsForEnhancedBalanceSheetEnhancedReportReportItemsAccountCategory:
    
    levels: Optional[list[GetAccountsForEnhancedBalanceSheetEnhancedReportReportItemsAccountCategoryLevels]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('levels'), 'exclude': lambda f: f is None }})  
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccountsForEnhancedBalanceSheetEnhancedReportReportItems:
    
    account_category: Optional[GetAccountsForEnhancedBalanceSheetEnhancedReportReportItemsAccountCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountCategory'), 'exclude': lambda f: f is None }})  
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is None }})
    r"""The unique account ID."""  
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountName'), 'exclude': lambda f: f is None }})  
    balance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance'), 'exclude': lambda f: f is None }})  
    date_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'exclude': lambda f: f is None }})
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
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccountsForEnhancedBalanceSheetEnhancedReport:
    r"""OK"""
    
    report_info: Optional[GetAccountsForEnhancedBalanceSheetEnhancedReportReportInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportInfo'), 'exclude': lambda f: f is None }})  
    report_items: Optional[list[GetAccountsForEnhancedBalanceSheetEnhancedReportReportItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportItems'), 'exclude': lambda f: f is None }})
    r"""An array of report items."""  
    

@dataclasses.dataclass
class GetAccountsForEnhancedBalanceSheetResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    enhanced_report: Optional[GetAccountsForEnhancedBalanceSheetEnhancedReport] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    