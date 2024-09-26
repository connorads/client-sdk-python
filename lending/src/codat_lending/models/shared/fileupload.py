"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .codatfile import CodatFile, CodatFileTypedDict
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class FileUploadTypedDict(TypedDict):
    file: CodatFileTypedDict
    r"""The file to be uploaded as an attachment."""


class FileUpload(BaseModel):
    file: Annotated[
        CodatFile,
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(file=True)),
    ]
    r"""The file to be uploaded as an attachment."""
