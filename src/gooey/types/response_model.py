# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .reply_button import ReplyButton
from .response_model_final_keyword_query import ResponseModelFinalKeywordQuery
from .response_model_final_prompt import ResponseModelFinalPrompt
from .search_reference import SearchReference


class ResponseModel(pydantic_v1.BaseModel):
    final_prompt: typing.Optional[ResponseModelFinalPrompt] = None
    output_text: typing.Optional[typing.List[str]] = None
    output_audio: typing.Optional[typing.List[str]] = None
    output_video: typing.Optional[typing.List[str]] = None
    raw_input_text: typing.Optional[str] = None
    raw_tts_text: typing.Optional[typing.List[str]] = None
    raw_output_text: typing.Optional[typing.List[str]] = None
    references: typing.Optional[typing.List[SearchReference]] = None
    final_search_query: typing.Optional[str] = None
    final_keyword_query: typing.Optional[ResponseModelFinalKeywordQuery] = None
    output_documents: typing.Optional[typing.List[str]] = None
    reply_buttons: typing.Optional[typing.List[ReplyButton]] = None
    finish_reason: typing.Optional[typing.List[str]] = None

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
