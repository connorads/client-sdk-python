"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatcommon import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class PullOperationStatus(str, Enum):
    INITIAL = 'Initial'
    QUEUED = 'Queued'
    FETCHING = 'Fetching'
    MAP_QUEUED = 'MapQueued'
    MAPPING = 'Mapping'
    COMPLETE = 'Complete'
    FETCH_ERROR = 'FetchError'
    MAP_ERROR = 'MapError'
    INTERNAL_ERROR = 'InternalError'
    PROCESSING_QUEUED = 'ProcessingQueued'
    PROCESSING = 'Processing'
    PROCESSING_ERROR = 'ProcessingError'
    VALIDATION_QUEUED = 'ValidationQueued'
    VALIDATING = 'Validating'
    VALIDATION_ERROR = 'ValidationError'
    AUTH_ERROR = 'AuthError'
    CANCELLED = 'Cancelled'
    ROUTING = 'Routing'
    ROUTING_ERROR = 'RoutingError'
    NOT_SUPPORTED = 'NotSupported'
    RATE_LIMIT_ERROR = 'RateLimitError'
    PERMISSIONS_ERROR = 'PermissionsError'
    PREREQUISITE_NOT_MET = 'PrerequisiteNotMet'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PullOperation:
    r"""Information about a queued, in progress or completed pull operation.
    *Formally called `dataset`*
    """
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId') }})
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionId') }})
    data_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    is_completed: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isCompleted') }})
    is_errored: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isErrored') }})
    progress: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('progress') }})
    requested: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requested') }})
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
    status: PullOperationStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

