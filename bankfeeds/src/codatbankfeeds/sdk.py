"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codatbankfeeds.models import operations, shared
from typing import Optional

SERVERS = [
    "https://api.codat.io",
    r"""Production"""
]
"""Contains the list of servers available to the SDK"""

class CodatBankFeeds:
    r"""Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting platforms.
    
    A bank feed is a connection between a source bank account—in your application—and a target bank account in a supported accounting package.
    
    [Read more...](https://docs.codat.io/bank-feeds-api/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas)
    """

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.20.1"
    _gen_version: str = "2.31.0"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        
    
    
    
    def create_bank_feed(self, request: operations.CreateBankFeedRequest, retries: Optional[utils.RetryConfig] = None) -> operations.CreateBankFeedResponse:
        r"""Create bank feed bank accounts
        Put BankFeed BankAccounts for a single data source connected to a single company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateBankFeedRequest, base_url, '/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('PUT', url, data=data, files=form, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBankFeedResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.BankFeedAccount]])
                res.bank_feed_accounts = out

        return res

    
    def create_bank_transactions(self, request: operations.CreateBankTransactionsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.CreateBankTransactionsResponse:
        r"""Create bank transactions
        Posts bank transactions to the accounting package for a given company.
        
        > **Supported Integrations**
        > 
        > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support POST methods.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateBankTransactionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/bankAccounts/{accountId}/bankTransactions', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bank_transactions", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateBankTransactionsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBankTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateBankTransactionsResponse])
                res.create_bank_transactions_response = out

        return res

    
    def get_bank_feeds(self, request: operations.GetBankFeedsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetBankFeedsResponse:
        r"""List bank feed bank accounts
        Get BankFeed BankAccounts for a single data source connected to a single company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBankFeedsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts', request)
        headers = {}
        headers['Accept'] = 'application/json'
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

        res = operations.GetBankFeedsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.BankFeedAccount]])
                res.bank_feed_accounts = out

        return res

    
    def get_create_bank_account_model(self, request: operations.GetCreateBankAccountModelRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCreateBankAccountModelResponse:
        r"""List push options for bank account bank transactions
        Gets the options of pushing bank account transactions.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateBankAccountModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/bankAccounts/{accountId}/bankTransactions', request)
        headers = {}
        headers['Accept'] = 'application/json'
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

        res = operations.GetCreateBankAccountModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PushOption])
                res.push_option = out

        return res

    
    def list_bank_account_transactions(self, request: operations.ListBankAccountTransactionsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListBankAccountTransactionsResponse:
        r"""List bank transactions for bank account
        Gets bank transactions for a given bank account ID
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListBankAccountTransactionsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}/bankTransactions', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListBankAccountTransactionsRequest, request)
        headers['Accept'] = 'application/json'
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

        res = operations.ListBankAccountTransactionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BankTransactionsResponse])
                res.bank_transactions_response = out

        return res

    
    def update_bank_feed(self, request: operations.UpdateBankFeedRequest, retries: Optional[utils.RetryConfig] = None) -> operations.UpdateBankFeedResponse:
        r"""Update bank feed bank account
        Update a single BankFeed BankAccount for a single data source connected to a single company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateBankFeedRequest, base_url, '/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts/{accountId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bank_feed_account", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
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

        res = operations.UpdateBankFeedResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BankFeedAccount])
                res.bank_feed_account = out

        return res

    