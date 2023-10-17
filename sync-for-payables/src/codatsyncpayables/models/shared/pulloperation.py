"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import datatype as shared_datatype
from codatsyncpayables import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class PullOperationStatus(str, Enum):
    r"""The current status of the pull operation."""
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
    r"""Unique identifier of the company associated to this pull operation."""
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionId') }})
    r"""Unique identifier of the connection associated to this pull operation."""
    data_type: shared_datatype.DataType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType') }})
    r"""Available Data types"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier of the pull operation."""
    is_completed: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isCompleted') }})
    r"""`True` if the pull operation completed successfully."""
    is_errored: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isErrored') }})
    r"""`True` if the pull operation entered an error state."""
    progress: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('progress') }})
    r"""An integer signifying the progress of the pull operation."""
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
    r"""The current status of the pull operation."""
    completed: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completed'), 'exclude': lambda f: f is None }})
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
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage') }})
    r"""A message about a transient or persistent error."""
    

