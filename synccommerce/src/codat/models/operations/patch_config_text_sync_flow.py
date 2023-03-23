"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchConfigTextSyncFlowRequestBodyAdditionalProp1:
    r"""Placeholder for the property name."""
    
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})  
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Value of the property."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchConfigTextSyncFlowRequestBodyAdditionalProp2:
    r"""Placeholder for the property name."""
    
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})  
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Value of the property."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchConfigTextSyncFlowRequestBodyAdditionalProp3:
    r"""Placeholder for the property name."""
    
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})  
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Value of the property."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchConfigTextSyncFlowRequestBody:
    
    additional_prop1: Optional[PatchConfigTextSyncFlowRequestBodyAdditionalProp1] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProp1'), 'exclude': lambda f: f is None }})
    r"""Placeholder for the property name."""  
    additional_prop2: Optional[PatchConfigTextSyncFlowRequestBodyAdditionalProp2] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProp2'), 'exclude': lambda f: f is None }})
    r"""Placeholder for the property name."""  
    additional_prop3: Optional[PatchConfigTextSyncFlowRequestBodyAdditionalProp3] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProp3'), 'exclude': lambda f: f is None }})
    r"""Placeholder for the property name."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchConfigTextSyncFlow200ApplicationJSONAdditionalProp1:
    r"""Placeholder for the property name."""
    
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})  
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Value of the property."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchConfigTextSyncFlow200ApplicationJSONAdditionalProp2:
    r"""Placeholder for the property name."""
    
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})  
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Value of the property."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchConfigTextSyncFlow200ApplicationJSONAdditionalProp3:
    r"""Placeholder for the property name."""
    
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})  
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Value of the property."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchConfigTextSyncFlow200ApplicationJSON:
    r"""Success"""
    
    additional_prop1: Optional[PatchConfigTextSyncFlow200ApplicationJSONAdditionalProp1] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProp1'), 'exclude': lambda f: f is None }})
    r"""Placeholder for the property name."""  
    additional_prop2: Optional[PatchConfigTextSyncFlow200ApplicationJSONAdditionalProp2] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProp2'), 'exclude': lambda f: f is None }})
    r"""Placeholder for the property name."""  
    additional_prop3: Optional[PatchConfigTextSyncFlow200ApplicationJSONAdditionalProp3] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalProp3'), 'exclude': lambda f: f is None }})
    r"""Placeholder for the property name."""  
    

@dataclasses.dataclass
class PatchConfigTextSyncFlowResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    patch_config_text_sync_flow_200_application_json_object: Optional[PatchConfigTextSyncFlow200ApplicationJSON] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    