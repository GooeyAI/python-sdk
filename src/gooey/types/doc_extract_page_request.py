# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_extract_page_request_response_format_type import DocExtractPageRequestResponseFormatType
from .doc_extract_page_request_selected_asr_model import DocExtractPageRequestSelectedAsrModel
from .doc_extract_page_request_selected_model import DocExtractPageRequestSelectedModel
from .recipe_function import RecipeFunction
from .run_settings import RunSettings


class DocExtractPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    documents: typing.List[str]
    sheet_url: typing.Optional[str] = None
    selected_asr_model: typing.Optional[DocExtractPageRequestSelectedAsrModel] = None
    google_translate_target: typing.Optional[str] = None
    glossary_document: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provide a glossary to customize translation and improve accuracy of domain-specific terms.
    If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).
    """

    task_instructions: typing.Optional[str] = None
    selected_model: typing.Optional[DocExtractPageRequestSelectedModel] = None
    avoid_repetition: typing.Optional[bool] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[float] = None
    max_tokens: typing.Optional[int] = None
    sampling_temperature: typing.Optional[float] = None
    response_format_type: typing.Optional[DocExtractPageRequestResponseFormatType] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
