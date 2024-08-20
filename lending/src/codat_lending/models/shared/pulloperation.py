"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DatasetStatus(str, Enum):
    r"""The current status of the dataset."""
    INITIAL = "Initial"
    QUEUED = "Queued"
    FETCHING = "Fetching"
    MAP_QUEUED = "MapQueued"
    MAPPING = "Mapping"
    COMPLETE = "Complete"
    FETCH_ERROR = "FetchError"
    MAP_ERROR = "MapError"
    INTERNAL_ERROR = "InternalError"
    PROCESSING_QUEUED = "ProcessingQueued"
    PROCESSING = "Processing"
    PROCESSING_ERROR = "ProcessingError"
    VALIDATION_QUEUED = "ValidationQueued"
    VALIDATING = "Validating"
    VALIDATION_ERROR = "ValidationError"
    AUTH_ERROR = "AuthError"
    CANCELLED = "Cancelled"
    NOT_SUPPORTED = "NotSupported"
    RATE_LIMIT_ERROR = "RateLimitError"
    PERMISSIONS_ERROR = "PermissionsError"
    PREREQUISITE_NOT_MET = "PrerequisiteNotMet"

class PullOperationTypedDict(TypedDict):
    r"""Information about a queued, in progress or completed pull operation.
    *Formally called `dataset`*
    """
    
    company_id: str
    r"""Unique identifier of the company associated to this pull operation."""
    connection_id: str
    r"""Unique identifier of the connection associated to this pull operation."""
    data_type: str
    r"""The data type you are requesting in a pull operation."""
    id: str
    r"""Unique identifier of the pull operation."""
    is_completed: bool
    r"""`True` if the pull operation is completed successfully. The `isCompleted` property is not queryable. To filter failed pull operations, query by `status!=Complete&&status!=NotSupported` instead."""
    is_errored: bool
    r"""`True` if the pull operation entered an error state."""
    progress: int
    r"""An integer signifying the progress of the pull operation."""
    requested: str
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
    status: DatasetStatus
    r"""The current status of the dataset."""
    completed: NotRequired[str]
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
    error_message: NotRequired[Nullable[str]]
    r"""A message about a transient or persistent error returned by Codat or the source platform."""
    status_description: NotRequired[Nullable[str]]
    r"""Additional information about the dataset status."""
    

class PullOperation(BaseModel):
    r"""Information about a queued, in progress or completed pull operation.
    *Formally called `dataset`*
    """
    
    company_id: Annotated[str, pydantic.Field(alias="companyId")]
    r"""Unique identifier of the company associated to this pull operation."""
    connection_id: Annotated[str, pydantic.Field(alias="connectionId")]
    r"""Unique identifier of the connection associated to this pull operation."""
    data_type: Annotated[str, pydantic.Field(alias="dataType")]
    r"""The data type you are requesting in a pull operation."""
    id: str
    r"""Unique identifier of the pull operation."""
    is_completed: Annotated[bool, pydantic.Field(alias="isCompleted")]
    r"""`True` if the pull operation is completed successfully. The `isCompleted` property is not queryable. To filter failed pull operations, query by `status!=Complete&&status!=NotSupported` instead."""
    is_errored: Annotated[bool, pydantic.Field(alias="isErrored")]
    r"""`True` if the pull operation entered an error state."""
    progress: int
    r"""An integer signifying the progress of the pull operation."""
    requested: str
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
    status: DatasetStatus
    r"""The current status of the dataset."""
    completed: Optional[str] = None
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
    error_message: Annotated[OptionalNullable[str], pydantic.Field(alias="errorMessage")] = UNSET
    r"""A message about a transient or persistent error returned by Codat or the source platform."""
    status_description: Annotated[OptionalNullable[str], pydantic.Field(alias="statusDescription")] = UNSET
    r"""Additional information about the dataset status."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["completed", "errorMessage", "statusDescription"]
        nullable_fields = ["errorMessage", "statusDescription"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
