"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class PaymentMethodRefTypedDict(TypedDict):
    r"""The payment method the record is linked to in the accounting or commerce software."""

    id: str
    r"""The unique identifier of the location being referenced."""
    name: NotRequired[str]
    r"""Name of the location being referenced."""


class PaymentMethodRef(BaseModel):
    r"""The payment method the record is linked to in the accounting or commerce software."""

    id: str
    r"""The unique identifier of the location being referenced."""

    name: Optional[str] = None
    r"""Name of the location being referenced."""
