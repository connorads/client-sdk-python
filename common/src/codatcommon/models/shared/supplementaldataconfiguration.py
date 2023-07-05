"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatcommon import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SupplementalDataConfiguration:
    r"""The client's defined name for the object."""
    data_source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataSource'), 'exclude': lambda f: f is None }})
    r"""The underlying endpoint of the source system which the configuration is targeting."""
    pull_data: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pullData'), 'exclude': lambda f: f is None }})
    r"""The additional properties that are required when pulling records."""
    push_data: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pushData'), 'exclude': lambda f: f is None }})
    r"""The additional properties that are required to create and/or update records."""
    

