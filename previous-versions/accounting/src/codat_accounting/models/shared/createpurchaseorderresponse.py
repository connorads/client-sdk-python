"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .datatype import DataType
from .metadata import Metadata, MetadataTypedDict
from .purchaseorderlineitem import PurchaseOrderLineItem, PurchaseOrderLineItemTypedDict
from .purchaseorderstatus import PurchaseOrderStatus
from .pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
from .pushoperationstatus import PushOperationStatus
from .shipto import ShipTo, ShipToTypedDict
from .supplierref import SupplierRef, SupplierRefTypedDict
from .validation import Validation, ValidationTypedDict
from codat_accounting.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_accounting.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired, deprecated


class CreatePurchaseOrderResponseUserTypedDict(TypedDict):
    r"""The user who created the purchase order in the accounting system"""

    email: NotRequired[Nullable[str]]
    r"""Email address of the user."""
    first_name: NotRequired[Nullable[str]]
    r"""First name of the user."""
    last_name: NotRequired[Nullable[str]]
    r"""Last name of the user."""


class CreatePurchaseOrderResponseUser(BaseModel):
    r"""The user who created the purchase order in the accounting system"""

    email: OptionalNullable[str] = UNSET
    r"""Email address of the user."""

    first_name: Annotated[OptionalNullable[str], pydantic.Field(alias="firstName")] = (
        UNSET
    )
    r"""First name of the user."""

    last_name: Annotated[OptionalNullable[str], pydantic.Field(alias="lastName")] = (
        UNSET
    )
    r"""Last name of the user."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["email", "firstName", "lastName"]
        nullable_fields = ["email", "firstName", "lastName"]
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


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class AccountingPurchaseOrderTypedDict(TypedDict):
    r"""> View the coverage for purchase orders in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    Purchase orders represent a business's intent to purchase goods or services from a supplier and normally include information such as expected delivery dates and shipping details.

    This information can be used to provide visibility on a business's expected payables and to track a purchase through the full procurement process.
    """

    created_by: NotRequired[CreatePurchaseOrderResponseUserTypedDict]
    r"""The user who created the purchase order in the accounting system"""
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    currency_rate: NotRequired[Nullable[Decimal]]
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting software, it will be available from Codat with the same precision (up to a maximum of 9 decimal places).

    For accounting software which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

    ## Examples with base currency of GBP

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |

    ## Examples with base currency of USD

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, specify a currencyRate in the request body.  |
    """
    delivery_date: NotRequired[str]
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
    expected_delivery_date: NotRequired[str]
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
    id: NotRequired[str]
    r"""Identifier for the purchase order, unique for the company in the accounting software."""
    issue_date: NotRequired[str]
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
    line_items: NotRequired[Nullable[List[PurchaseOrderLineItemTypedDict]]]
    r"""Array of line items."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    note: NotRequired[Nullable[str]]
    r"""Any additional information associated with the purchase order."""
    payment_due_date: NotRequired[str]
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
    purchase_order_number: NotRequired[Nullable[str]]
    r"""Friendly reference for the purchase order, commonly generated by the accounting software."""
    ship_to: NotRequired[ShipToTypedDict]
    r"""Delivery details for any goods that have been ordered."""
    source_modified_date: NotRequired[str]
    status: NotRequired[PurchaseOrderStatus]
    r"""Current state of the purchase order"""
    sub_total: NotRequired[Decimal]
    r"""Total amount of the purchase order, including discounts but excluding tax."""
    supplier_ref: NotRequired[SupplierRefTypedDict]
    r"""Reference to the supplier the record relates to."""
    total_amount: NotRequired[Decimal]
    r"""Total amount of the purchase order, including discounts and tax."""
    total_discount: NotRequired[Decimal]
    r"""Total value of any discounts applied to the purchase order."""
    total_tax_amount: NotRequired[Decimal]
    r"""
    Total amount of tax included in the purchase order.
    """


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class AccountingPurchaseOrder(BaseModel):
    r"""> View the coverage for purchase orders in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    Purchase orders represent a business's intent to purchase goods or services from a supplier and normally include information such as expected delivery dates and shipping details.

    This information can be used to provide visibility on a business's expected payables and to track a purchase through the full procurement process.
    """

    created_by: Annotated[
        Optional[CreatePurchaseOrderResponseUser], pydantic.Field(alias="createdBy")
    ] = None
    r"""The user who created the purchase order in the accounting system"""

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    currency_rate: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="currencyRate"),
    ] = UNSET
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting software, it will be available from Codat with the same precision (up to a maximum of 9 decimal places).

    For accounting software which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

    ## Examples with base currency of GBP

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |

    ## Examples with base currency of USD

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, specify a currencyRate in the request body.  |
    """

    delivery_date: Annotated[Optional[str], pydantic.Field(alias="deliveryDate")] = None
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

    expected_delivery_date: Annotated[
        Optional[str], pydantic.Field(alias="expectedDeliveryDate")
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

    id: Optional[str] = None
    r"""Identifier for the purchase order, unique for the company in the accounting software."""

    issue_date: Annotated[Optional[str], pydantic.Field(alias="issueDate")] = None
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

    line_items: Annotated[
        OptionalNullable[List[PurchaseOrderLineItem]], pydantic.Field(alias="lineItems")
    ] = UNSET
    r"""Array of line items."""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    note: OptionalNullable[str] = UNSET
    r"""Any additional information associated with the purchase order."""

    payment_due_date: Annotated[
        Optional[str], pydantic.Field(alias="paymentDueDate")
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

    purchase_order_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="purchaseOrderNumber")
    ] = UNSET
    r"""Friendly reference for the purchase order, commonly generated by the accounting software."""

    ship_to: Annotated[Optional[ShipTo], pydantic.Field(alias="shipTo")] = None
    r"""Delivery details for any goods that have been ordered."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    status: Optional[PurchaseOrderStatus] = None
    r"""Current state of the purchase order"""

    sub_total: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="subTotal"),
    ] = None
    r"""Total amount of the purchase order, including discounts but excluding tax."""

    supplier_ref: Annotated[
        Optional[SupplierRef], pydantic.Field(alias="supplierRef")
    ] = None
    r"""Reference to the supplier the record relates to."""

    total_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalAmount"),
    ] = None
    r"""Total amount of the purchase order, including discounts and tax."""

    total_discount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalDiscount"),
    ] = None
    r"""Total value of any discounts applied to the purchase order."""

    total_tax_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalTaxAmount"),
    ] = None
    r"""
    Total amount of tax included in the purchase order.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "createdBy",
            "currency",
            "currencyRate",
            "deliveryDate",
            "expectedDeliveryDate",
            "id",
            "issueDate",
            "lineItems",
            "metadata",
            "modifiedDate",
            "note",
            "paymentDueDate",
            "purchaseOrderNumber",
            "shipTo",
            "sourceModifiedDate",
            "status",
            "subTotal",
            "supplierRef",
            "totalAmount",
            "totalDiscount",
            "totalTaxAmount",
        ]
        nullable_fields = ["currencyRate", "lineItems", "note", "purchaseOrderNumber"]
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


class CreatePurchaseOrderResponseTypedDict(TypedDict):
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
    data: NotRequired[Nullable[AccountingPurchaseOrderTypedDict]]
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


class CreatePurchaseOrderResponse(BaseModel):
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

    data: OptionalNullable[AccountingPurchaseOrder] = UNSET

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
