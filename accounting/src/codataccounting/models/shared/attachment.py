"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Attachment:
    r"""The Codat API supports pulling and pushing of file attachments for invoices, bills, direct costs, and direct incomes.
    
    > **Retrieving attachments**
    > 
    > If a company is authorized, you can query the Codat API to read, download, and upload attachments without requiring a fresh sync of data.
    
    Unlike other data types, Codat doesn't support sync settings for attachments.
    
    View the coverage for accounts in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts\" target=\"_blank\">Data coverage explorer</a>.
    """
    
    content_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contentType'), 'exclude': lambda f: f is None }})

    r"""File type of the attachment. This is represented by appending the file type to the [IETF standard file naming requirements](https://tools.ietf.org/html/rfc6838). For example, for a jpeg file the output is **image/jpeg**.
    
    Supported file types vary per platform.
    """
    date_created: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dateCreated'), 'exclude': lambda f: f is None }})

    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:
    
    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```
    
    
    
    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:
    
    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`
    
    > Time zones
    > 
    > Not all dates from Codat will contain information about time zones.  
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """
    file_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fileSize'), 'exclude': lambda f: f is None }})

    r"""File size in bytes. For example, if this reads **46153**, then the file size is 46kb."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})

    r"""Identifier for the attachment, unique for the company in the accounting platform."""
    include_when_sent: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('includeWhenSent'), 'exclude': lambda f: f is None }})

    r"""If `true`, then the attachment is included with the associated invoice, bill or direct costs when it is printed, emailed, or sent to a customer, if the underlying accounting platform allows this."""
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})

    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})

    r"""Name of the attachment file."""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})

    