"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .account_transactions import AccountTransactions
from .accounts import Accounts
from .bank_account_transactions import BankAccountTransactions
from .bank_accounts import BankAccounts
from .bill_credit_notes import BillCreditNotes
from .bill_payments import BillPayments
from .bills import Bills
from .company_info import CompanyInfo
from .credit_notes import CreditNotes
from .customers import Customers
from .direct_costs import DirectCosts
from .direct_incomes import DirectIncomes
from .financials import Financials
from .invoices import Invoices
from .items import Items
from .journal_entries import JournalEntries
from .journals import Journals
from .payment_methods import PaymentMethods
from .payments import Payments
from .purchase_orders import PurchaseOrders
from .reports import Reports
from .sales_orders import SalesOrders
from .suppliers import Suppliers
from .tax_rates import TaxRates
from .tracking_categories import TrackingCategories
from .transfers import Transfers
from codat.models import shared

SERVERS = [
    "https://api.codat.io",
    r"""Production"""
]
"""Contains the list of servers available to the SDK"""

class Codat:
    r"""A flexible API for pulling accounting data, normalized and aggregated from 20 accounting integrations.
    
    Standardize how you connect to your customers’ accounting software. View, create, update, and delete data in the same way for all the leading accounting platforms.
    
    [Read more...](https://docs.codat.io/accounting-api/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas)    
    """
    account_transactions: AccountTransactions
    r"""Account transactions"""
    accounts: Accounts
    r"""Accounts"""
    bank_account_transactions: BankAccountTransactions
    r"""Bank transactions for bank accounts"""
    bank_accounts: BankAccounts
    r"""Bank accounts"""
    bill_credit_notes: BillCreditNotes
    r"""Bill credit notes"""
    bill_payments: BillPayments
    r"""Bill payments"""
    bills: Bills
    r"""Bills"""
    company_info: CompanyInfo
    r"""Company info"""
    credit_notes: CreditNotes
    r"""Credit notes"""
    customers: Customers
    r"""Customers"""
    direct_costs: DirectCosts
    r"""Direct costs"""
    direct_incomes: DirectIncomes
    r"""Direct incomes"""
    financials: Financials
    r"""Financials"""
    invoices: Invoices
    r"""Invoices"""
    items: Items
    r"""Items"""
    journal_entries: JournalEntries
    r"""Journal entries"""
    journals: Journals
    r"""Journals"""
    payment_methods: PaymentMethods
    r"""Payment methods"""
    payments: Payments
    r"""Payments"""
    purchase_orders: PurchaseOrders
    r"""Purchase orders"""
    reports: Reports
    r"""Reports"""
    sales_orders: SalesOrders
    r"""Sales orders"""
    suppliers: Suppliers
    r"""Suppliers"""
    tax_rates: TaxRates
    r"""Tax rates"""
    tracking_categories: TrackingCategories
    r"""Tracking categories"""
    transfers: Transfers
    r"""Transfers"""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.9.2"
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
        self.account_transactions = AccountTransactions(
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
        
        self.bank_account_transactions = BankAccountTransactions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bank_accounts = BankAccounts(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bill_credit_notes = BillCreditNotes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bill_payments = BillPayments(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bills = Bills(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.company_info = CompanyInfo(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.credit_notes = CreditNotes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.customers = Customers(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.direct_costs = DirectCosts(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.direct_incomes = DirectIncomes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.financials = Financials(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.invoices = Invoices(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.items = Items(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.journal_entries = JournalEntries(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.journals = Journals(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.payment_methods = PaymentMethods(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.payments = Payments(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.purchase_orders = PurchaseOrders(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.reports = Reports(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.sales_orders = SalesOrders(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.suppliers = Suppliers(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.tax_rates = TaxRates(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.tracking_categories = TrackingCategories(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transfers = Transfers(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    