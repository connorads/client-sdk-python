"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .files import Files
from codat.models import shared

SERVERS = [
    "https://api.codat.io",
    r"""Production"""
]
"""Contains the list of servers available to the SDK"""

class Codat:
    r"""An API for uploading and downloading files from 'File Upload' Integrations.
    
    The Accounting file upload, Banking file upload, and Business documents file upload integrations provide simple file upload functionality.
    
    [Read more...](https://docs.codat.io/other/file-upload)
    
    [See our OpenAPI spec](https://github.com/codatio/oas)
    """
    files: Files
    r"""Endpoints to manage uploaded files."""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.8.4"
    _gen_version: str = "2.16.7"

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
        self.files = Files(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    