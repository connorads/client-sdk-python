"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ListIntegrationsRequest:
    
    page: int = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""  
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""  
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""  
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrations401ApplicationJSON:
    r"""Your API request was not properly authorized."""
    
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canBeRetried'), 'exclude': lambda f: f is None }})  
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correlationId'), 'exclude': lambda f: f is None }})  
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})  
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})  
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})  
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrations400ApplicationJSON:
    r"""Your `query` parameter was not correctly formed"""
    
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canBeRetried'), 'exclude': lambda f: f is None }})  
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correlationId'), 'exclude': lambda f: f is None }})  
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})  
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})  
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})  
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksLinksHypertextReference:
    
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('href'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksLinks:
    
    current: ListIntegrationsLinksLinksHypertextReference = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current') }})  
    self_: ListIntegrationsLinksLinksHypertextReference = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self') }})  
    next: Optional[ListIntegrationsLinksLinksHypertextReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})  
    previous: Optional[ListIntegrationsLinksLinksHypertextReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})  
    
class ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeaturesFeatureStateEnum(str, Enum):
    RELEASE = "Release"
    BETA = "Beta"
    DEPRECATED = "Deprecated"
    NOT_SUPPORTED = "NotSupported"
    NOT_IMPLEMENTED = "NotImplemented"

class ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeaturesFeatureTypeEnum(str, Enum):
    GET = "Get"
    POST = "Post"
    CATEGORIZATION = "Categorization"
    DELETE = "Delete"
    PUT = "Put"
    GET_AS_PDF = "GetAsPdf"
    DOWNLOAD_ATTACHMENT = "DownloadAttachment"
    GET_ATTACHMENT = "GetAttachment"
    GET_ATTACHMENTS = "GetAttachments"
    UPLOAD_ATTACHMENT = "UploadAttachment"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeatures:
    
    feature_state: ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeaturesFeatureStateEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('featureState') }})  
    feature_type: ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeaturesFeatureTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('featureType') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksIntegrationDatatypeFeature:
    r"""Describes support for a given datatype and associated operations"""
    
    datatype: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datatype') }})  
    supported_features: list[ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeatures] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supportedFeatures') }})  
    
class ListIntegrationsLinksIntegrationSourceTypeEnum(str, Enum):
    r"""The type of platform of the connection."""
    ACCOUNTING = "Accounting"
    BANKING = "Banking"
    COMMERCE = "Commerce"
    OTHER = "Other"
    UNKNOWN = "Unknown"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksIntegration:
    r"""An integration that Codat supports"""
    
    enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled') }})
    r"""Whether this integration is enabled for your customers to use"""  
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    r"""4 letter key for an integration. [Read more](https://docs.codat.io/integrations/accounting/accounting-platform-keys)."""  
    logo_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logoUrl') }})  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})  
    data_provided_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataProvidedBy'), 'exclude': lambda f: f is None }})  
    datatype_features: Optional[list[ListIntegrationsLinksIntegrationDatatypeFeature]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datatypeFeatures'), 'exclude': lambda f: f is None }})  
    integration_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrationId'), 'exclude': lambda f: f is None }})
    r"""A Codat ID representing the integration."""  
    is_beta: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBeta'), 'exclude': lambda f: f is None }})  
    is_offline_connector: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isOfflineConnector'), 'exclude': lambda f: f is None }})  
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId'), 'exclude': lambda f: f is None }})
    r"""A source-specific ID used to distinguish between different sources originating from the same data connection. In general, a data connection is a single data source. However, for TrueLayer, `sourceId` is associated with a specific bank and has a many-to-one relationship with the `integrationId`."""  
    source_type: Optional[ListIntegrationsLinksIntegrationSourceTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    r"""The type of platform of the connection."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinks:
    r"""Codat's Paging Model"""
    
    links: ListIntegrationsLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_links') }})  
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageNumber') }})  
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize') }})  
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalResults') }})  
    results: Optional[list[ListIntegrationsLinksIntegration]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class ListIntegrationsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    links: Optional[ListIntegrationsLinks] = dataclasses.field(default=None)
    r"""OK"""  
    list_integrations_400_application_json_object: Optional[ListIntegrations400ApplicationJSON] = dataclasses.field(default=None)
    r"""Your `query` parameter was not correctly formed"""  
    list_integrations_401_application_json_object: Optional[ListIntegrations401ApplicationJSON] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    