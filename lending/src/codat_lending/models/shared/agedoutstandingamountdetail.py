"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AgedOutstandingAmountDetailTypedDict(TypedDict):
    amount: NotRequired[Decimal]
    r"""The amount outstanding."""
    name: NotRequired[str]
    r"""Name of data type with outstanding amount for given period."""


class AgedOutstandingAmountDetail(BaseModel):
    amount: Annotated[
        Optional[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = None
    r"""The amount outstanding."""

    name: Optional[str] = None
    r"""Name of data type with outstanding amount for given period."""
