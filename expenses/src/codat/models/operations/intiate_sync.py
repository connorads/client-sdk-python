"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import codaterrormessage as shared_codaterrormessage
from ..shared import postsync as shared_postsync
from ..shared import syncinitiated as shared_syncinitiated
from typing import Optional


@dataclasses.dataclass
class IntiateSyncRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    post_sync: Optional[shared_postsync.PostSync] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class IntiateSyncResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    codat_error_message: Optional[shared_codaterrormessage.CodatErrorMessage] = dataclasses.field(default=None)
    r"""If model is incorrect"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    sync_initiated: Optional[shared_syncinitiated.SyncInitiated] = dataclasses.field(default=None)
    r"""Returns the newly created SyncId"""  
    