"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DataIntegrityByAmountTypedDict(TypedDict):
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    match_percentage: NotRequired[Decimal]
    r"""The percentage of the absolute value of transactions of the type specified in the route which have a match."""
    matched: NotRequired[Decimal]
    r"""The sum of the absolute value of transactions of the type specified in the route which have a match."""
    total: NotRequired[Decimal]
    r"""The total of unmatched and matched."""
    unmatched: NotRequired[Decimal]
    r"""The sum of the absolute value of transactions of the type specified in the route which don't have a match."""
    

class DataIntegrityByAmount(BaseModel):
    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    match_percentage: Annotated[Annotated[Optional[Decimal], BeforeValidator(validate_decimal), PlainSerializer(serialize_decimal(False))], pydantic.Field(alias="matchPercentage")] = None
    r"""The percentage of the absolute value of transactions of the type specified in the route which have a match."""
    matched: Annotated[Optional[Decimal], BeforeValidator(validate_decimal), PlainSerializer(serialize_decimal(False))] = None
    r"""The sum of the absolute value of transactions of the type specified in the route which have a match."""
    total: Annotated[Optional[Decimal], BeforeValidator(validate_decimal), PlainSerializer(serialize_decimal(False))] = None
    r"""The total of unmatched and matched."""
    unmatched: Annotated[Optional[Decimal], BeforeValidator(validate_decimal), PlainSerializer(serialize_decimal(False))] = None
    r"""The sum of the absolute value of transactions of the type specified in the route which don't have a match."""
    
