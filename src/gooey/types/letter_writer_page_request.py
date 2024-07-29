# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recipe_function import RecipeFunction
from .run_settings import RunSettings
from .training_data_model import TrainingDataModel


class LetterWriterPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    action_id: str
    prompt_header: typing.Optional[str] = None
    example_letters: typing.Optional[typing.List[TrainingDataModel]] = None
    lm_selected_api: typing.Optional[str] = None
    lm_selected_engine: typing.Optional[str] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[float] = None
    lm_sampling_temperature: typing.Optional[float] = None
    api_http_method: typing.Optional[str] = None
    api_url: typing.Optional[str] = None
    api_headers: typing.Optional[str] = None
    api_json_body: typing.Optional[str] = None
    input_prompt: typing.Optional[str] = None
    strip_html2text: typing.Optional[bool] = pydantic.Field(alias="strip_html_2_text", default=None)
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow