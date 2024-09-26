"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from enum import Enum
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TrackingRecordRefDataType(str, Enum):
    r"""Name of underlying data type."""

    CUSTOMERS = "customers"
    SUPPLIERS = "suppliers"
    TRACKING_CATEGORIES = "trackingCategories"


class TrackingRecordRefTypedDict(TypedDict):
    r"""Links to the customer or tracking category."""

    data_type: NotRequired[TrackingRecordRefDataType]
    r"""Name of underlying data type."""
    id: NotRequired[str]
    r"""'id' of the underlying record or data type."""


class TrackingRecordRef(BaseModel):
    r"""Links to the customer or tracking category."""

    data_type: Annotated[
        Optional[TrackingRecordRefDataType], pydantic.Field(alias="dataType")
    ] = None
    r"""Name of underlying data type."""

    id: Optional[str] = None
    r"""'id' of the underlying record or data type."""
