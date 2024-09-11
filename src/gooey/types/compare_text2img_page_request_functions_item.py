# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .compare_text2img_page_request_functions_item_trigger import CompareText2ImgPageRequestFunctionsItemTrigger
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class CompareText2ImgPageRequestFunctionsItem(UniversalBaseModel):
    url: str
    trigger: CompareText2ImgPageRequestFunctionsItemTrigger = pydantic.Field()
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