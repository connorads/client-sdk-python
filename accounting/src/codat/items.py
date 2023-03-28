"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Items:
    r"""Items"""
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
        
    def create_item(self, request: operations.CreateItemRequest) -> operations.CreateItemResponse:
        r"""Create item
        Posts a new item to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create item model](https://docs.codat.io/accounting-api#/operations/get-create-items-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) for integrations that support creating items.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateItemRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/items', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateItemRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateItem200ApplicationJSON])
                res.create_item_200_application_json_object = out

        return res

    def get_create_items_model(self, request: operations.GetCreateItemsModelRequest) -> operations.GetCreateItemsModelResponse:
        r"""Get create item model
        Get create item model. Returns the expected data for the request payload.
        
        See the examples for integration-specific indicative models.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) for integrations that support creating items.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateItemsModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/items', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateItemsModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateItemsModelPushOption])
                res.push_option = out

        return res

    def get_item(self, request: operations.GetItemRequest) -> operations.GetItemResponse:
        r"""Get item
        Gets the specified item for a given company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetItemRequest, base_url, '/companies/{companyId}/data/items/{itemId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetItemSourceModifiedDate])
                res.source_modified_date = out

        return res

    def list_items(self, request: operations.ListItemsRequest) -> operations.ListItemsResponse:
        r"""List items
        Gets the items for a given company.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListItemsRequest, base_url, '/companies/{companyId}/data/items', request)
        
        query_params = utils.get_query_params(operations.ListItemsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListItemsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListItems200ApplicationJSON])
                res.list_items_200_application_json_object = out

        return res

    