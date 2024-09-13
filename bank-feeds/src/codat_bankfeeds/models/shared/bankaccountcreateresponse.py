"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccountstatus import BankAccountStatus
from .datatype import DataType
from .pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
from .pushoperationstatus import PushOperationStatus
from .validation import Validation, ValidationTypedDict
from codat_bankfeeds.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_bankfeeds.utils import serialize_decimal, validate_decimal
from decimal import Decimal
from enum import Enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired, deprecated


class BankAccountCreateResponseBankAccountType(str, Enum):
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """

    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"


class MetadataTypedDict(TypedDict):
    is_deleted: NotRequired[Nullable[bool]]
    r"""Indicates whether the record has been deleted in the third-party system this record originated from."""


class Metadata(BaseModel):
    is_deleted: Annotated[OptionalNullable[bool], pydantic.Field(alias="isDeleted")] = (
        UNSET
    )
    r"""Indicates whether the record has been deleted in the third-party system this record originated from."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["isDeleted"]
        nullable_fields = ["isDeleted"]
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


class SupplementalDataTypedDict(TypedDict):
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    content: NotRequired[Nullable[Dict[str, Dict[str, Any]]]]


class SupplementalData(BaseModel):
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    content: OptionalNullable[Dict[str, Dict[str, Any]]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["content"]
        nullable_fields = ["content"]
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
class AccountingBankAccountTypedDict(TypedDict):
    r"""> **Accessing Bank Accounts through Banking API**
    >
    > This datatype was originally used for accessing bank account data both in accounting integrations and open banking aggregators.
    >
    > To view bank account data through the Banking API, please refer to the new datatype [here](https://docs.codat.io/bank-feeds-api#/schemas/Account)

    > View the coverage for bank accounts in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    A list of bank accounts associated with a company and a specific data connection.

    Bank accounts data includes:
    * The name and ID of the account in the accounting software.
    * The currency and balance of the account.
    * The sort code and account number.
    """

    account_name: NotRequired[Nullable[str]]
    r"""Name of the bank account in the accounting software."""
    account_number: NotRequired[Nullable[str]]
    r"""Account number for the bank account.

    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.

    FreeAgent integrations
    For Credit accounts, only the last four digits are required. For other types, the field is optional.
    """
    account_type: NotRequired[BankAccountCreateResponseBankAccountType]
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """
    available_balance: NotRequired[Nullable[Decimal]]
    r"""Total available balance of the bank account as reported by the underlying data source. This may take into account overdrafts or pending transactions for example."""
    balance: NotRequired[Nullable[Decimal]]
    r"""Balance of the bank account."""
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    i_ban: NotRequired[Nullable[str]]
    r"""International bank account number of the account. Often used when making or receiving international payments."""
    id: NotRequired[str]
    r"""Identifier for the account, unique for the company in the accounting software."""
    institution: NotRequired[Nullable[str]]
    r"""The institution of the bank account."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    nominal_code: NotRequired[Nullable[str]]
    r"""Code used to identify each nominal account for a business."""
    overdraft_limit: NotRequired[Nullable[Decimal]]
    r"""Pre-arranged overdraft limit of the account.

    The value is always positive. For example, an overdraftLimit of `1000` means that the balance of the account can go down to `-1000`.
    """
    sort_code: NotRequired[Nullable[str]]
    r"""Sort code for the bank account.

    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """
    source_modified_date: NotRequired[str]
    status: NotRequired[BankAccountStatus]
    r"""Status of the bank account."""
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class AccountingBankAccount(BaseModel):
    r"""> **Accessing Bank Accounts through Banking API**
    >
    > This datatype was originally used for accessing bank account data both in accounting integrations and open banking aggregators.
    >
    > To view bank account data through the Banking API, please refer to the new datatype [here](https://docs.codat.io/bank-feeds-api#/schemas/Account)

    > View the coverage for bank accounts in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    A list of bank accounts associated with a company and a specific data connection.

    Bank accounts data includes:
    * The name and ID of the account in the accounting software.
    * The currency and balance of the account.
    * The sort code and account number.
    """

    account_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="accountName")
    ] = UNSET
    r"""Name of the bank account in the accounting software."""

    account_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="accountNumber")
    ] = UNSET
    r"""Account number for the bank account.

    Xero integrations
    Only a UK account number shows for bank accounts with GBP currency and a combined total of sort code and account number that equals 14 digits, For non-GBP accounts, the full bank account number is populated.

    FreeAgent integrations
    For Credit accounts, only the last four digits are required. For other types, the field is optional.
    """

    account_type: Annotated[
        Optional[BankAccountCreateResponseBankAccountType],
        pydantic.Field(alias="accountType"),
    ] = None
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """

    available_balance: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="availableBalance"),
    ] = UNSET
    r"""Total available balance of the bank account as reported by the underlying data source. This may take into account overdrafts or pending transactions for example."""

    balance: Annotated[
        OptionalNullable[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = UNSET
    r"""Balance of the bank account."""

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    i_ban: Annotated[OptionalNullable[str], pydantic.Field(alias="iBan")] = UNSET
    r"""International bank account number of the account. Often used when making or receiving international payments."""

    id: Optional[str] = None
    r"""Identifier for the account, unique for the company in the accounting software."""

    institution: OptionalNullable[str] = UNSET
    r"""The institution of the bank account."""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    nominal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="nominalCode")
    ] = UNSET
    r"""Code used to identify each nominal account for a business."""

    overdraft_limit: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="overdraftLimit"),
    ] = UNSET
    r"""Pre-arranged overdraft limit of the account.

    The value is always positive. For example, an overdraftLimit of `1000` means that the balance of the account can go down to `-1000`.
    """

    sort_code: Annotated[OptionalNullable[str], pydantic.Field(alias="sortCode")] = (
        UNSET
    )
    r"""Sort code for the bank account.

    Xero integrations
    The sort code is only displayed when the currency = GBP and the sort code and account number sum to 14 digits. For non-GBP accounts, this field is not populated.
    """

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    status: Optional[BankAccountStatus] = None
    r"""Status of the bank account."""

    supplemental_data: Annotated[
        Optional[SupplementalData], pydantic.Field(alias="supplementalData")
    ] = None
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "accountName",
            "accountNumber",
            "accountType",
            "availableBalance",
            "balance",
            "currency",
            "iBan",
            "id",
            "institution",
            "metadata",
            "modifiedDate",
            "nominalCode",
            "overdraftLimit",
            "sortCode",
            "sourceModifiedDate",
            "status",
            "supplementalData",
        ]
        nullable_fields = [
            "accountName",
            "accountNumber",
            "availableBalance",
            "balance",
            "iBan",
            "institution",
            "nominalCode",
            "overdraftLimit",
            "sortCode",
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


class BankAccountCreateResponseTypedDict(TypedDict):
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
    data: NotRequired[Nullable[AccountingBankAccountTypedDict]]
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


class BankAccountCreateResponse(BaseModel):
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

    data: OptionalNullable[AccountingBankAccount] = UNSET

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
