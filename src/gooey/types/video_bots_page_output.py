# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .called_function_response import CalledFunctionResponse
from .reply_button import ReplyButton
from .search_reference import SearchReference
from .video_bots_page_output_final_keyword_query import VideoBotsPageOutputFinalKeywordQuery
from .video_bots_page_output_final_prompt import VideoBotsPageOutputFinalPrompt


class VideoBotsPageOutput(UniversalBaseModel):
    final_prompt: typing.Optional[VideoBotsPageOutputFinalPrompt] = None
    output_text: typing.Optional[typing.List[str]] = None
    output_audio: typing.Optional[typing.List[str]] = None
    output_video: typing.Optional[typing.List[str]] = None
    raw_input_text: typing.Optional[str] = None
    raw_tts_text: typing.Optional[typing.List[str]] = None
    raw_output_text: typing.Optional[typing.List[str]] = None
    references: typing.Optional[typing.List[SearchReference]] = None
    final_search_query: typing.Optional[str] = None
    final_keyword_query: typing.Optional[VideoBotsPageOutputFinalKeywordQuery] = None
    output_documents: typing.Optional[typing.List[str]] = None
    reply_buttons: typing.Optional[typing.List[ReplyButton]] = None
    finish_reason: typing.Optional[typing.List[str]] = None
    called_functions: typing.Optional[typing.List[CalledFunctionResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow