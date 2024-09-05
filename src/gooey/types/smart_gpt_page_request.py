# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recipe_function import RecipeFunction
from .run_settings import RunSettings
from .smart_gpt_page_request_response_format_type import SmartGptPageRequestResponseFormatType
from .smart_gpt_page_request_selected_model import SmartGptPageRequestSelectedModel


class SmartGptPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    input_prompt: str
    cot_prompt: typing.Optional[str] = None
    reflexion_prompt: typing.Optional[str] = None
    dera_prompt: typing.Optional[str] = None
    selected_model: typing.Optional[SmartGptPageRequestSelectedModel] = None
    avoid_repetition: typing.Optional[bool] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[float] = None
    max_tokens: typing.Optional[int] = None
    sampling_temperature: typing.Optional[float] = None
    response_format_type: typing.Optional[SmartGptPageRequestResponseFormatType] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
