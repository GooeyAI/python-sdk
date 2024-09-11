# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .translate_request_functions_item_trigger import TranslateRequestFunctionsItemTrigger
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class TranslateRequestFunctionsItem(UniversalBaseModel):
    url: str
    trigger: TranslateRequestFunctionsItemTrigger = pydantic.Field()
    """
    When to run this function. `pre` runs before the recipe, `post` runs after the recipe.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
