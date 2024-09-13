"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_commerce.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ProductVariantRefTypedDict(TypedDict):
    r"""Reference that links the line item to the specific version of product that has been ordered."""

    id: str
    r"""The unique identifier of the product variant being referenced."""
    name: NotRequired[str]
    r"""Name of the product variant being referenced."""


class ProductVariantRef(BaseModel):
    r"""Reference that links the line item to the specific version of product that has been ordered."""

    id: str
    r"""The unique identifier of the product variant being referenced."""

    name: Optional[str] = None
    r"""Name of the product variant being referenced."""
