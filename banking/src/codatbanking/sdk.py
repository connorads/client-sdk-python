"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .account_balances import AccountBalances
from .accounts import Accounts
from .transaction_categories import TransactionCategories
from .transactions import Transactions
from codatbanking.models import shared

SERVERS = [
    "https://api.codat.io",
    r"""Production"""
]
"""Contains the list of servers available to the SDK"""

class CodatBanking:
    r"""Codat's standardized API for accessing banking data.
    Codat's Banking API allows you to access standardised data from over bank accounts via third party providers.
    
    Standardize how you connect to your customers’ bank accounts. Retrieve bank account and bank transaction data in the same way via our partnerships with Plaid and TrueLayer.
    
    [Read more...](https://docs.codat.io/banking-api/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas)
    """
    account_balances: AccountBalances
    r"""Balances for a bank account including end-of-day batch balance or running balances per transaction."""
    accounts: Accounts
    r"""Where payments are made or received, and bank transactions are recorded."""
    transaction_categories: TransactionCategories
    r"""Hierarchical categories associated with a transaction for greater contextual meaning to transaction activity."""
    transactions: Transactions
    r"""An immutable source of up-to-date information on income and expenditure."""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.11.0"
    _gen_version: str = "2.21.0"

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
        self.account_balances = AccountBalances(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.accounts = Accounts(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transaction_categories = TransactionCategories(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transactions = Transactions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    