"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .company_management import CompanyManagement
from .configuration import Configuration
from .integrations import Integrations
from .sync import Sync
from .sync_flow_preferences import SyncFlowPreferences
from codat.models import shared

SERVERS = [
    "https://api.codat.io",
    r"""Production"""
]
"""Contains the list of servers available to the SDK"""

class Codat:
    r"""The API for Sync for Commerce. Sync for Commerce is an API and a set of supporting tools. It has been built to enable e-commerce, point of sale platforms to provide high-quality integrations with numerous accounting platform through standardized API, seamlessly transforming business sale's data into accounting artefacts.
    [Read More...](https://docs.codat.io/sfc/overview)
    """
    company_management: CompanyManagement
    r"""Create new and manage existing sync for commerce companies."""
    configuration: Configuration
    r"""Expressively configure preferences for any given sync for commerce company."""
    integrations: Integrations
    r"""View useful information about codat's integrations."""
    sync: Sync
    r"""Initiate a sync of sync for commerce company data into their respective accounting software."""
    sync_flow_preferences: SyncFlowPreferences
    r"""Configure preferences for any given sync for commerce company using sync flow."""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.8.3"
    _gen_version: str = "2.16.5"

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
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.company_management = CompanyManagement(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.configuration = Configuration(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.integrations = Integrations(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.sync = Sync(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.sync_flow_preferences = SyncFlowPreferences(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    