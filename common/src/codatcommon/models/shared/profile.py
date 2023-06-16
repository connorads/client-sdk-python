"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatcommon import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Profile:
    r"""Describes your Codat client instance"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    redirect_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirectUrl') }})
    alert_auth_header: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alertAuthHeader'), 'exclude': lambda f: f is None }})
    api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKey'), 'exclude': lambda f: f is None }})
    r"""Deprecated: this field will be removed in a future release, please migrate away from it as soon as possible"""
    confirm_company_name: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confirmCompanyName'), 'exclude': lambda f: f is None }})
    r"""Deprecated: this field will be removed in a future release, please migrate away from it as soon as possible"""
    icon_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iconUrl'), 'exclude': lambda f: f is None }})
    logo_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logoUrl'), 'exclude': lambda f: f is None }})
    white_list_urls: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('whiteListUrls'), 'exclude': lambda f: f is None }})
    

