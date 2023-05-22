"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codataccounting.models import operations, shared
from typing import Optional

class BillCreditNotes:
    r"""Bill credit notes"""
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
        
    
    def create(self, request: operations.CreateBillCreditNoteRequest, retries: Optional[utils.RetryConfig] = None) -> operations.CreateBillCreditNoteResponse:
        r"""Create bill credit note
        Posts a new billCreditNote to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).
        
        > **Supported Integrations**
        > 
        > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating bill credit notes.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateBillCreditNoteRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/billCreditNotes', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bill_credit_note", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateBillCreditNoteRequest, request)
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

        res = operations.CreateBillCreditNoteResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateBillCreditNoteResponse])
                res.create_bill_credit_note_response = out

        return res

    
    def get(self, request: operations.GetBillCreditNoteRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetBillCreditNoteResponse:
        r"""Get bill credit note
        Gets a single billCreditNote corresponding to the given ID.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetBillCreditNoteRequest, base_url, '/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}', request)
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

        res = operations.GetBillCreditNoteResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BillCreditNote])
                res.bill_credit_note = out

        return res

    
    def get_create_update_model(self, request: operations.GetCreateUpdateBillCreditNotesModelRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCreateUpdateBillCreditNotesModelResponse:
        r"""Get create/update bill credit note model
        Get create/update bill credit note model.
        
        > **Supported Integrations**
        > 
        > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating and updating bill credit notes.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateUpdateBillCreditNotesModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/billCreditNotes', request)
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

        res = operations.GetCreateUpdateBillCreditNotesModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PushOption])
                res.push_option = out

        return res

    
    def list(self, request: operations.ListBillCreditNotesRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListBillCreditNotesResponse:
        r"""List bill credit notes
        Gets a list of all bill credit notes for a company, with pagination.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListBillCreditNotesRequest, base_url, '/companies/{companyId}/data/billCreditNotes', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListBillCreditNotesRequest, request)
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

        res = operations.ListBillCreditNotesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BillCreditNotes])
                res.bill_credit_notes = out

        return res

    
    def update(self, request: operations.UpdateBillCreditNoteRequest, retries: Optional[utils.RetryConfig] = None) -> operations.UpdateBillCreditNoteResponse:
        r"""Update bill credit note
        Posts an updated billCreditNote to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).
        
        > **Supported Integrations**
        > 
        > Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support updating bill credit notes.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateBillCreditNoteRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/billCreditNotes/{billCreditNoteId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bill_credit_note", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.UpdateBillCreditNoteRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', True)
            retry_config.backoff = utils.BackoffStrategy(500, 60000, 1.5, 3600000)
            

        def do_request():
            return client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateBillCreditNoteResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UpdateBillCreditNoteResponse])
                res.update_bill_credit_note_response = out

        return res

    