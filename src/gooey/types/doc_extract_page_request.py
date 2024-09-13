# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .recipe_function import RecipeFunction
import pydantic
from .asr_models import AsrModels
from .large_language_models import LargeLanguageModels
from .response_format_type import ResponseFormatType
from .run_settings import RunSettings
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DocExtractPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    documents: typing.List[str]
    sheet_url: typing.Optional[str] = None
    selected_asr_model: typing.Optional[AsrModels] = None
    google_translate_target: typing.Optional[str] = None
    glossary_document: typing.Optional[str] = None
    task_instructions: typing.Optional[str] = None
    selected_model: typing.Optional[LargeLanguageModels] = None
    avoid_repetition: typing.Optional[bool] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[float] = None
    max_tokens: typing.Optional[int] = None
    sampling_temperature: typing.Optional[float] = None
    response_format_type: typing.Optional[ResponseFormatType] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow