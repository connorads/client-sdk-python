"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import featurestate as shared_featurestate
from ..shared import featuretype as shared_featuretype
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SupportedFeature:
    feature_state: shared_featurestate.FeatureState = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('featureState') }})
    r"""The current release state of the feature."""
    feature_type: shared_featuretype.FeatureType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('featureType') }})
    r"""The type of feature."""
    

