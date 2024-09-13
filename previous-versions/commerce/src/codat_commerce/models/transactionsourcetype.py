"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class TransactionSourceType(str, Enum):
    r"""The type of source the transaction arose."""

    FEE = "Fee"
    ORDER = "Order"
    PAYMENT = "Payment"
    SERVICE_CHARGE = "ServiceCharge"
    UNKNOWN = "Unknown"
