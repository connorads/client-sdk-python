"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from typing import Dict, List, Optional, TypedDict
from typing_extensions import NotRequired


class CommerceReportErrorTypedDict(TypedDict):
    details: NotRequired[Dict[str, List[str]]]
    r"""Additional details on the error."""
    message: NotRequired[str]
    r"""Message returned by error."""
    type: NotRequired[str]
    r"""The type of error."""
    

class CommerceReportError(BaseModel):
    details: Optional[Dict[str, List[str]]] = None
    r"""Additional details on the error."""
    message: Optional[str] = None
    r"""Message returned by error."""
    type: Optional[str] = None
    r"""The type of error."""
    
