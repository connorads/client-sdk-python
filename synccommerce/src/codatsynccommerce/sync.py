"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codatsynccommerce.models import operations, shared
from typing import Optional

class Sync:
    r"""Initiate a sync of Sync for Commerce company data into their respective accounting software."""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def request_sync(self, request: operations.RequestSyncRequest, retries: Optional[utils.RetryConfig] = None) -> operations.RequestSyncResponse:
        r"""Run a Commerce sync from the last successful sync
        Run a Commerce sync from the last successful sync up to the date provided (optional), otherwise UtcNow is used.
        If there was no previously successful sync, the start date in the config is used.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RequestSyncRequest, base_url, '/companies/{companyId}/sync/commerce/latest', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "sync_to_latest_args", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('POST', url, data=data, files=form, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.RequestSyncResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SyncSummary])
                res.sync_summary = out

        return res

    
    def request_sync_for_date_range(self, request: operations.RequestSyncForDateRangeRequest, retries: Optional[utils.RetryConfig] = None) -> operations.RequestSyncForDateRangeResponse:
        r"""Run a Commerce sync from a given date range
        Run a Commerce sync from the specified start date to the specified finish date in the request payload.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RequestSyncForDateRangeRequest, base_url, '/meta/companies/{companyId}/sync/commerce/historic', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "date_range", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('POST', url, data=data, files=form, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.RequestSyncForDateRangeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SyncSummary])
                res.sync_summary = out

        return res

    