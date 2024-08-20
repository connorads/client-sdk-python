"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountingcustomerref import AccountingCustomerRef, AccountingCustomerRefTypedDict
from .billedtotype1 import BilledToType1
from .projectref import ProjectRef, ProjectRefTypedDict
from .trackingcategoryref import TrackingCategoryRef, TrackingCategoryRefTypedDict
from codat_lending.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RecordReferenceTypedDict(TypedDict):
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    
    data_type: NotRequired[str]
    r"""Allowed name of the 'dataType'."""
    id: NotRequired[str]
    r"""'id' of the underlying record or data type."""
    

class RecordReference(BaseModel):
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    
    data_type: Annotated[Optional[str], pydantic.Field(alias="dataType")] = None
    r"""Allowed name of the 'dataType'."""
    id: Optional[str] = None
    r"""'id' of the underlying record or data type."""
    

class AccountsReceivableTrackingTypedDict(TypedDict):
    r"""Categories, and a project and customer, against which the item is tracked."""
    
    category_refs: List[TrackingCategoryRefTypedDict]
    is_billed_to: BilledToType1
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    is_rebilled_to: BilledToType1
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    customer_ref: NotRequired[AccountingCustomerRefTypedDict]
    project_ref: NotRequired[ProjectRefTypedDict]
    record_ref: NotRequired[RecordReferenceTypedDict]
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    

class AccountsReceivableTracking(BaseModel):
    r"""Categories, and a project and customer, against which the item is tracked."""
    
    category_refs: Annotated[List[TrackingCategoryRef], pydantic.Field(alias="categoryRefs")]
    is_billed_to: Annotated[BilledToType1, pydantic.Field(alias="isBilledTo")]
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    is_rebilled_to: Annotated[BilledToType1, pydantic.Field(alias="isRebilledTo")]
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    customer_ref: Annotated[Optional[AccountingCustomerRef], pydantic.Field(alias="customerRef")] = None
    project_ref: Annotated[Optional[ProjectRef], pydantic.Field(alias="projectRef")] = None
    record_ref: Annotated[Optional[RecordReference], pydantic.Field(alias="recordRef")] = None
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    
