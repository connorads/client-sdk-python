"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codatfiles.models import operations, shared
from typing import Optional

class Files:
    r"""Endpoints to manage uploaded files."""
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
        
    def download_files(self, request: operations.DownloadFilesRequest, retries: Optional[utils.RetryConfig] = None) -> operations.DownloadFilesResponse:
        r"""Download all files for a company
        You can specify a date to download specific files for.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DownloadFilesRequest, base_url, '/companies/{companyId}/files/download', request)
        
        query_params = utils.get_query_params(operations.DownloadFilesRequest, request)
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, params=query_params)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.DownloadFilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/octet-stream'):
                res.data = http_res.content

        return res

    def list_files(self, request: operations.ListFilesRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListFilesResponse:
        r"""List all files uploaded by a company
        Returns an array of files that have been uploaded for a given company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListFilesRequest, base_url, '/companies/{companyId}/files', request)
        
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListFilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.File]])
                res.files = out

        return res

    def upload_files(self, request: operations.UploadFilesRequest, retries: Optional[utils.RetryConfig] = None) -> operations.UploadFilesResponse:
        r"""Upload files for a company
        Upload files
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UploadFilesRequest, base_url, '/companies/{companyId}/connections/{connectionId}/files', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'multipart')
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

        res = operations.UploadFilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    