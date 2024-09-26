"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListBankingTransactionsRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    order_by: NotRequired[str]
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""
    page: NotRequired[int]
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""
    page_size: NotRequired[int]
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""
    query: NotRequired[str]
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""


class ListBankingTransactionsRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    connection_id: Annotated[
        str,
        pydantic.Field(alias="connectionId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a connection."""

    order_by: Annotated[
        Optional[str],
        pydantic.Field(alias="orderBy"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""

    query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""
