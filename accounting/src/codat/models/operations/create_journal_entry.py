"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntrySourceModifiedDateJournalLinesAccountRef:
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' from the Accounts data type."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""'name' from the Accounts data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntrySourceModifiedDateJournalLinesTracking:
    r"""List of record refs associated with the tracking information for the line (eg to a Tracking Category, or customer etc.)"""
    
    record_refs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRefs'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntrySourceModifiedDateJournalLines:
    
    net_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netAmount') }})
    r"""Amount for the journal line. Debit entries are considered positive, and credit entries are considered negative."""  
    account_ref: Optional[CreateJournalEntrySourceModifiedDateJournalLinesAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""Currency for the journal line item."""  
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the journal line item."""  
    tracking: Optional[CreateJournalEntrySourceModifiedDateJournalLinesTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})
    r"""List of record refs associated with the tracking information for the line (eg to a Tracking Category, or customer etc.)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntrySourceModifiedDateJournalRef:
    r"""Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals)."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""GUID of the underlying journal."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Journal name, 256 characters max."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntrySourceModifiedDateMetadata:
    
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the record has been deleted in the third-party system this record originated from."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntrySourceModifiedDateRecordRef:
    r"""Links to the underlying record or data type.
    
    Found on:
    
    - Journal entries
    - Account transactions
    - Invoices
    - Transfers
    """
    
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Name of the 'dataType'."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' of the underlying record or data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntrySourceModifiedDateSupplementalData:
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""
    
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntrySourceModifiedDate:
    r"""> **Language tip:** For the top-level record of a company's financial transactions, refer to the [Journals](https://docs.codat.io/accounting-api#/schemas/Journal) data type
    
    > View the coverage for journal entries in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A journal entry report shows the entries made in a company's general ledger, or [accounts](https://api.codat.io/swagger/index.html#/Accounts/get_companies__companyId__data_accounts), when transactions are approved. The journal line items for each journal entry should balance.
    
    A journal entry line item is a single transaction line on the journal entry. For example: 
    
    - When a journal entry is recording a receipt of cash, the credit to accounts receivable and the debit to cash are separate line items. 
    - When a company needs to recognise revenue from an annual contract on a monthly basis, on receipt of cash for month one, they make a debit to deferred income and a credit to revenue.
    
    In Codat a journal entry contains details of:
    
    - The date on which the entry was created and posted.
    - Itemised lines, including amounts and currency.
    - A reference to the associated accounts.
    - A reference to the underlying record. For example, the invoice, bill, or other data type that triggered the posting of the journal entry to the general ledger. 
    
    > **Pushing journal entries **  
    > Codat only supports journal entries in the base currency of the company that are pushed into accounts denominated in the same base currency.
    """
    
    created_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdOn'), 'exclude': lambda f: f is None }})
    r"""Date on which the journal was created in the accounting platform."""  
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Optional description of the journal entry."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the journal entry for the company in the accounting platform."""  
    journal_lines: Optional[list[CreateJournalEntrySourceModifiedDateJournalLines]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journalLines'), 'exclude': lambda f: f is None }})
    r"""An array of journal lines."""  
    journal_ref: Optional[CreateJournalEntrySourceModifiedDateJournalRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journalRef'), 'exclude': lambda f: f is None }})
    r"""Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals)."""  
    metadata: Optional[CreateJournalEntrySourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    posted_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postedOn'), 'exclude': lambda f: f is None }})
    r"""Date on which the journal entry was posted to the accounting platform, and had an impact on the general ledger. This may be different from the creation date.
    
    For example, a user creates a journal entry on Monday and saves it as draft, which has no impact on the general ledger. On Thursday, they return to the entry and post it.
    
    The **createdOn** date shows as Monday.
    The **postedOn** date shows as Thursday.
    Journal entries can also be backdated, so the **postedOn** date may be earlier than the **createdOn** date.
    """  
    record_ref: Optional[CreateJournalEntrySourceModifiedDateRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})
    r"""Links to the underlying record or data type.
    
    Found on:
    
    - Journal entries
    - Account transactions
    - Invoices
    - Transfers
    """  
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    supplemental_data: Optional[CreateJournalEntrySourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""  
    updated_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedOn'), 'exclude': lambda f: f is None }})
    r"""Date on which the journal was last updated in the accounting platform."""  
    

@dataclasses.dataclass
class CreateJournalEntryRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    request_body: Optional[CreateJournalEntrySourceModifiedDate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONChangesPushOperationRecordRef:
    
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})  
    
class CreateJournalEntry200ApplicationJSONChangesTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREATED = "Created"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    ATTACHMENT_UPLOADED = "AttachmentUploaded"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONChanges:
    
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachmentId'), 'exclude': lambda f: f is None }})  
    record_ref: Optional[CreateJournalEntry200ApplicationJSONChangesPushOperationRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})  
    type: Optional[CreateJournalEntry200ApplicationJSONChangesTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONSourceModifiedDateJournalLinesAccountRef:
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' from the Accounts data type."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""'name' from the Accounts data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONSourceModifiedDateJournalLinesTracking:
    r"""List of record refs associated with the tracking information for the line (eg to a Tracking Category, or customer etc.)"""
    
    record_refs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRefs'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONSourceModifiedDateJournalLines:
    
    net_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netAmount') }})
    r"""Amount for the journal line. Debit entries are considered positive, and credit entries are considered negative."""  
    account_ref: Optional[CreateJournalEntry200ApplicationJSONSourceModifiedDateJournalLinesAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""  
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""Currency for the journal line item."""  
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description of the journal line item."""  
    tracking: Optional[CreateJournalEntry200ApplicationJSONSourceModifiedDateJournalLinesTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})
    r"""List of record refs associated with the tracking information for the line (eg to a Tracking Category, or customer etc.)"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONSourceModifiedDateJournalRef:
    r"""Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals)."""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""GUID of the underlying journal."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Journal name, 256 characters max."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONSourceModifiedDateMetadata:
    
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDeleted'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the record has been deleted in the third-party system this record originated from."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONSourceModifiedDateRecordRef:
    r"""Links to the underlying record or data type.
    
    Found on:
    
    - Journal entries
    - Account transactions
    - Invoices
    - Transfers
    """
    
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Name of the 'dataType'."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' of the underlying record or data type."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONSourceModifiedDateSupplementalData:
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""
    
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONSourceModifiedDate:
    r"""> **Language tip:** For the top-level record of a company's financial transactions, refer to the [Journals](https://docs.codat.io/accounting-api#/schemas/Journal) data type
    
    > View the coverage for journal entries in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A journal entry report shows the entries made in a company's general ledger, or [accounts](https://api.codat.io/swagger/index.html#/Accounts/get_companies__companyId__data_accounts), when transactions are approved. The journal line items for each journal entry should balance.
    
    A journal entry line item is a single transaction line on the journal entry. For example: 
    
    - When a journal entry is recording a receipt of cash, the credit to accounts receivable and the debit to cash are separate line items. 
    - When a company needs to recognise revenue from an annual contract on a monthly basis, on receipt of cash for month one, they make a debit to deferred income and a credit to revenue.
    
    In Codat a journal entry contains details of:
    
    - The date on which the entry was created and posted.
    - Itemised lines, including amounts and currency.
    - A reference to the associated accounts.
    - A reference to the underlying record. For example, the invoice, bill, or other data type that triggered the posting of the journal entry to the general ledger. 
    
    > **Pushing journal entries **  
    > Codat only supports journal entries in the base currency of the company that are pushed into accounts denominated in the same base currency.
    """
    
    created_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdOn'), 'exclude': lambda f: f is None }})
    r"""Date on which the journal was created in the accounting platform."""  
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Optional description of the journal entry."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the journal entry for the company in the accounting platform."""  
    journal_lines: Optional[list[CreateJournalEntry200ApplicationJSONSourceModifiedDateJournalLines]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journalLines'), 'exclude': lambda f: f is None }})
    r"""An array of journal lines."""  
    journal_ref: Optional[CreateJournalEntry200ApplicationJSONSourceModifiedDateJournalRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journalRef'), 'exclude': lambda f: f is None }})
    r"""Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals)."""  
    metadata: Optional[CreateJournalEntry200ApplicationJSONSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in Codat."""  
    posted_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postedOn'), 'exclude': lambda f: f is None }})
    r"""Date on which the journal entry was posted to the accounting platform, and had an impact on the general ledger. This may be different from the creation date.
    
    For example, a user creates a journal entry on Monday and saves it as draft, which has no impact on the general ledger. On Thursday, they return to the entry and post it.
    
    The **createdOn** date shows as Monday.
    The **postedOn** date shows as Thursday.
    Journal entries can also be backdated, so the **postedOn** date may be earlier than the **createdOn** date.
    """  
    record_ref: Optional[CreateJournalEntry200ApplicationJSONSourceModifiedDateRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})
    r"""Links to the underlying record or data type.
    
    Found on:
    
    - Journal entries
    - Account transactions
    - Invoices
    - Transfers
    """  
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this record was last modified in the originating system"""  
    supplemental_data: Optional[CreateJournalEntry200ApplicationJSONSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    r"""Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more."""  
    updated_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedOn'), 'exclude': lambda f: f is None }})
    r"""Date on which the journal was last updated in the accounting platform."""  
    
class CreateJournalEntry200ApplicationJSONStatusEnum(str, Enum):
    r"""The status of the push operation."""
    PENDING = "Pending"
    FAILED = "Failed"
    SUCCESS = "Success"
    TIMED_OUT = "TimedOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONValidationValidationItem:
    
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemId'), 'exclude': lambda f: f is None }})  
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})  
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validatorName'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSONValidation:
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""
    
    errors: Optional[list[CreateJournalEntry200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})  
    warnings: Optional[list[CreateJournalEntry200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateJournalEntry200ApplicationJSON:
    r"""Success"""
    
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId') }})
    r"""Unique identifier for your SMB in Codat."""  
    data_connection_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataConnectionKey') }})
    r"""Unique identifier for a company's data connection."""  
    push_operation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pushOperationKey') }})
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""  
    requested_on_utc: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestedOnUtc') }})
    r"""The datetime when the push was requested."""  
    status: CreateJournalEntry200ApplicationJSONStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the push operation."""  
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})  
    changes: Optional[list[CreateJournalEntry200ApplicationJSONChanges]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changes'), 'exclude': lambda f: f is None }})  
    completed_on_utc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completedOnUtc'), 'exclude': lambda f: f is None }})
    r"""The datetime when the push was completed, null if Pending."""  
    data: Optional[CreateJournalEntry200ApplicationJSONSourceModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""> **Language tip:** For the top-level record of a company's financial transactions, refer to the [Journals](https://docs.codat.io/accounting-api#/schemas/Journal) data type
    
    > View the coverage for journal entries in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A journal entry report shows the entries made in a company's general ledger, or [accounts](https://api.codat.io/swagger/index.html#/Accounts/get_companies__companyId__data_accounts), when transactions are approved. The journal line items for each journal entry should balance.
    
    A journal entry line item is a single transaction line on the journal entry. For example: 
    
    - When a journal entry is recording a receipt of cash, the credit to accounts receivable and the debit to cash are separate line items. 
    - When a company needs to recognise revenue from an annual contract on a monthly basis, on receipt of cash for month one, they make a debit to deferred income and a credit to revenue.
    
    In Codat a journal entry contains details of:
    
    - The date on which the entry was created and posted.
    - Itemised lines, including amounts and currency.
    - A reference to the associated accounts.
    - A reference to the underlying record. For example, the invoice, bill, or other data type that triggered the posting of the journal entry to the general ledger. 
    
    > **Pushing journal entries **  
    > Codat only supports journal entries in the base currency of the company that are pushed into accounts denominated in the same base currency.
    """  
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""The type of data being pushed, eg invoices, customers."""  
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage'), 'exclude': lambda f: f is None }})  
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInMinutes'), 'exclude': lambda f: f is None }})  
    timeout_in_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutInSeconds'), 'exclude': lambda f: f is None }})  
    validation: Optional[CreateJournalEntry200ApplicationJSONValidation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""  
    

@dataclasses.dataclass
class CreateJournalEntryResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    create_journal_entry_200_application_json_object: Optional[CreateJournalEntry200ApplicationJSON] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    