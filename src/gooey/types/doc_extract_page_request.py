# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .doc_extract_page_request_selected_asr_model import DocExtractPageRequestSelectedAsrModel
from .doc_extract_page_request_selected_model import DocExtractPageRequestSelectedModel
from .recipe_function import RecipeFunction
from .run_settings import RunSettings


class DocExtractPageRequest(pydantic_v1.BaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    documents: typing.List[str]
    sheet_url: typing.Optional[str] = None
    selected_asr_model: typing.Optional[DocExtractPageRequestSelectedAsrModel] = None
    google_translate_target: typing.Optional[str] = None
    glossary_document: typing.Optional[str] = pydantic_v1.Field(default=None)
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
    settings: typing.Optional[RunSettings] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
