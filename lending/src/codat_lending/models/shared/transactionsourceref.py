"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .transactionsourcetype import TransactionSourceType
from codat_lending.types import BaseModel
from typing import TypedDict


class TransactionSourceRefTypedDict(TypedDict):
    id: str
    r"""The unique identitifer of the record being referenced"""
    type: TransactionSourceType
    r"""The type of source the transaction arose."""


class TransactionSourceRef(BaseModel):
    id: str
    r"""The unique identitifer of the record being referenced"""

    type: TransactionSourceType
    r"""The type of source the transaction arose."""
