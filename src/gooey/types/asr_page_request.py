# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .asr_page_request_functions_item import AsrPageRequestFunctionsItem
import pydantic
from .asr_page_request_selected_model import AsrPageRequestSelectedModel
from .asr_page_request_translation_model import AsrPageRequestTranslationModel
from .asr_page_request_output_format import AsrPageRequestOutputFormat
from .run_settings import RunSettings
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AsrPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[AsrPageRequestFunctionsItem]] = None
    variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    documents: typing.List[str]
    selected_model: typing.Optional[AsrPageRequestSelectedModel] = None
    language: typing.Optional[str] = None
    translation_model: typing.Optional[AsrPageRequestTranslationModel] = None
    output_format: typing.Optional[AsrPageRequestOutputFormat] = None
    google_translate_target: typing.Optional[str] = pydantic.Field(default=None)
    """
    use `translation_model` & `translation_target` instead.
    """

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