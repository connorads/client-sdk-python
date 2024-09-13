"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .profitandlossreport import ProfitAndLossReport, ProfitAndLossReportTypedDict
from .reportbasis import ReportBasis
from codat_accounting.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ProfitAndLossReportInputTypedDict(TypedDict):
    r"""> **Language tip:** Profit and loss statement is also referred to as **income statement** under US GAAP (Generally Accepted Accounting Principles).

    > View the coverage for profit and loss in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=profitAndLoss\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    The purpose of a profit and loss report is to present the financial performance of a company over a specified time period.

    A profit and loss report shows a company's total income and expenses for a specified period of time and whether a profit or loss has been made.

    > **Profit and loss or balance sheet?**
    > Profit and loss reports summarise the total revenue, expenses, and profit or loss over a specified time period. A balance sheet report presents all assets, liability, and equity for a given date.


    **Structure of this report**
    This report will reflect the structure and line descriptions that the business has set in their own accounting software.

    **History**
    By default, Codat pulls (up to) 24 months of profit and loss history for a company. You can adjust this to fetch more history, where available, by updating the `monthsToSync` value for `profitAndLoss` on the [data type settings endpoint](https://docs.codat.io/codat-api#/operations/post-profile-syncSettings).

    **Want to pull this in a standardised structure?**
    Our [Enhanced Financials](https://docs.codat.io/lending/features/financial-statements-overview) endpoints provide the same report under standardized headings, allowing you to pull it in the same format for all of your business customers.
    """

    currency: str
    r"""Base currency of the company in which the profit and loss report is presented."""
    report_basis: ReportBasis
    r"""The basis of a report."""
    reports: List[ProfitAndLossReportTypedDict]
    r"""An array of profit and loss reports."""
    earliest_available_month: NotRequired[str]
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
    most_recent_available_month: NotRequired[str]
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


class ProfitAndLossReportInput(BaseModel):
    r"""> **Language tip:** Profit and loss statement is also referred to as **income statement** under US GAAP (Generally Accepted Accounting Principles).

    > View the coverage for profit and loss in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=profitAndLoss\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    The purpose of a profit and loss report is to present the financial performance of a company over a specified time period.

    A profit and loss report shows a company's total income and expenses for a specified period of time and whether a profit or loss has been made.

    > **Profit and loss or balance sheet?**
    > Profit and loss reports summarise the total revenue, expenses, and profit or loss over a specified time period. A balance sheet report presents all assets, liability, and equity for a given date.


    **Structure of this report**
    This report will reflect the structure and line descriptions that the business has set in their own accounting software.

    **History**
    By default, Codat pulls (up to) 24 months of profit and loss history for a company. You can adjust this to fetch more history, where available, by updating the `monthsToSync` value for `profitAndLoss` on the [data type settings endpoint](https://docs.codat.io/codat-api#/operations/post-profile-syncSettings).

    **Want to pull this in a standardised structure?**
    Our [Enhanced Financials](https://docs.codat.io/lending/features/financial-statements-overview) endpoints provide the same report under standardized headings, allowing you to pull it in the same format for all of your business customers.
    """

    currency: str
    r"""Base currency of the company in which the profit and loss report is presented."""

    report_basis: Annotated[ReportBasis, pydantic.Field(alias="reportBasis")]
    r"""The basis of a report."""

    reports: List[ProfitAndLossReport]
    r"""An array of profit and loss reports."""

    earliest_available_month: Annotated[
        Optional[str], pydantic.Field(alias="earliestAvailableMonth")
    ] = None
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

    most_recent_available_month: Annotated[
        Optional[str], pydantic.Field(alias="mostRecentAvailableMonth")
    ] = None
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
