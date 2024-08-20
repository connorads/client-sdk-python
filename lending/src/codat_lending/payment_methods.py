"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from codat_lending import utils
from codat_lending._hooks import HookContext
from codat_lending.models import errors, operations, shared
from codat_lending.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Optional, Union, cast

class PaymentMethods(BaseSDK):
    
    
    def get(
        self, *,
        request: Union[operations.GetCommercePaymentMethodRequest, operations.GetCommercePaymentMethodRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommercePaymentMethod]:
        r"""Get payment method

        The *Get payment method* endpoint returns a single payment method for a given paymentMethodId.

        [Payment methods](https://docs.codat.io/lending-api#/schemas/PaymentMethod) represent the payment method(s) used to make payments.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-paymentMethods) for integrations that support getting a specific payment method.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetCommercePaymentMethodRequest)
        request = cast(operations.GetCommercePaymentMethodRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/data/commerce-paymentMethods/{paymentMethodId}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="get-commerce-payment-method", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["401","402","403","404","409","429","4XX","500","503","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommercePaymentMethod])
        if utils.match_response(http_res, ["401","402","403","404","409","429","500","503"], "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def get_async(
        self, *,
        request: Union[operations.GetCommercePaymentMethodRequest, operations.GetCommercePaymentMethodRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommercePaymentMethod]:
        r"""Get payment method

        The *Get payment method* endpoint returns a single payment method for a given paymentMethodId.

        [Payment methods](https://docs.codat.io/lending-api#/schemas/PaymentMethod) represent the payment method(s) used to make payments.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-paymentMethods) for integrations that support getting a specific payment method.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetCommercePaymentMethodRequest)
        request = cast(operations.GetCommercePaymentMethodRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/data/commerce-paymentMethods/{paymentMethodId}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="get-commerce-payment-method", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["401","402","403","404","409","429","4XX","500","503","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommercePaymentMethod])
        if utils.match_response(http_res, ["401","402","403","404","409","429","500","503"], "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def list(
        self, *,
        request: Union[operations.ListCommercePaymentMethodsRequest, operations.ListCommercePaymentMethodsRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommercePaymentMethods]:
        r"""List payment methods

        The *List payment methods* endpoint returns a list of [payment methods](https://docs.codat.io/lending-api#/schemas/PaymentMethod) for a given company's connection.

        [Payment methods](https://docs.codat.io/lending-api#/schemas/PaymentMethod) represent the payment method(s) used to make payments.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.ListCommercePaymentMethodsRequest)
        request = cast(operations.ListCommercePaymentMethodsRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/data/commerce-paymentMethods",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="list-commerce-payment-methods", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","402","403","404","409","429","4XX","500","503","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommercePaymentMethods])
        if utils.match_response(http_res, ["400","401","402","403","404","409","429","500","503"], "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def list_async(
        self, *,
        request: Union[operations.ListCommercePaymentMethodsRequest, operations.ListCommercePaymentMethodsRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommercePaymentMethods]:
        r"""List payment methods

        The *List payment methods* endpoint returns a list of [payment methods](https://docs.codat.io/lending-api#/schemas/PaymentMethod) for a given company's connection.

        [Payment methods](https://docs.codat.io/lending-api#/schemas/PaymentMethod) represent the payment method(s) used to make payments.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.ListCommercePaymentMethodsRequest)
        request = cast(operations.ListCommercePaymentMethodsRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/data/commerce-paymentMethods",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig("backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "408",
                "429",
                "5XX"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="list-commerce-payment-methods", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","402","403","404","409","429","4XX","500","503","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommercePaymentMethods])
        if utils.match_response(http_res, ["400","401","402","403","404","409","429","500","503"], "application/json"):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
