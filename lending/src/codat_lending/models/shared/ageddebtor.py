"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .agedcurrencyoutstanding import (
    AgedCurrencyOutstanding,
    AgedCurrencyOutstandingTypedDict,
)
from codat_lending.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AgedDebtorTypedDict(TypedDict):
    aged_currency_outstanding: NotRequired[List[AgedCurrencyOutstandingTypedDict]]
    r"""Array of aged debtors by currency."""
    customer_id: NotRequired[str]
    r"""Customer ID of the aged debtor."""
    customer_name: NotRequired[str]
    r"""Customer name of the aged debtor."""


class AgedDebtor(BaseModel):
    aged_currency_outstanding: Annotated[
        Optional[List[AgedCurrencyOutstanding]],
        pydantic.Field(alias="agedCurrencyOutstanding"),
    ] = None
    r"""Array of aged debtors by currency."""

    customer_id: Annotated[Optional[str], pydantic.Field(alias="customerId")] = None
    r"""Customer ID of the aged debtor."""

    customer_name: Annotated[Optional[str], pydantic.Field(alias="customerName")] = None
    r"""Customer name of the aged debtor."""
