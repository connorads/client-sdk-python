"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class UploadDirectCostAttachmentRequestBody:
    
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})

    request_body: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'requestBody' }})

    

@dataclasses.dataclass
class UploadDirectCostAttachmentRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})

    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})

    direct_cost_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'directCostId', 'style': 'simple', 'explode': False }})

    r"""Unique identifier for a direct cost"""
    request_body: Optional[UploadDirectCostAttachmentRequestBody] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }, 'request': { 'media_type': 'multipart/form-data' }})

    

@dataclasses.dataclass
class UploadDirectCostAttachmentResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    