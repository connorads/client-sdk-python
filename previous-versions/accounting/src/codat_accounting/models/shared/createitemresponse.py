"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .billitem import BillItem, BillItemTypedDict
from .datatype import DataType
from .invoiceitem import InvoiceItem, InvoiceItemTypedDict
from .itemstatus import ItemStatus
from .itemtype import ItemType
from .metadata import Metadata, MetadataTypedDict
from .pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
from .pushoperationstatus import PushOperationStatus
from .supplementaldata import SupplementalData, SupplementalDataTypedDict
from .validation import Validation, ValidationTypedDict
from codat_accounting.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired, deprecated


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class AccountingItemTypedDict(TypedDict):
    r"""> View the coverage for items in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    **Items** allow your customers to save and track details of the products and services that they buy and sell.

    """

    is_bill_item: bool
    r"""Whether you can use this item for bills."""
    is_invoice_item: bool
    r"""Whether you can use this item for invoices."""
    item_status: ItemStatus
    r"""Current state of the item, either:

    - `Active`: Available for use
    - `Archived`: Unavailable
    - `Unknown`

    Due to a [limitation in Xero's API](https://docs.codat.io/integrations/accounting/xero/xero-faq#why-do-all-of-my-items-from-xero-have-their-status-as-unknown), all items from Xero are mapped as `Unknown`.
    """
    type: ItemType
    r"""Type of the item."""
    bill_item: NotRequired[BillItemTypedDict]
    r"""Item details that are only for bills."""
    code: NotRequired[Nullable[str]]
    r"""Friendly reference for the item."""
    id: NotRequired[str]
    r"""Identifier for the item that is unique to a company in the accounting software."""
    invoice_item: NotRequired[InvoiceItemTypedDict]
    r"""Item details that are only for bills."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    name: NotRequired[Nullable[str]]
    r"""Name of the item in the accounting software."""
    source_modified_date: NotRequired[str]
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class AccountingItem(BaseModel):
    r"""> View the coverage for items in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    **Items** allow your customers to save and track details of the products and services that they buy and sell.

    """

    is_bill_item: Annotated[bool, pydantic.Field(alias="isBillItem")]
    r"""Whether you can use this item for bills."""

    is_invoice_item: Annotated[bool, pydantic.Field(alias="isInvoiceItem")]
    r"""Whether you can use this item for invoices."""

    item_status: Annotated[ItemStatus, pydantic.Field(alias="itemStatus")]
    r"""Current state of the item, either:

    - `Active`: Available for use
    - `Archived`: Unavailable
    - `Unknown`

    Due to a [limitation in Xero's API](https://docs.codat.io/integrations/accounting/xero/xero-faq#why-do-all-of-my-items-from-xero-have-their-status-as-unknown), all items from Xero are mapped as `Unknown`.
    """

    type: ItemType
    r"""Type of the item."""

    bill_item: Annotated[Optional[BillItem], pydantic.Field(alias="billItem")] = None
    r"""Item details that are only for bills."""

    code: OptionalNullable[str] = UNSET
    r"""Friendly reference for the item."""

    id: Optional[str] = None
    r"""Identifier for the item that is unique to a company in the accounting software."""

    invoice_item: Annotated[
        Optional[InvoiceItem], pydantic.Field(alias="invoiceItem")
    ] = None
    r"""Item details that are only for bills."""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    name: OptionalNullable[str] = UNSET
    r"""Name of the item in the accounting software."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    supplemental_data: Annotated[
        Optional[SupplementalData], pydantic.Field(alias="supplementalData")
    ] = None
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "billItem",
            "code",
            "id",
            "invoiceItem",
            "metadata",
            "modifiedDate",
            "name",
            "sourceModifiedDate",
            "supplementalData",
        ]
        nullable_fields = ["code", "name"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class CreateItemResponseTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for your SMB in Codat."""
    data_connection_key: str
    r"""Unique identifier for a company's data connection."""
    push_operation_key: str
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""
    requested_on_utc: str
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
    status: PushOperationStatus
    r"""The current status of the push operation."""
    status_code: int
    r"""Push status code."""
    changes: NotRequired[Nullable[List[PushOperationChangeTypedDict]]]
    r"""Contains a single entry that communicates which record has changed and the manner in which it changed."""
    completed_on_utc: NotRequired[str]
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
    data: NotRequired[Nullable[AccountingItemTypedDict]]
    data_type: NotRequired[DataType]
    r"""Available data types"""
    error_message: NotRequired[Nullable[str]]
    r"""A message about the error."""
    timeout_in_minutes: NotRequired[Nullable[int]]
    r"""Number of minutes the push operation must complete within before it times out."""
    timeout_in_seconds: NotRequired[Nullable[int]]
    r"""Number of seconds the push operation must complete within before it times out."""
    validation: NotRequired[ValidationTypedDict]
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""


class CreateItemResponse(BaseModel):
    company_id: Annotated[str, pydantic.Field(alias="companyId")]
    r"""Unique identifier for your SMB in Codat."""

    data_connection_key: Annotated[str, pydantic.Field(alias="dataConnectionKey")]
    r"""Unique identifier for a company's data connection."""

    push_operation_key: Annotated[str, pydantic.Field(alias="pushOperationKey")]
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""

    requested_on_utc: Annotated[str, pydantic.Field(alias="requestedOnUtc")]
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

    status: PushOperationStatus
    r"""The current status of the push operation."""

    status_code: Annotated[int, pydantic.Field(alias="statusCode")]
    r"""Push status code."""

    changes: OptionalNullable[List[PushOperationChange]] = UNSET
    r"""Contains a single entry that communicates which record has changed and the manner in which it changed."""

    completed_on_utc: Annotated[
        Optional[str], pydantic.Field(alias="completedOnUtc")
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

    data: OptionalNullable[AccountingItem] = UNSET

    data_type: Annotated[Optional[DataType], pydantic.Field(alias="dataType")] = None
    r"""Available data types"""

    error_message: Annotated[
        OptionalNullable[str], pydantic.Field(alias="errorMessage")
    ] = UNSET
    r"""A message about the error."""

    timeout_in_minutes: Annotated[
        OptionalNullable[int], pydantic.Field(alias="timeoutInMinutes")
    ] = UNSET
    r"""Number of minutes the push operation must complete within before it times out."""

    timeout_in_seconds: Annotated[
        OptionalNullable[int],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="timeoutInSeconds",
        ),
    ] = UNSET
    r"""Number of seconds the push operation must complete within before it times out."""

    validation: Optional[Validation] = None
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "changes",
            "completedOnUtc",
            "data",
            "dataType",
            "errorMessage",
            "timeoutInMinutes",
            "timeoutInSeconds",
            "validation",
        ]
        nullable_fields = [
            "changes",
            "data",
            "errorMessage",
            "timeoutInMinutes",
            "timeoutInSeconds",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
