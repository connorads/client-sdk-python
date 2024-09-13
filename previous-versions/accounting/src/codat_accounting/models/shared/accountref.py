"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_accounting.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class AccountRefTypedDict(TypedDict):
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""

    id: NotRequired[str]
    r"""'id' from the Accounts data type."""
    name: NotRequired[str]
    r"""'name' from the Accounts data type."""


class AccountRef(BaseModel):
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""

    id: Optional[str] = None
    r"""'id' from the Accounts data type."""

    name: Optional[str] = None
    r"""'name' from the Accounts data type."""
