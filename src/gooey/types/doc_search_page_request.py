# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_search_page_request_citation_style import DocSearchPageRequestCitationStyle
from .doc_search_page_request_embedding_model import DocSearchPageRequestEmbeddingModel
from .doc_search_page_request_keyword_query import DocSearchPageRequestKeywordQuery
from .doc_search_page_request_selected_model import DocSearchPageRequestSelectedModel
from .recipe_function import RecipeFunction
from .run_settings import RunSettings


class DocSearchPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    search_query: str
    keyword_query: typing.Optional[DocSearchPageRequestKeywordQuery] = None
    documents: typing.Optional[typing.List[str]] = None
    max_references: typing.Optional[int] = None
    max_context_words: typing.Optional[int] = None
    scroll_jump: typing.Optional[int] = None
    doc_extract_url: typing.Optional[str] = None
    embedding_model: typing.Optional[DocSearchPageRequestEmbeddingModel] = None
    dense_weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
    Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    """

    task_instructions: typing.Optional[str] = None
    query_instructions: typing.Optional[str] = None
    selected_model: typing.Optional[DocSearchPageRequestSelectedModel] = None
    avoid_repetition: typing.Optional[bool] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[float] = None
    max_tokens: typing.Optional[int] = None
    sampling_temperature: typing.Optional[float] = None
    citation_style: typing.Optional[DocSearchPageRequestCitationStyle] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
