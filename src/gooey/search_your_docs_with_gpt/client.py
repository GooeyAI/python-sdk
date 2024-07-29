# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.async_api_response_model_v3 import AsyncApiResponseModelV3
from ..types.doc_search_page_request_citation_style import DocSearchPageRequestCitationStyle
from ..types.doc_search_page_request_embedding_model import DocSearchPageRequestEmbeddingModel
from ..types.doc_search_page_request_keyword_query import DocSearchPageRequestKeywordQuery
from ..types.doc_search_page_request_selected_model import DocSearchPageRequestSelectedModel
from ..types.doc_search_page_response import DocSearchPageResponse
from ..types.doc_search_page_status_response import DocSearchPageStatusResponse
from ..types.failed_reponse_model_v2 import FailedReponseModelV2
from ..types.generic_error_response import GenericErrorResponse
from ..types.http_validation_error import HttpValidationError
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SearchYourDocsWithGptClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def doc_search(
        self,
        *,
        search_query: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        keyword_query: typing.Optional[DocSearchPageRequestKeywordQuery] = OMIT,
        documents: typing.Optional[typing.Sequence[str]] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        doc_extract_url: typing.Optional[str] = OMIT,
        embedding_model: typing.Optional[DocSearchPageRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[DocSearchPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        citation_style: typing.Optional[DocSearchPageRequestCitationStyle] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> DocSearchPageResponse:
        """
        Parameters
        ----------
        search_query : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        keyword_query : typing.Optional[DocSearchPageRequestKeywordQuery]

        documents : typing.Optional[typing.Sequence[str]]

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        doc_extract_url : typing.Optional[str]

        embedding_model : typing.Optional[DocSearchPageRequestEmbeddingModel]

        dense_weight : typing.Optional[float]
            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        selected_model : typing.Optional[DocSearchPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        citation_style : typing.Optional[DocSearchPageRequestCitationStyle]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSearchPageResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.search_your_docs_with_gpt.doc_search(
            search_query="search_query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/doc-search/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "search_query": search_query,
                "keyword_query": keyword_query,
                "documents": documents,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "doc_extract_url": doc_extract_url,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "citation_style": citation_style,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(DocSearchPageResponse, parse_obj_as(type_=DocSearchPageResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(GenericErrorResponse, parse_obj_as(type_=GenericErrorResponse, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(FailedReponseModelV2, parse_obj_as(type_=FailedReponseModelV2, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def async_doc_search(
        self,
        *,
        search_query: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        keyword_query: typing.Optional[DocSearchPageRequestKeywordQuery] = OMIT,
        documents: typing.Optional[typing.Sequence[str]] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        doc_extract_url: typing.Optional[str] = OMIT,
        embedding_model: typing.Optional[DocSearchPageRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[DocSearchPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        citation_style: typing.Optional[DocSearchPageRequestCitationStyle] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        search_query : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        keyword_query : typing.Optional[DocSearchPageRequestKeywordQuery]

        documents : typing.Optional[typing.Sequence[str]]

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        doc_extract_url : typing.Optional[str]

        embedding_model : typing.Optional[DocSearchPageRequestEmbeddingModel]

        dense_weight : typing.Optional[float]
            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        selected_model : typing.Optional[DocSearchPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        citation_style : typing.Optional[DocSearchPageRequestCitationStyle]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncApiResponseModelV3
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.search_your_docs_with_gpt.async_doc_search(
            search_query="search_query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/doc-search/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "search_query": search_query,
                "keyword_query": keyword_query,
                "documents": documents,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "doc_extract_url": doc_extract_url,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "citation_style": citation_style,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AsyncApiResponseModelV3, parse_obj_as(type_=AsyncApiResponseModelV3, object_=_response.json()))  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(GenericErrorResponse, parse_obj_as(type_=GenericErrorResponse, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def status_doc_search(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DocSearchPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSearchPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.search_your_docs_with_gpt.status_doc_search(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/doc-search/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(DocSearchPageStatusResponse, parse_obj_as(type_=DocSearchPageStatusResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(GenericErrorResponse, parse_obj_as(type_=GenericErrorResponse, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSearchYourDocsWithGptClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def doc_search(
        self,
        *,
        search_query: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        keyword_query: typing.Optional[DocSearchPageRequestKeywordQuery] = OMIT,
        documents: typing.Optional[typing.Sequence[str]] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        doc_extract_url: typing.Optional[str] = OMIT,
        embedding_model: typing.Optional[DocSearchPageRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[DocSearchPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        citation_style: typing.Optional[DocSearchPageRequestCitationStyle] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> DocSearchPageResponse:
        """
        Parameters
        ----------
        search_query : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        keyword_query : typing.Optional[DocSearchPageRequestKeywordQuery]

        documents : typing.Optional[typing.Sequence[str]]

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        doc_extract_url : typing.Optional[str]

        embedding_model : typing.Optional[DocSearchPageRequestEmbeddingModel]

        dense_weight : typing.Optional[float]
            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        selected_model : typing.Optional[DocSearchPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        citation_style : typing.Optional[DocSearchPageRequestCitationStyle]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSearchPageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search_your_docs_with_gpt.doc_search(
                search_query="search_query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/doc-search/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "search_query": search_query,
                "keyword_query": keyword_query,
                "documents": documents,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "doc_extract_url": doc_extract_url,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "citation_style": citation_style,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(DocSearchPageResponse, parse_obj_as(type_=DocSearchPageResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(GenericErrorResponse, parse_obj_as(type_=GenericErrorResponse, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(FailedReponseModelV2, parse_obj_as(type_=FailedReponseModelV2, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def async_doc_search(
        self,
        *,
        search_query: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        keyword_query: typing.Optional[DocSearchPageRequestKeywordQuery] = OMIT,
        documents: typing.Optional[typing.Sequence[str]] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        doc_extract_url: typing.Optional[str] = OMIT,
        embedding_model: typing.Optional[DocSearchPageRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[DocSearchPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        citation_style: typing.Optional[DocSearchPageRequestCitationStyle] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        search_query : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        keyword_query : typing.Optional[DocSearchPageRequestKeywordQuery]

        documents : typing.Optional[typing.Sequence[str]]

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        doc_extract_url : typing.Optional[str]

        embedding_model : typing.Optional[DocSearchPageRequestEmbeddingModel]

        dense_weight : typing.Optional[float]
            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        selected_model : typing.Optional[DocSearchPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        citation_style : typing.Optional[DocSearchPageRequestCitationStyle]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncApiResponseModelV3
            Successful Response

        Examples
        --------
        import asyncio

        from gooey import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search_your_docs_with_gpt.async_doc_search(
                search_query="search_query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/doc-search/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "search_query": search_query,
                "keyword_query": keyword_query,
                "documents": documents,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "doc_extract_url": doc_extract_url,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "citation_style": citation_style,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AsyncApiResponseModelV3, parse_obj_as(type_=AsyncApiResponseModelV3, object_=_response.json()))  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(GenericErrorResponse, parse_obj_as(type_=GenericErrorResponse, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def status_doc_search(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DocSearchPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSearchPageStatusResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search_your_docs_with_gpt.status_doc_search(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/doc-search/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(DocSearchPageStatusResponse, parse_obj_as(type_=DocSearchPageStatusResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(GenericErrorResponse, parse_obj_as(type_=GenericErrorResponse, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)