# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .translation_page_output import TranslationPageOutput


class TranslationPageResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique ID for this run
    """

    url: str = pydantic.Field()
    """
    Web URL for this run
    """

    created_at: str = pydantic.Field()
    """
    Time when the run was created as ISO format
    """

    output: TranslationPageOutput = pydantic.Field()
    """
    Output of the run
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
