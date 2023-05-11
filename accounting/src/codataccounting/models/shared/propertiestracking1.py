"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import billedtotype_enum1 as shared_billedtotype_enum1
from ..shared import customerref as shared_customerref
from ..shared import projectref as shared_projectref
from ..shared import trackingcategoryref as shared_trackingcategoryref
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Propertiestracking1:
    r"""Categories, and a project and customer, against which the item is tracked."""
    
    category_refs: list[shared_trackingcategoryref.TrackingCategoryRef] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categoryRefs') }})
    is_billed_to: shared_billedtotype_enum1.BilledToTypeEnum1 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBilledTo') }})
    is_rebilled_to: shared_billedtotype_enum1.BilledToTypeEnum1 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRebilledTo') }})
    customer_ref: Optional[shared_customerref.CustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[shared_projectref.ProjectRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectRef'), 'exclude': lambda f: f is None }})
    