"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class ProjectRefTypedDict(TypedDict):
    id: str
    r"""Unique identifier to the project reference."""
    name: NotRequired[Nullable[str]]
    r"""The project's name."""
    

class ProjectRef(BaseModel):
    id: str
    r"""Unique identifier to the project reference."""
    name: OptionalNullable[str] = UNSET
    r"""The project's name."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name"]
        nullable_fields = ["name"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
