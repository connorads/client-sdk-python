"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
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
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateBankAccountTransactionTypedDict(TypedDict):
    amount: NotRequired[Decimal]
    r"""The amount transacted in the bank transaction."""
    balance: NotRequired[Decimal]
    r"""The remaining balance in the account with ID `accountId`."""
    date_: NotRequired[str]
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
    description: NotRequired[Nullable[str]]
    r"""Description of the bank transaction."""
    id: NotRequired[str]
    r"""Identifier for the bank account transaction, unique for the company in the accounting software."""


class CreateBankAccountTransaction(BaseModel):
    amount: Annotated[
        Optional[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = None
    r"""The amount transacted in the bank transaction."""

    balance: Annotated[
        Optional[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = None
    r"""The remaining balance in the account with ID `accountId`."""

    date_: Annotated[Optional[str], pydantic.Field(alias="date")] = None
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

    description: OptionalNullable[str] = UNSET
    r"""Description of the bank transaction."""

    id: Optional[str] = None
    r"""Identifier for the bank account transaction, unique for the company in the accounting software."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["amount", "balance", "date", "description", "id"]
        nullable_fields = ["description"]
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
