"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import brandingimage as shared_brandingimage
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BrandingLogo:
    r"""Logo branding references."""
    
    full: Optional[shared_brandingimage.BrandingImage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full'), 'exclude': lambda f: f is None }})

    square: Optional[shared_brandingimage.BrandingImage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('square'), 'exclude': lambda f: f is None }})

    