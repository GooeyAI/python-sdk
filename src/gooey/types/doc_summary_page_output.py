# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .called_function_response import CalledFunctionResponse
from .prompt_tree_node import PromptTreeNode


class DocSummaryPageOutput(UniversalBaseModel):
    output_text: typing.List[str]
    prompt_tree: typing.Optional[typing.List[PromptTreeNode]] = None
    final_prompt: str
    called_functions: typing.Optional[typing.List[CalledFunctionResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
