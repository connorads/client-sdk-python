"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from codat_lending import utils
from codat_lending._hooks import SDKHooks
from codat_lending.accounts_payable import AccountsPayable
from codat_lending.accounts_receivable import AccountsReceivable
from codat_lending.bank_statements import BankStatements
from codat_lending.banking import Banking
from codat_lending.codatlending_accounting_bank_data import CodatLendingAccountingBankData
from codat_lending.companies import Companies
from codat_lending.company_info import CompanyInfo
from codat_lending.connections import Connections
from codat_lending.data_integrity import DataIntegrity
from codat_lending.excel_reports import ExcelReports
from codat_lending.file_upload import FileUpload
from codat_lending.financial_statements import FinancialStatements
from codat_lending.liabilities import Liabilities
from codat_lending.loan_writeback import LoanWriteback
from codat_lending.manage_data import ManageData
from codat_lending.models import shared
from codat_lending.sales import Sales
from codat_lending.transactions import Transactions
from codat_lending.types import OptionalNullable, UNSET
import httpx
from typing import Callable, Dict, Optional, Union

class CodatLending(BaseSDK):
    r"""Lending API: Our Lending API helps you make smarter credit decisions on small businesses by enabling you to pull your customers' latest data from accounting, banking, and commerce software they are already using. It also includes features to help providers verify the accuracy of data and process it more efficiently.

    The Lending API is built on top of the latest accounting, commerce, and banking data, providing you with the most important data points you need to get a full picture of SMB creditworthiness and make a comprehensive assessment of your customers.

    [Explore product](https://docs.codat.io/lending/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

    <!-- Start Codat Tags Table -->
    ## Endpoints

    | Endpoints | Description |
    | :- |:- |
    | Companies | Create and manage your SMB users' companies. |
    | Connections | Create new and manage existing data connections for a company. |
    | Bank statements | Retrieve banking data from linked bank accounts. |
    | Sales | Retrieve standardized sales data from a linked commerce software. |
    | Financial statements | Financial data and reports from a linked accounting software. |
    | Liabilities | Debt and other liabilities. |
    | Accounts payable | Data from a linked accounting software representing money the business owes money to its suppliers. |
    | Accounts receivable | Data from a linked accounting software representing money owed to the business for sold goods or services. |
    | Transactions | Data from a linked accounting software representing transactions. |
    | Company info | View company information fetched from the source platform. |
    | Data integrity | Match mutable accounting data with immutable banking data to increase confidence in financial data. |
    | Excel reports | Download reports in Excel format. |
    | Manage data | Control how data is retrieved from an integration. |
    | File upload | Endpoints to manage uploaded files. |
    | Loan writeback | Implement the [loan writeback](https://docs.codat.io/lending/guides/loan-writeback/introduction) procedure in your lending process to maintain an accurate position of a loan during the entire lending cycle. |
    <!-- End Codat Tags Table -->
    """
    companies: Companies
    r"""Create and manage your SMB users' companies."""
    connections: Connections
    r"""Create new and manage existing data connections for a company."""
    bank_statements: BankStatements
    r"""Retrieve banking data from linked bank accounts."""
    transactions: Transactions
    accounting_bank_data: CodatLendingAccountingBankData
    r"""Access bank transactions from an accounting software."""
    banking: Banking
    accounts_payable: AccountsPayable
    sales: Sales
    company_info: CompanyInfo
    r"""View company information fetched from the source platform."""
    accounts_receivable: AccountsReceivable
    file_upload: FileUpload
    r"""Endpoints to manage uploaded files."""
    loan_writeback: LoanWriteback
    financial_statements: FinancialStatements
    manage_data: ManageData
    liabilities: Liabilities
    r"""Debt and other liabilities."""
    data_integrity: DataIntegrity
    r"""Match mutable accounting data with immutable banking data to increase confidence in financial data."""
    excel_reports: ExcelReports
    r"""Download reports in Excel format."""
    def __init__(
        self,
        security: Union[shared.Security, Callable[[], shared.Security]],
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    

        BaseSDK.__init__(self, SDKConfiguration(
            client=client,
            async_client=async_client,
            security=security,
            server_url=server_url,
            server_idx=server_idx,
            retry_config=retry_config,
            timeout_ms=timeout_ms,
            debug_logger=debug_logger
        ))

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.companies = Companies(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.bank_statements = BankStatements(self.sdk_configuration)
        self.transactions = Transactions(self.sdk_configuration)
        self.accounting_bank_data = CodatLendingAccountingBankData(self.sdk_configuration)
        self.banking = Banking(self.sdk_configuration)
        self.accounts_payable = AccountsPayable(self.sdk_configuration)
        self.sales = Sales(self.sdk_configuration)
        self.company_info = CompanyInfo(self.sdk_configuration)
        self.accounts_receivable = AccountsReceivable(self.sdk_configuration)
        self.file_upload = FileUpload(self.sdk_configuration)
        self.loan_writeback = LoanWriteback(self.sdk_configuration)
        self.financial_statements = FinancialStatements(self.sdk_configuration)
        self.manage_data = ManageData(self.sdk_configuration)
        self.liabilities = Liabilities(self.sdk_configuration)
        self.data_integrity = DataIntegrity(self.sdk_configuration)
        self.excel_reports = ExcelReports(self.sdk_configuration)
    
