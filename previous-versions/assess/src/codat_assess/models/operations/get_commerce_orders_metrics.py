"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_assess.models.shared import periodunit as shared_periodunit
from codat_assess.types import BaseModel
from codat_assess.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetCommerceOrdersMetricsRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    number_of_periods: int
    r"""The number of periods to return. There will be no pagination as a query parameter."""
    period_length: int
    r"""The number of months per period. E.g. 2 = 2 months per period."""
    period_unit: shared_periodunit.PeriodUnit
    r"""The period unit of time returned."""
    report_date: str
    r"""The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month."""
    include_display_names: NotRequired[bool]
    r"""Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable."""


class GetCommerceOrdersMetricsRequest(BaseModel):
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

    number_of_periods: Annotated[
        int,
        pydantic.Field(alias="numberOfPeriods"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The number of periods to return. There will be no pagination as a query parameter."""

    period_length: Annotated[
        int,
        pydantic.Field(alias="periodLength"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The number of months per period. E.g. 2 = 2 months per period."""

    period_unit: Annotated[
        shared_periodunit.PeriodUnit,
        pydantic.Field(alias="periodUnit"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The period unit of time returned."""

    report_date: Annotated[
        str,
        pydantic.Field(alias="reportDate"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month."""

    include_display_names: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeDisplayNames"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable."""
