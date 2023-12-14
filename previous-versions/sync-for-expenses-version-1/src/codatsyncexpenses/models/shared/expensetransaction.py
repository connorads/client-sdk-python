"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .contactref import ContactRef
from .expensetransactionline import ExpenseTransactionLine
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from enum import Enum
from typing import List, Optional

class Type(str, Enum):
    r"""The type of transaction."""
    PAYMENT = 'Payment'
    REFUND = 'Refund'
    REWARD = 'Reward'
    CHARGEBACK = 'Chargeback'
    TRANSFER_IN = 'TransferIn'
    TRANSFER_OUT = 'TransferOut'
    ADJUSTMENT_IN = 'AdjustmentIn'
    ADJUSTMENT_OUT = 'AdjustmentOut'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExpenseTransaction:
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""Currency the transaction was recorded in."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Your unique identifier for the transaction."""
    issue_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issueDate') }})
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
    type: Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of transaction."""
    contact_ref: Optional[ContactRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contactRef'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyRate'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.  

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places). 

    For accounting platforms which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

    ## Examples with base currency of GBP

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |

    ## Examples with base currency of USD

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, include the required currency rate in the expense transaction.  |
    """
    lines: Optional[List[ExpenseTransactionLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lines'), 'exclude': lambda f: f is None }})
    r"""Array of transaction lines."""
    merchant_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchantName'), 'exclude': lambda f: f is None }})
    r"""Name of the merchant where the purchase took place"""
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes'), 'exclude': lambda f: f is None }})
    r"""Any private, company notes about the transaction."""
    

