"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from codat_lending import utils
from codat_lending._hooks import HookContext
from codat_lending.models import errors, operations, shared
from codat_lending.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Optional, Union, cast


class Metrics(BaseSDK):
    def get_customer_retention(
        self,
        *,
        request: Union[
            operations.GetCommerceCustomerRetentionMetricsRequest,
            operations.GetCommerceCustomerRetentionMetricsRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommerceReport]:
        r"""Get customer retention metrics

        The *Get customer retention metrics* endpoint returns customer retention insights for a specific company's commerce connection over one or more periods of time.

        This detail helps you assess a merchant's health and advise them on performance improvement strategies. It also provides you with key insights you need to assess the credit risk of a company.

        #### Customer retention metrics

        - __Existing customers__: the number of unique customers that have placed an order(s) in the specified period and any previous period.
        - __New customers__: the number of unique customers that have placed an order(s) in the specified period and none in any previous period.
        - __Total customers__: the total number of existing and new customers within the specified period.
        - __Retention rate__: the ratio of existing customers within the specified period compared to the total customers at the end of the previous period represented as a percentage.
        - __Repeat rate__: the ratio of existing customers to total customers over the specified period represented as a percentage.

        Learn more about the formulas used to calculate customer retention metrics [here](https://docs.codat.io/lending/commerce-metrics/overview#what-metrics-are-available).

        #### Response structure

        The Customer retention report's dimensions and measures are:

        | Index                       | Dimensions                 |
        |-----------------------------|----------------------------|
        | `index` = 0                 | Period                     |
        | `index` = 1                 | Customer retention metrics |

        | Index                | Measures    |
        |----------------------|------------|
        | `index` = 0          | Count      |
        | `index` = 1          | Percentage |

        The report data then combines multiple reporting dimensions and measures and outputs the value of each combination.

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
            request = utils.unmarshal(
                request, operations.GetCommerceCustomerRetentionMetricsRequest
            )
        request = cast(operations.GetCommerceCustomerRetentionMetricsRequest, request)

        req = self.build_request(
            method="GET",
            path="/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/customerRetention",
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
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="get-commerce-customer-retention-metrics",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommerceReport])
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_customer_retention_async(
        self,
        *,
        request: Union[
            operations.GetCommerceCustomerRetentionMetricsRequest,
            operations.GetCommerceCustomerRetentionMetricsRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommerceReport]:
        r"""Get customer retention metrics

        The *Get customer retention metrics* endpoint returns customer retention insights for a specific company's commerce connection over one or more periods of time.

        This detail helps you assess a merchant's health and advise them on performance improvement strategies. It also provides you with key insights you need to assess the credit risk of a company.

        #### Customer retention metrics

        - __Existing customers__: the number of unique customers that have placed an order(s) in the specified period and any previous period.
        - __New customers__: the number of unique customers that have placed an order(s) in the specified period and none in any previous period.
        - __Total customers__: the total number of existing and new customers within the specified period.
        - __Retention rate__: the ratio of existing customers within the specified period compared to the total customers at the end of the previous period represented as a percentage.
        - __Repeat rate__: the ratio of existing customers to total customers over the specified period represented as a percentage.

        Learn more about the formulas used to calculate customer retention metrics [here](https://docs.codat.io/lending/commerce-metrics/overview#what-metrics-are-available).

        #### Response structure

        The Customer retention report's dimensions and measures are:

        | Index                       | Dimensions                 |
        |-----------------------------|----------------------------|
        | `index` = 0                 | Period                     |
        | `index` = 1                 | Customer retention metrics |

        | Index                | Measures    |
        |----------------------|------------|
        | `index` = 0          | Count      |
        | `index` = 1          | Percentage |

        The report data then combines multiple reporting dimensions and measures and outputs the value of each combination.

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
            request = utils.unmarshal(
                request, operations.GetCommerceCustomerRetentionMetricsRequest
            )
        request = cast(operations.GetCommerceCustomerRetentionMetricsRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/customerRetention",
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
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="get-commerce-customer-retention-metrics",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommerceReport])
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def get_lifetime_value(
        self,
        *,
        request: Union[
            operations.GetCommerceLifetimeValueMetricsRequest,
            operations.GetCommerceLifetimeValueMetricsRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommerceReport]:
        r"""Get lifetime value metrics

        The *Get lifetime value metrics* endpoint returns the average revenue that a specific company will generate throughout its lifespan over one or more periods of time.

        This detail helps you assess a merchant's health and advise them on performance improvement strategies. It also provides you with key insights you need to assess the credit risk of a company.

        Learn more about the formulas used to calculate the lifetime value metrics [here](https://docs.codat.io/lending/commerce-metrics/overview#what-metrics-are-available).

        Refer to the [commerce reporting structure](https://docs.codat.io/lending/commerce-metrics/reporting-structure) page for more detail on commerce reports in Lending.

        #### Response structure

        The Lifetime value report's dimensions and measures are:

        | Index         | Dimensions             |
        |---------------|------------------------|
        | `index` = 0   | Period                 |
        | `index` = 1   | Lifetime value metrics |

        | Index             | Measures |
        |-------------------|---------|
        |   `index` = 1     | Value   |

        The report data then combines multiple reporting dimensions and measures and outputs the value of each combination.


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
            request = utils.unmarshal(
                request, operations.GetCommerceLifetimeValueMetricsRequest
            )
        request = cast(operations.GetCommerceLifetimeValueMetricsRequest, request)

        req = self.build_request(
            method="GET",
            path="/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/lifetimeValue",
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
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="get-commerce-lifetime-value-metrics",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommerceReport])
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_lifetime_value_async(
        self,
        *,
        request: Union[
            operations.GetCommerceLifetimeValueMetricsRequest,
            operations.GetCommerceLifetimeValueMetricsRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommerceReport]:
        r"""Get lifetime value metrics

        The *Get lifetime value metrics* endpoint returns the average revenue that a specific company will generate throughout its lifespan over one or more periods of time.

        This detail helps you assess a merchant's health and advise them on performance improvement strategies. It also provides you with key insights you need to assess the credit risk of a company.

        Learn more about the formulas used to calculate the lifetime value metrics [here](https://docs.codat.io/lending/commerce-metrics/overview#what-metrics-are-available).

        Refer to the [commerce reporting structure](https://docs.codat.io/lending/commerce-metrics/reporting-structure) page for more detail on commerce reports in Lending.

        #### Response structure

        The Lifetime value report's dimensions and measures are:

        | Index         | Dimensions             |
        |---------------|------------------------|
        | `index` = 0   | Period                 |
        | `index` = 1   | Lifetime value metrics |

        | Index             | Measures |
        |-------------------|---------|
        |   `index` = 1     | Value   |

        The report data then combines multiple reporting dimensions and measures and outputs the value of each combination.


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
            request = utils.unmarshal(
                request, operations.GetCommerceLifetimeValueMetricsRequest
            )
        request = cast(operations.GetCommerceLifetimeValueMetricsRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/lifetimeValue",
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
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="get-commerce-lifetime-value-metrics",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommerceReport])
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def get_revenue(
        self,
        *,
        request: Union[
            operations.GetCommerceRevenueMetricsRequest,
            operations.GetCommerceRevenueMetricsRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommerceReport]:
        r"""Get commerce revenue metrics

        The *Get revenue report* endpoint returns the revenue and revenue growth for a specific company connection over one or more periods of time.

        This detail helps you assess a merchant's health and advise them on performance improvement strategies. It also provides you with key insights you need to assess the credit risk of a company.

        Learn more about the formulas used to calculate the revenue metrics [here](https://docs.codat.io/lending/commerce-metrics/overview#what-metrics-are-available).

        Refer to the [commerce reporting structure](https://docs.codat.io/lending/commerce-metrics/reporting-structure) page for more details on commerce reports in Lending.

        #### Response structure

        The Revenue report's dimensions and measures are:

        | Index         | Dimensions |
        |---------------|------------|
        |   `index` = 0 | Period     |
        |   `index` = 1 | Revenue    |

        | Index         | Measures                                                                                                                 |
        |---------------|--------------------------------------------------------------------------------------------------------------------------|
        | `index` = 0   | Value                                                                                                                    |
        | `index` = 1   | Percentage change, defined as the change between the current and previous periods' values and expressed as a percentage. |

        The report data then combines multiple reporting dimensions and measures and outputs the value of each combination.


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
            request = utils.unmarshal(
                request, operations.GetCommerceRevenueMetricsRequest
            )
        request = cast(operations.GetCommerceRevenueMetricsRequest, request)

        req = self.build_request(
            method="GET",
            path="/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/revenue",
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
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="get-commerce-revenue-metrics",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommerceReport])
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_revenue_async(
        self,
        *,
        request: Union[
            operations.GetCommerceRevenueMetricsRequest,
            operations.GetCommerceRevenueMetricsRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CommerceReport]:
        r"""Get commerce revenue metrics

        The *Get revenue report* endpoint returns the revenue and revenue growth for a specific company connection over one or more periods of time.

        This detail helps you assess a merchant's health and advise them on performance improvement strategies. It also provides you with key insights you need to assess the credit risk of a company.

        Learn more about the formulas used to calculate the revenue metrics [here](https://docs.codat.io/lending/commerce-metrics/overview#what-metrics-are-available).

        Refer to the [commerce reporting structure](https://docs.codat.io/lending/commerce-metrics/reporting-structure) page for more details on commerce reports in Lending.

        #### Response structure

        The Revenue report's dimensions and measures are:

        | Index         | Dimensions |
        |---------------|------------|
        |   `index` = 0 | Period     |
        |   `index` = 1 | Revenue    |

        | Index         | Measures                                                                                                                 |
        |---------------|--------------------------------------------------------------------------------------------------------------------------|
        | `index` = 0   | Value                                                                                                                    |
        | `index` = 1   | Percentage change, defined as the change between the current and previous periods' values and expressed as a percentage. |

        The report data then combines multiple reporting dimensions and measures and outputs the value of each combination.


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
            request = utils.unmarshal(
                request, operations.GetCommerceRevenueMetricsRequest
            )
        request = cast(operations.GetCommerceRevenueMetricsRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/revenue",
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
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="get-commerce-revenue-metrics",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.CommerceReport])
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )
