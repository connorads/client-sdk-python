"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatcommon import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DataStatus:
    r"""Describes the state of data in the Codat cache for a company and data type"""
    current_status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentStatus') }})
    data_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType') }})
    last_successful_sync: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastSuccessfulSync') }})
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
    latest_successful_sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latestSuccessfulSyncId'), 'exclude': lambda f: f is None }})
    latest_sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latestSyncId'), 'exclude': lambda f: f is None }})
    

