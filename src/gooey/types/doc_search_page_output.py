# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .search_reference import SearchReference
from .called_function_response import CalledFunctionResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DocSearchPageOutput(UniversalBaseModel):
    output_text: typing.List[str]
    references: typing.List[SearchReference]
    final_prompt: str
    final_search_query: typing.Optional[str] = None
    called_functions: typing.Optional[typing.List[CalledFunctionResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
