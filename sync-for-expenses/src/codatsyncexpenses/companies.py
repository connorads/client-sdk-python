"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from codatsyncexpenses import utils
from codatsyncexpenses._hooks import HookContext
from codatsyncexpenses.models import errors, operations, shared
from typing import Optional

class Companies:
    r"""Create and manage your Codat companies."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def create(self, request: Optional[shared.CompanyRequestBody], retries: Optional[utils.RetryConfig] = None) -> operations.CreateCompanyResponse:
        r"""Create company
        Use the *Create company* endpoint to create a new [company](https://docs.codat.io/sync-for-expenses-api#/schemas/Company) that represents your customer in Codat. 

        A [company](https://docs.codat.io/sync-for-expenses-api#/schemas/Company) represents a business sharing access to their data.
        Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.

        If forbidden characters (see `name` pattern) are present in the request, a company will be created with the forbidden characters removed. For example, `Company (Codat[1])` with be created as `Company Codat1`.
        """
        hook_ctx = HookContext(operation_id='create-company', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/companies'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        req_content_type, data, form = utils.serialize_request_body(request, Optional[shared.CompanyRequestBody], "request", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['400','401','402','403','429','4XX','500','503','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        
        
        res = operations.CreateCompanyResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.Company])
                res.company = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 429, 500, 503]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def delete(self, request: operations.DeleteCompanyRequest, retries: Optional[utils.RetryConfig] = None) -> operations.DeleteCompanyResponse:
        r"""Delete a company
        The *Delete company* endpoint permanently deletes a [company](https://docs.codat.io/sync-for-expenses-api#/schemas/Company), its [connections](https://docs.codat.io/sync-for-expenses-api#/schemas/Connection) and any cached data. This operation is irreversible.

        A [company](https://docs.codat.io/sync-for-expenses-api#/schemas/Company) represents a business sharing access to their data.
        Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.
        """
        hook_ctx = HookContext(operation_id='delete-company', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteCompanyRequest, base_url, '/companies/{companyId}', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('DELETE', url, params=query_params, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        
        
        res = operations.DeleteCompanyResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get(self, request: operations.GetCompanyRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCompanyResponse:
        r"""Get company
        The *Get company* endpoint returns a single company for a given `companyId`.

        A [company](https://docs.codat.io/sync-for-expenses-api#/schemas/Company) represents a business sharing access to their data.
        Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.
        """
        hook_ctx = HookContext(operation_id='get-company', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCompanyRequest, base_url, '/companies/{companyId}', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('GET', url, params=query_params, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        
        
        res = operations.GetCompanyResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.Company])
                res.company = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def list(self, request: operations.ListCompaniesRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListCompaniesResponse:
        r"""List companies
        The *List companies* endpoint returns a list of [companies] associated to your instances.

        A [company](https://docs.codat.io/sync-for-expenses-api#/schemas/Company) represents a business sharing access to their data.
        Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.
        """
        hook_ctx = HookContext(operation_id='list-companies', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/companies'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        query_params = { **utils.get_query_params(operations.ListCompaniesRequest, request), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('GET', url, params=query_params, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['400','401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        
        
        res = operations.ListCompaniesResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.Companies])
                res.companies = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def update(self, request: operations.UpdateCompanyRequest, retries: Optional[utils.RetryConfig] = None) -> operations.UpdateCompanyResponse:
        r"""Update company
        Use the *Update company* endpoint to update both the name and description of the company. 
        If you use [groups](https://docs.codat.io/sync-for-expenses-api#/schemas/Group) to manage a set of companies, use the [Add company](https://docs.codat.io/sync-for-expenses-api#/operations/add-company-to-group) or [Remove company](https://docs.codat.io/sync-for-expenses-api#/operations/remove-company-from-group) endpoints to add or remove a company from a group.

        A [company](https://docs.codat.io/sync-for-expenses-api#/schemas/Company) represents a business sharing access to their data.
        Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.
        """
        hook_ctx = HookContext(operation_id='update-company', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateCompanyRequest, base_url, '/companies/{companyId}', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        req_content_type, data, form = utils.serialize_request_body(request, operations.UpdateCompanyRequest, "company_request_body", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('PUT', url, params=query_params, data=data, files=form, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['401','402','403','404','429','4XX','500','503','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        
        
        res = operations.UpdateCompanyResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.Company])
                res.company = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ErrorMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    