"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .agedoutstandingamount import AgedOutstandingAmount, AgedOutstandingAmountTypedDict
from codat_accounting.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AgedCurrencyOutstandingItemsTypedDict(TypedDict):
    aged_outstanding_amounts: NotRequired[List[AgedOutstandingAmountTypedDict]]
    r"""Array of outstanding amounts by period."""
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """


class AgedCurrencyOutstandingItems(BaseModel):
    aged_outstanding_amounts: Annotated[
        Optional[List[AgedOutstandingAmount]],
        pydantic.Field(alias="agedOutstandingAmounts"),
    ] = None
    r"""Array of outstanding amounts by period."""

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
