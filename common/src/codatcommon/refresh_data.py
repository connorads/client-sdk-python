"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codatcommon.models import operations, shared
from typing import Optional

class RefreshData:
    r"""Queue pull operations to refresh data in Codat."""
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
        
    
    def all(self, request: operations.RefreshCompanyDataRequest, retries: Optional[utils.RetryConfig] = None) -> operations.RefreshCompanyDataResponse:
        r"""Queue pull operations
        Refreshes all data types marked Fetch on first link.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RefreshCompanyDataRequest, base_url, '/companies/{companyId}/data/all', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('POST', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.RefreshCompanyDataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [401, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out

        return res

    
    def by_data_type(self, request: operations.CreatePullOperationRequest, retries: Optional[utils.RetryConfig] = None) -> operations.CreatePullOperationResponse:
        r"""Queue pull operation
        Queue a single pull operation for the given company and data type.
        
        This will bring updated data into Codat from the linked integration for you to view.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreatePullOperationRequest, base_url, '/companies/{companyId}/data/queue/{dataType}', request)
        headers = {}
        query_params = utils.get_query_params(operations.CreatePullOperationRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('POST', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreatePullOperationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PullOperation])
                res.pull_operation = out
        elif http_res.status_code in [401, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out

        return res

    