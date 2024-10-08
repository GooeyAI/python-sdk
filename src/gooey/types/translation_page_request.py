# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .recipe_function import RecipeFunction
import pydantic
from .translation_models import TranslationModels
from .run_settings import RunSettings
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TranslationPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    texts: typing.Optional[typing.List[str]] = None
    selected_model: typing.Optional[TranslationModels] = None
    translation_source: typing.Optional[str] = None
    translation_target: typing.Optional[str] = None
    glossary_document: typing.Optional[str] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
