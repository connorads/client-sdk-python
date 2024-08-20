"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productinventorylocation import ProductInventoryLocation, ProductInventoryLocationTypedDict
from codat_lending.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ProductInventoryTypedDict(TypedDict):
    r"""Information about the total inventory as well as the locations inventory is in."""
    
    locations: NotRequired[List[ProductInventoryLocationTypedDict]]
    total_quantity: NotRequired[Nullable[Decimal]]
    r"""The total quantity of stock remaining across locations."""
    

class ProductInventory(BaseModel):
    r"""Information about the total inventory as well as the locations inventory is in."""
    
    locations: Optional[List[ProductInventoryLocation]] = None
    total_quantity: Annotated[Annotated[OptionalNullable[Decimal], BeforeValidator(validate_decimal), PlainSerializer(serialize_decimal(False))], pydantic.Field(alias="totalQuantity")] = UNSET
    r"""The total quantity of stock remaining across locations."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["locations", "totalQuantity"]
        nullable_fields = ["totalQuantity"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
