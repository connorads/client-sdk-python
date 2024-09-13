"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_assess.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class LendingCustomerRefTypedDict(TypedDict):
    customer_name: NotRequired[Nullable[str]]
    r"""`customerName` from the Customer data type."""
    id: NotRequired[str]
    r"""`id` from the Customers data type."""


class LendingCustomerRef(BaseModel):
    customer_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="customerName")
    ] = UNSET
    r"""`customerName` from the Customer data type."""

    id: Optional[str] = None
    r"""`id` from the Customers data type."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["customerName", "id"]
        nullable_fields = ["customerName"]
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
