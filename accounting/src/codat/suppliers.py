import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Suppliers:
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
        
    def create_suppliers(self, request: operations.CreateSuppliersRequest) -> operations.CreateSuppliersResponse:
        r"""Create suppliers
        Push suppliers
        
        Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating suppliers.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateSuppliersRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/suppliers', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateSuppliersRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateSuppliersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateSuppliers200ApplicationJSON])
                res.create_suppliers_200_application_json_object = out

        return res

    def download_supplier_attachment(self, request: operations.DownloadSupplierAttachmentRequest) -> operations.DownloadSupplierAttachmentResponse:
        r"""Download supplier attachment
        Download supplier attachment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DownloadSupplierAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments/{attachmentId}/download', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DownloadSupplierAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def get_create_update_suppliers_model(self, request: operations.GetCreateUpdateSuppliersModelRequest) -> operations.GetCreateUpdateSuppliersModelResponse:
        r"""Get create/update supplier model
        Get create/update supplier model. Returns the expected data for the request payload.
        
        See the examples for integration-specific indicative models.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating and updating suppliers.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateUpdateSuppliersModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/suppliers', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateUpdateSuppliersModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateUpdateSuppliersModelPushOption])
                res.push_option = out

        return res

    def get_supplier(self, request: operations.GetSupplierRequest) -> operations.GetSupplierResponse:
        r"""Get supplier
        Gets a single supplier corresponding to the given ID.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSupplierRequest, base_url, '/companies/{companyId}/data/suppliers/{supplierId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSupplierResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetSupplierSourceModifiedDate])
                res.source_modified_date = out

        return res

    def get_supplier_attachment(self, request: operations.GetSupplierAttachmentRequest) -> operations.GetSupplierAttachmentResponse:
        r"""Get supplier attachment
        Get supplier attachment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSupplierAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments/{attachmentId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSupplierAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetSupplierAttachmentAttachment])
                res.attachment = out

        return res

    def list_supplier_attachments(self, request: operations.ListSupplierAttachmentsRequest) -> operations.ListSupplierAttachmentsResponse:
        r"""List supplier attachments
        Get supplier attachments
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListSupplierAttachmentsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListSupplierAttachmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListSupplierAttachmentsAttachments])
                res.attachments = out

        return res

    def list_suppliers(self, request: operations.ListSuppliersRequest) -> operations.ListSuppliersResponse:
        r"""List suppliers
        Gets the latest suppliers for a company, with pagination
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListSuppliersRequest, base_url, '/companies/{companyId}/data/suppliers', request)
        
        query_params = utils.get_query_params(operations.ListSuppliersRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListSuppliersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListSuppliersLinks])
                res.links = out

        return res

    def put_supplier(self, request: operations.PutSupplierRequest) -> operations.PutSupplierResponse:
        r"""Update supplier
        Push supplier
        
        Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support updating suppliers.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutSupplierRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/suppliers/{supplierId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.PutSupplierRequest, request)
        
        client = self._security_client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutSupplierResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PutSupplier200ApplicationJSON])
                res.put_supplier_200_application_json_object = out

        return res

    