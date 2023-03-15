import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Invoices:
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
        
    def create_invoice(self, request: operations.CreateInvoiceRequest) -> operations.CreateInvoiceResponse:
        r"""Create invoice
        Posts a new invoice to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating invoices.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateInvoiceRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/invoices', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateInvoiceRequest, request)
        
        client = self._security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateInvoiceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateInvoice200ApplicationJSON])
                res.create_invoice_200_application_json_object = out

        return res

    def donwload_invoice_attachment(self, request: operations.DonwloadInvoiceAttachmentRequest) -> operations.DonwloadInvoiceAttachmentResponse:
        r"""Download invoice attachment
        Download invoice attachments
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DonwloadInvoiceAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments/{attachmentId}/download', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DonwloadInvoiceAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def get_create_update_invoices_model(self, request: operations.GetCreateUpdateInvoicesModelRequest) -> operations.GetCreateUpdateInvoicesModelResponse:
        r"""Get create/update invoice model
        Get create/update invoice model. Returns the expected data for the request payload.
        
        See the examples for integration-specific indicative models.
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating and updating invoices.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCreateUpdateInvoicesModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/invoices', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateUpdateInvoicesModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCreateUpdateInvoicesModelPushOption])
                res.push_option = out

        return res

    def get_invoice(self, request: operations.GetInvoiceRequest) -> operations.GetInvoiceResponse:
        r"""Get invoice
        Get invoice
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetInvoiceRequest, base_url, '/companies/{companyId}/data/invoices/{invoiceId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetInvoiceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInvoiceSourceModifiedDate])
                res.source_modified_date = out

        return res

    def get_invoice_attachment(self, request: operations.GetInvoiceAttachmentRequest) -> operations.GetInvoiceAttachmentResponse:
        r"""Get invoice attachment
        Get invoice attachments
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetInvoiceAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments/{attachmentId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetInvoiceAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInvoiceAttachmentAttachment])
                res.attachment = out

        return res

    def get_invoice_attachments(self, request: operations.GetInvoiceAttachmentsRequest) -> operations.GetInvoiceAttachmentsResponse:
        r"""Get invoice attachments
        Get invoice attachments
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetInvoiceAttachmentsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetInvoiceAttachmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetInvoiceAttachmentsAttachments])
                res.attachments = out

        return res

    def get_invoice_pdf(self, request: operations.GetInvoicePdfRequest) -> operations.GetInvoicePdfResponse:
        r"""Get invoice as PDF
        Get invoice as PDF
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetInvoicePdfRequest, base_url, '/companies/{companyId}/data/invoices/{invoiceId}/pdf', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetInvoicePdfResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def list_invoices(self, request: operations.ListInvoicesRequest) -> operations.ListInvoicesResponse:
        r"""List invoices
        Gets the latest invoices for a company, with pagination
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListInvoicesRequest, base_url, '/companies/{companyId}/data/invoices', request)
        
        query_params = utils.get_query_params(operations.ListInvoicesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListInvoicesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListInvoicesLinks])
                res.links = out

        return res

    def push_invoice_attachment(self, request: operations.PushInvoiceAttachmentRequest) -> operations.PushInvoiceAttachmentResponse:
        r"""Push invoice attachment
        Push invoice attachment
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.PushInvoiceAttachmentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId}/attachment', request)
        
        
        client = self._security_client
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PushInvoiceAttachmentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def update_invoice(self, request: operations.UpdateInvoiceRequest) -> operations.UpdateInvoiceResponse:
        r"""Update invoice
        Posts an updated invoice to the accounting package for a given company.
        
        Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support updating invoices.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateInvoiceRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.UpdateInvoiceRequest, request)
        
        client = self._security_client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateInvoiceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateInvoice200ApplicationJSON])
                res.update_invoice_200_application_json_object = out

        return res

    