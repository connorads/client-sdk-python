"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class AccountIdentifierTypeEnum(str, Enum):
    r"""Type of account"""
    ACCOUNT = "Account"
    CARD = "Card"
    CREDIT = "Credit"
    DEPOSITORY = "Depository"
    INVESTMENT = "Investment"
    LOAN = "Loan"
    OTHER = "Other"
