"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.models.shared import excelreporttypes as shared_excelreporttypes
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class GetExcelReportGenerationStatusRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    report_type: shared_excelreporttypes.ExcelReportTypes
    r"""The type of report you want to generate and download."""


class GetExcelReportGenerationStatusRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    report_type: Annotated[
        shared_excelreporttypes.ExcelReportTypes,
        pydantic.Field(alias="reportType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The type of report you want to generate and download."""
