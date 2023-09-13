"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import paymentlinelink as shared_paymentlinelink
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PaymentLine:
    amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Amount in the payment currency."""
    allocated_on_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allocatedOnDate'), 'exclude': lambda f: f is None }})
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
    links: Optional[list[shared_paymentlinelink.PaymentLineLink]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('links'), 'exclude': lambda f: f is None }})
    

