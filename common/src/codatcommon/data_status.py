"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codatcommon.models import operations, shared
from typing import Optional

class DataStatus:
    r"""Understand the state of data within Codat."""
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
        
    def get_company_data_history(self, request: operations.GetCompanyDataHistoryRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCompanyDataHistoryResponse:
        r"""Get pull operations
        Gets the pull operation history (datasets) for a given company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCompanyDataHistoryRequest, base_url, '/companies/{companyId}/data/history', request)
        
        query_params = utils.get_query_params(operations.GetCompanyDataHistoryRequest, request)
        
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

        res = operations.GetCompanyDataHistoryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DataConnectionHistory])
                res.data_connection_history = out
        elif http_res.status_code in [400, 401, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out

        return res

    def get_company_data_status(self, request: operations.GetCompanyDataStatusRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCompanyDataStatusResponse:
        r"""Get data status
        Get the state of each data type for a company
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCompanyDataStatusRequest, base_url, '/companies/{companyId}/dataStatus', request)
        
        
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

        res = operations.GetCompanyDataStatusResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, shared.DataStatus]])
                res.data_status_response = out
        elif http_res.status_code in [401, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out

        return res

    def get_pull_operation(self, request: operations.GetPullOperationRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetPullOperationResponse:
        r"""Get pull operation
        Retrieve information about a single dataset or pull operation.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetPullOperationRequest, base_url, '/companies/{companyId}/data/history/{datasetId}', request)
        
        
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

        res = operations.GetPullOperationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PullOperation])
                res.pull_operation = out
        elif http_res.status_code in [401, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out

        return res

    