"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .companies import Companies
from .configuration import Configuration
from .connections import Connections
from .expenses import Expenses
from .mapping_options import MappingOptions
from .sdkconfiguration import SDKConfiguration
from .sync import Sync
from .sync_status import SyncStatus
from .transaction_status import TransactionStatus
from codatsyncexpenses import utils
from codatsyncexpenses.models import shared
from typing import Dict

class CodatSyncExpenses:
    r"""Sync for Expenses (v1): The API for Sync for Expenses.

    Sync for Expenses is an API and a set of supporting tools. It has been built to
    enable corporate card and expense management platforms to provide high-quality
    integrations with multiple accounting platforms through a standardized API.

    [Read more...](https://docs.codat.io/sync-for-expenses/overview)

    [See our OpenAPI spec](https://github.com/codatio/oas)

    Not seeing what you expect? [See the main Sync for Commerce API](https://docs.codat.io/sync-for-commerce-api).
    """
    companies: Companies
    r"""Create and manage your Codat companies."""
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

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: shared.Security = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        
        security_client = utils.configure_security_client(client, security)
        
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.companies = Companies(self.sdk_configuration)
        self.configuration = Configuration(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.expenses = Expenses(self.sdk_configuration)
        self.mapping_options = MappingOptions(self.sdk_configuration)
        self.sync = Sync(self.sdk_configuration)
        self.sync_status = SyncStatus(self.sdk_configuration)
        self.transaction_status = TransactionStatus(self.sdk_configuration)
    