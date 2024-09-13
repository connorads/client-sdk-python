"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_accounting.models.shared import item as shared_item
from codat_accounting.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_accounting.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateItemRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    item: NotRequired[Nullable[shared_item.ItemTypedDict]]
    timeout_in_minutes: NotRequired[int]
    r"""Time limit for the push operation to complete before it is timed out."""


class CreateItemRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    connection_id: Annotated[
        str,
        pydantic.Field(alias="connectionId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a connection."""

    item: Annotated[
        OptionalNullable[shared_item.Item],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = UNSET

    timeout_in_minutes: Annotated[
        Optional[int],
        pydantic.Field(alias="timeoutInMinutes"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Time limit for the push operation to complete before it is timed out."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["Item", "timeoutInMinutes"]
        nullable_fields = ["Item"]
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
