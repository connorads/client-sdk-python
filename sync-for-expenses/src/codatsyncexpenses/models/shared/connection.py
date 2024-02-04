"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .dataconnectionerror import DataConnectionError
from .dataconnectionstatus import DataConnectionStatus
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Dict, List, Optional

class SourceType(str, Enum):
    r"""The type of platform of the connection."""
    ACCOUNTING = 'Accounting'
    BANKING = 'Banking'
    BANK_FEED = 'BankFeed'
    COMMERCE = 'Commerce'
    EXPENSE = 'Expense'
    OTHER = 'Other'
    UNKNOWN = 'Unknown'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Connection:
    r"""A connection represents a [company's](https://docs.codat.io/sync-for-expenses-api#/schemas/Company) connection to a data source and allows you to synchronize data (pull and/or push) with that source.

    A company can have multiple data connections depending on the type of data source it is connecting to. For example, a single company can link to:

    - [Accounting data](https://docs.codat.io/accounting-api/overview) - 1 active connection.
    - [Banking data](https://docs.codat.io/banking-api/overview) - Multiple active connections.
    - [Commerce data](https://docs.codat.io/commerce-api/overview) - Multiple active connections.
    Any combination of accounting, banking, and commerce data connections is allowed.

    Before you can use a data connection to pull or push data, the company must grant you access to their business data by [linking the connection](https://docs.codat.io/auth-flow/overview).
    """
    created: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
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
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier for a company's data connection."""
    integration_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrationId') }})
    r"""A Codat ID representing the integration."""
    integration_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrationKey') }})
    r"""A unique four-character ID that identifies the platform of the company's data connection. This ensures continuity if the platform changes its name in the future."""
    link_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('linkUrl') }})
    r"""The link URL your customers can use to authorize access to their business application."""
    platform_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('platformName') }})
    r"""Name of integration connected to company."""
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    r"""A source-specific ID used to distinguish between different sources originating from the same data connection. In general, a data connection is a single data source. However, for TrueLayer, `sourceId` is associated with a specific bank and has a many-to-one relationship with the `integrationId`."""
    source_type: SourceType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    r"""The type of platform of the connection."""
    status: DataConnectionStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The current authorization status of the data connection."""
    additional_properties: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProperties'), 'exclude': lambda f: f is None }})
    connection_info: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionInfo'), 'exclude': lambda f: f is None }})
    data_connection_errors: Optional[List[DataConnectionError]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataConnectionErrors'), 'exclude': lambda f: f is None }})
    last_sync: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastSync'), 'exclude': lambda f: f is None }})
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
    

