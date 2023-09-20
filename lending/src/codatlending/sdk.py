"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .accounting_bank_data import AccountingBankData
from .accounts_payable import AccountsPayable
from .accounts_receivable import AccountsReceivable
from .banking import Banking
from .companies import Companies
from .company_info import CompanyInfo
from .connections import Connections
from .data_integrity import DataIntegrity
from .excel_reports import ExcelReports
from .file_upload import FileUpload
from .financial_statements import FinancialStatements
from .liabilities import Liabilities
from .loan_writeback import LoanWriteback
from .manage_data import ManageData
from .sales import Sales
from .sdkconfiguration import SDKConfiguration
from .transactions import Transactions
from codatlending import utils
from codatlending.models import shared

class CodatLending:
    r"""Lending API: Our Lending API helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from accounting, banking, and commerce platforms they are already using. It also includes features to help providers verify the accuracy of data and process it more efficiently.

    The Lending API is built on top of the latest accounting, commerce, and banking data, providing you with the most important data points you need to get a full picture of SMB creditworthiness and make a comprehensive assessment of your customers.

    [Explore product](https://docs.codat.io/lending/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

    ---

    ## Endpoints

    | Endpoints            | Description                                                                                                |
    |:---------------------|:-----------------------------------------------------------------------------------------------------------|
    | Companies            | Create and manage your SMB users' companies.                                                               |
    | Connections          | Create new and manage existing data connections for a company.                                             |
    | Bank statements      | Retrieve banking data from linked bank accounts.                                                           |
    | Sales                | Retrieve standardized sales data from a linked commerce platform.                                          |
    | Financial statements | Financial data and reports from a linked accounting platform.                                              |
    | Liabilities          | Debt and other liabilities.                                                                                |
    | Accounts payable     | Data from a linked accounting platform representing money the business owes money to its suppliers.        |
    | Accounts receivable  | Data from a linked accounting platform representing money owed to the business for sold goods or services. |
    | Transactions         | Data from a linked accounting platform representing transactions.                                          |
    | Data integrity       | Match mutable accounting data with immutable banking data to increase confidence in financial data.        |
    | Company info         | View company profile from the source platform.                                                             |
    | Excel reports        | Download reports in Excel format.                                                                          |
    | Categories           | Manage Codat's automatic account categorization functionality.                                             |
    | Manage data          | Control how data is retrieved from an integration.                                                         |
    | File upload          | Endpoints to manage uploaded files.                                                                        |
    """
    accounting_bank_data: AccountingBankData
    r"""Access bank transactions from an accounting platform."""
    companies: Companies
    r"""Create and manage your Codat companies."""
    company_info: CompanyInfo
    r"""View company information fetched from the source platform."""
    connections: Connections
    r"""Manage your companies' data connections."""
    data_integrity: DataIntegrity
    r"""Match mutable accounting data with immutable banking data to increase confidence in financial data."""
    excel_reports: ExcelReports
    r"""Download reports in Excel format."""
    file_upload: FileUpload
    r"""Endpoints to manage uploaded files."""
    liabilities: Liabilities
    r"""Debt and other liabilities."""
    accounts_payable: AccountsPayable
    accounts_receivable: AccountsReceivable
    banking: Banking
    financial_statements: FinancialStatements
    loan_writeback: LoanWriteback
    manage_data: ManageData
    sales: Sales
    transactions: Transactions

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: shared.Security = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
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
        :type url_params: dict[str, str]
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
        self.accounting_bank_data = AccountingBankData(self.sdk_configuration)
        self.companies = Companies(self.sdk_configuration)
        self.company_info = CompanyInfo(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.data_integrity = DataIntegrity(self.sdk_configuration)
        self.excel_reports = ExcelReports(self.sdk_configuration)
        self.file_upload = FileUpload(self.sdk_configuration)
        self.liabilities = Liabilities(self.sdk_configuration)
        self.accounts_payable = AccountsPayable(self.sdk_configuration)
        self.accounts_receivable = AccountsReceivable(self.sdk_configuration)
        self.banking = Banking(self.sdk_configuration)
        self.financial_statements = FinancialStatements(self.sdk_configuration)
        self.loan_writeback = LoanWriteback(self.sdk_configuration)
        self.manage_data = ManageData(self.sdk_configuration)
        self.sales = Sales(self.sdk_configuration)
        self.transactions = Transactions(self.sdk_configuration)
    