"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .configuration import Configuration
from .connections import Connections
from .expenses import Expenses
from .mapping_options import MappingOptions
from .sync import Sync
from .sync_status import SyncStatus
from .transaction_status import TransactionStatus
from codatsyncexpenses.models import shared

SERVERS = [
    "https://api.codat.io",
]
"""Contains the list of servers available to the SDK"""

class CodatSyncExpenses:
    r"""The API for Sync for Expenses.
    Sync for Expenses is an API and a set of supporting tools. It has been built to enable corporate card and expense management platforms to provide high-quality integrations with multiple accounting platforms through a standardized API.
    
    [Read more...](https://docs.codat.io/sync-for-expenses/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas)
    """
    configuration: Configuration
    r"""Companies sync configuration."""
    connections: Connections
    r"""Create and manage partner expense connection."""
    expenses: Expenses
    r"""Create expense datasets and upload receipts."""
    mapping_options: MappingOptions
    r"""Mapping options for a companies expenses."""
    sync: Sync
    r"""Triggering a new sync of expenses to accounting software."""
    sync_status: SyncStatus
    r"""Check the status of ongoing or previous expense syncs."""
    transaction_status: TransactionStatus
    r"""Retrieve the status of transactions within a sync."""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.9.1"
    _gen_version: str = "2.17.9"

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
        self.configuration = Configuration(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.connections = Connections(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.expenses = Expenses(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.mapping_options = MappingOptions(
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
        
        self.sync_status = SyncStatus(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transaction_status = TransactionStatus(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    