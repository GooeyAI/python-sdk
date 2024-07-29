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
from ..types.failed_reponse_model_v2 import FailedReponseModelV2
from ..types.generic_error_response import GenericErrorResponse
from ..types.http_validation_error import HttpValidationError
from ..types.recipe_function import RecipeFunction
from ..types.related_qn_a_page_request_embedding_model import RelatedQnAPageRequestEmbeddingModel
from ..types.related_qn_a_page_request_selected_model import RelatedQnAPageRequestSelectedModel
from ..types.related_qn_a_page_response import RelatedQnAPageResponse
from ..types.related_qn_a_page_status_response import RelatedQnAPageStatusResponse
from ..types.run_settings import RunSettings
from ..types.serp_search_location import SerpSearchLocation
from ..types.serp_search_type import SerpSearchType

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GeneratePeopleAlsoAskSeoContentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def related_qna_maker(
        self,
        *,
        search_query: str,
        site_filter: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        serp_search_location: typing.Optional[SerpSearchLocation] = OMIT,
        scaleserp_locations: typing.Optional[typing.Sequence[str]] = OMIT,
        serp_search_type: typing.Optional[SerpSearchType] = OMIT,
        scaleserp_search_field: typing.Optional[str] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[RelatedQnAPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        max_search_urls: typing.Optional[int] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        embedding_model: typing.Optional[RelatedQnAPageRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> RelatedQnAPageResponse:
        """
        Parameters
        ----------
        search_query : str

        site_filter : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        serp_search_location : typing.Optional[SerpSearchLocation]

        scaleserp_locations : typing.Optional[typing.Sequence[str]]
            DEPRECATED: use `serp_search_location` instead

        serp_search_type : typing.Optional[SerpSearchType]

        scaleserp_search_field : typing.Optional[str]
            DEPRECATED: use `serp_search_type` instead

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        selected_model : typing.Optional[RelatedQnAPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        max_search_urls : typing.Optional[int]

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        embedding_model : typing.Optional[RelatedQnAPageRequestEmbeddingModel]

        dense_weight : typing.Optional[float]
            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelatedQnAPageResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.generate_people_also_ask_seo_content.related_qna_maker(
            search_query="search_query",
            site_filter="site_filter",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/related-qna-maker/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "serp_search_location": serp_search_location,
                "scaleserp_locations": scaleserp_locations,
                "serp_search_type": serp_search_type,
                "scaleserp_search_field": scaleserp_search_field,
                "search_query": search_query,
                "site_filter": site_filter,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "max_search_urls": max_search_urls,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(RelatedQnAPageResponse, parse_obj_as(type_=RelatedQnAPageResponse, object_=_response.json()))  # type: ignore
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

    def async_related_qna_maker(
        self,
        *,
        search_query: str,
        site_filter: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        serp_search_location: typing.Optional[SerpSearchLocation] = OMIT,
        scaleserp_locations: typing.Optional[typing.Sequence[str]] = OMIT,
        serp_search_type: typing.Optional[SerpSearchType] = OMIT,
        scaleserp_search_field: typing.Optional[str] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[RelatedQnAPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        max_search_urls: typing.Optional[int] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        embedding_model: typing.Optional[RelatedQnAPageRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        search_query : str

        site_filter : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        serp_search_location : typing.Optional[SerpSearchLocation]

        scaleserp_locations : typing.Optional[typing.Sequence[str]]
            DEPRECATED: use `serp_search_location` instead

        serp_search_type : typing.Optional[SerpSearchType]

        scaleserp_search_field : typing.Optional[str]
            DEPRECATED: use `serp_search_type` instead

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        selected_model : typing.Optional[RelatedQnAPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        max_search_urls : typing.Optional[int]

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        embedding_model : typing.Optional[RelatedQnAPageRequestEmbeddingModel]

        dense_weight : typing.Optional[float]
            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.

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
        client.generate_people_also_ask_seo_content.async_related_qna_maker(
            search_query="search_query",
            site_filter="site_filter",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/related-qna-maker/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "serp_search_location": serp_search_location,
                "scaleserp_locations": scaleserp_locations,
                "serp_search_type": serp_search_type,
                "scaleserp_search_field": scaleserp_search_field,
                "search_query": search_query,
                "site_filter": site_filter,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "max_search_urls": max_search_urls,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
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

    def status_related_qna_maker(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RelatedQnAPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelatedQnAPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.generate_people_also_ask_seo_content.status_related_qna_maker(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/related-qna-maker/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(RelatedQnAPageStatusResponse, parse_obj_as(type_=RelatedQnAPageStatusResponse, object_=_response.json()))  # type: ignore
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


class AsyncGeneratePeopleAlsoAskSeoContentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def related_qna_maker(
        self,
        *,
        search_query: str,
        site_filter: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        serp_search_location: typing.Optional[SerpSearchLocation] = OMIT,
        scaleserp_locations: typing.Optional[typing.Sequence[str]] = OMIT,
        serp_search_type: typing.Optional[SerpSearchType] = OMIT,
        scaleserp_search_field: typing.Optional[str] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[RelatedQnAPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        max_search_urls: typing.Optional[int] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        embedding_model: typing.Optional[RelatedQnAPageRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> RelatedQnAPageResponse:
        """
        Parameters
        ----------
        search_query : str

        site_filter : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        serp_search_location : typing.Optional[SerpSearchLocation]

        scaleserp_locations : typing.Optional[typing.Sequence[str]]
            DEPRECATED: use `serp_search_location` instead

        serp_search_type : typing.Optional[SerpSearchType]

        scaleserp_search_field : typing.Optional[str]
            DEPRECATED: use `serp_search_type` instead

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        selected_model : typing.Optional[RelatedQnAPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        max_search_urls : typing.Optional[int]

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        embedding_model : typing.Optional[RelatedQnAPageRequestEmbeddingModel]

        dense_weight : typing.Optional[float]
            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelatedQnAPageResponse
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
            await client.generate_people_also_ask_seo_content.related_qna_maker(
                search_query="search_query",
                site_filter="site_filter",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/related-qna-maker/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "serp_search_location": serp_search_location,
                "scaleserp_locations": scaleserp_locations,
                "serp_search_type": serp_search_type,
                "scaleserp_search_field": scaleserp_search_field,
                "search_query": search_query,
                "site_filter": site_filter,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "max_search_urls": max_search_urls,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(RelatedQnAPageResponse, parse_obj_as(type_=RelatedQnAPageResponse, object_=_response.json()))  # type: ignore
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

    async def async_related_qna_maker(
        self,
        *,
        search_query: str,
        site_filter: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        serp_search_location: typing.Optional[SerpSearchLocation] = OMIT,
        scaleserp_locations: typing.Optional[typing.Sequence[str]] = OMIT,
        serp_search_type: typing.Optional[SerpSearchType] = OMIT,
        scaleserp_search_field: typing.Optional[str] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[RelatedQnAPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        max_search_urls: typing.Optional[int] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        embedding_model: typing.Optional[RelatedQnAPageRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        search_query : str

        site_filter : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        serp_search_location : typing.Optional[SerpSearchLocation]

        scaleserp_locations : typing.Optional[typing.Sequence[str]]
            DEPRECATED: use `serp_search_location` instead

        serp_search_type : typing.Optional[SerpSearchType]

        scaleserp_search_field : typing.Optional[str]
            DEPRECATED: use `serp_search_type` instead

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        selected_model : typing.Optional[RelatedQnAPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        max_search_urls : typing.Optional[int]

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        embedding_model : typing.Optional[RelatedQnAPageRequestEmbeddingModel]

        dense_weight : typing.Optional[float]
            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.

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
            await client.generate_people_also_ask_seo_content.async_related_qna_maker(
                search_query="search_query",
                site_filter="site_filter",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/related-qna-maker/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "serp_search_location": serp_search_location,
                "scaleserp_locations": scaleserp_locations,
                "serp_search_type": serp_search_type,
                "scaleserp_search_field": scaleserp_search_field,
                "search_query": search_query,
                "site_filter": site_filter,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "max_search_urls": max_search_urls,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
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

    async def status_related_qna_maker(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RelatedQnAPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelatedQnAPageStatusResponse
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
            await client.generate_people_also_ask_seo_content.status_related_qna_maker(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/related-qna-maker/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(RelatedQnAPageStatusResponse, parse_obj_as(type_=RelatedQnAPageStatusResponse, object_=_response.json()))  # type: ignore
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