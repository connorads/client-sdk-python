"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codatassess.models import operations, shared
from typing import Optional

class Categories:
    r"""Categorisation"""
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
        
    
    def get_account_category(self, request: operations.GetAccountCategoryRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetAccountCategoryResponse:
        r"""Get suggested and/or confirmed category for a specific account
        Get category for specific nominal account.
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAccountCategoryRequest, base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/accounts/{accountId}/categories', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountCategoryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CategorisedAccount])
                res.categorised_account = out

        return res

    
    def list_accounts_categories(self, request: operations.ListAccountsCategoriesRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListAccountsCategoriesResponse:
        r"""List suggested and confirmed account categories
        Lists suggested and confirmed chart of account categories for the given company and data connection.
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListAccountsCategoriesRequest, base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/accounts/categories', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListAccountsCategoriesRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAccountsCategoriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CategorisedAccounts])
                res.categorised_accounts = out

        return res

    
    def list_available_account_categories(self, retries: Optional[utils.RetryConfig] = None) -> operations.ListAvailableAccountCategoriesResponse:
        r"""List account categories
        Lists available account categories Codat's categorisation engine can provide.
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/data/assess/accounts/categories'
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAvailableAccountCategoriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.Categories]])
                res.categories = out

        return res

    
    def update_account_category(self, request: operations.UpdateAccountCategoryRequest, retries: Optional[utils.RetryConfig] = None) -> operations.UpdateAccountCategoryResponse:
        r"""Patch account categories
        Update category for a specific nominal account
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateAccountCategoryRequest, base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/accounts/{accountId}/categories', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "confirm_category", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('PATCH', url, data=data, files=form, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateAccountCategoryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CategorisedAccount])
                res.categorised_account = out

        return res

    
    def update_accounts_categories(self, request: operations.UpdateAccountsCategoriesRequest, retries: Optional[utils.RetryConfig] = None) -> operations.UpdateAccountsCategoriesResponse:
        r"""Confirm categories for accounts
        Comfirms the categories for all or a batch of accounts for a specific connection.
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateAccountsCategoriesRequest, base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/accounts/categories', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "confirm_categories", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('PATCH', url, data=data, files=form, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateAccountsCategoriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.CategorisedAccount]])
                res.categorised_accounts = out

        return res

    