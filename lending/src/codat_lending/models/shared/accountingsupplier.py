"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountingaddress import AccountingAddress, AccountingAddressTypedDict
from .metadata import Metadata, MetadataTypedDict
from .supplementaldata import SupplementalData, SupplementalDataTypedDict
from .supplierstatus import SupplierStatus
from codat_lending.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AccountingSupplierTypedDict(TypedDict):
    r"""> View the coverage for suppliers in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    From the **Suppliers** endpoints, you can retrieve a list of [all the suppliers for a company](https://docs.codat.io/lending-api#/operations/list-suppliers). Suppliers' data links to accounts payable [bills](https://docs.codat.io/lending-api#/schemas/Bill).
    """

    status: SupplierStatus
    r"""Status of the supplier."""
    addresses: NotRequired[Nullable[List[AccountingAddressTypedDict]]]
    r"""An array of Addresses."""
    contact_name: NotRequired[Nullable[str]]
    r"""Name of the main contact for the supplier."""
    default_currency: NotRequired[Nullable[str]]
    r"""Default currency the supplier's transactional data is recorded in."""
    email_address: NotRequired[Nullable[str]]
    r"""Email address that the supplier may be contacted on."""
    id: NotRequired[str]
    r"""Identifier for the supplier, unique to the company in the accounting software."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    phone: NotRequired[Nullable[str]]
    r"""Phone number that the supplier may be contacted on."""
    registration_number: NotRequired[Nullable[str]]
    r"""Company number of the supplier. In the UK, this is typically the company registration number issued by Companies House."""
    source_modified_date: NotRequired[str]
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    supplier_name: NotRequired[Nullable[str]]
    r"""Name of the supplier as recorded in the accounting system, typically the company name."""
    tax_number: NotRequired[Nullable[str]]
    r"""Supplier's company tax number."""


class AccountingSupplier(BaseModel):
    r"""> View the coverage for suppliers in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    From the **Suppliers** endpoints, you can retrieve a list of [all the suppliers for a company](https://docs.codat.io/lending-api#/operations/list-suppliers). Suppliers' data links to accounts payable [bills](https://docs.codat.io/lending-api#/schemas/Bill).
    """

    status: SupplierStatus
    r"""Status of the supplier."""

    addresses: OptionalNullable[List[AccountingAddress]] = UNSET
    r"""An array of Addresses."""

    contact_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="contactName")
    ] = UNSET
    r"""Name of the main contact for the supplier."""

    default_currency: Annotated[
        OptionalNullable[str], pydantic.Field(alias="defaultCurrency")
    ] = UNSET
    r"""Default currency the supplier's transactional data is recorded in."""

    email_address: Annotated[
        OptionalNullable[str], pydantic.Field(alias="emailAddress")
    ] = UNSET
    r"""Email address that the supplier may be contacted on."""

    id: Optional[str] = None
    r"""Identifier for the supplier, unique to the company in the accounting software."""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    phone: OptionalNullable[str] = UNSET
    r"""Phone number that the supplier may be contacted on."""

    registration_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="registrationNumber")
    ] = UNSET
    r"""Company number of the supplier. In the UK, this is typically the company registration number issued by Companies House."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    supplemental_data: Annotated[
        Optional[SupplementalData], pydantic.Field(alias="supplementalData")
    ] = None
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    supplier_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="supplierName")
    ] = UNSET
    r"""Name of the supplier as recorded in the accounting system, typically the company name."""

    tax_number: Annotated[OptionalNullable[str], pydantic.Field(alias="taxNumber")] = (
        UNSET
    )
    r"""Supplier's company tax number."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "addresses",
            "contactName",
            "defaultCurrency",
            "emailAddress",
            "id",
            "metadata",
            "modifiedDate",
            "phone",
            "registrationNumber",
            "sourceModifiedDate",
            "supplementalData",
            "supplierName",
            "taxNumber",
        ]
        nullable_fields = [
            "addresses",
            "contactName",
            "defaultCurrency",
            "emailAddress",
            "phone",
            "registrationNumber",
            "supplierName",
            "taxNumber",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
