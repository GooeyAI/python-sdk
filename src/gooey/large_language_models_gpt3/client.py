# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.async_api_response_model_v3 import AsyncApiResponseModelV3
from ..types.compare_llm_page_request_response_format_type import CompareLlmPageRequestResponseFormatType
from ..types.compare_llm_page_request_selected_models_item import CompareLlmPageRequestSelectedModelsItem
from ..types.compare_llm_page_response import CompareLlmPageResponse
from ..types.compare_llm_page_status_response import CompareLlmPageStatusResponse
from ..types.failed_reponse_model_v2 import FailedReponseModelV2
from ..types.generic_error_response import GenericErrorResponse
from ..types.http_validation_error import HttpValidationError
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class LargeLanguageModelsGpt3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def compare_llm(
        self,
        *,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        input_prompt: typing.Optional[str] = OMIT,
        selected_models: typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[CompareLlmPageRequestResponseFormatType] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> CompareLlmPageResponse:
        """
        Parameters
        ----------
        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        input_prompt : typing.Optional[str]

        selected_models : typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[CompareLlmPageRequestResponseFormatType]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareLlmPageResponse
            Successful Response

        Examples
        --------
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
        )
        client.large_language_models_gpt3.compare_llm()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/CompareLLM/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_prompt": input_prompt,
                "selected_models": selected_models,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "response_format_type": response_format_type,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CompareLlmPageResponse, _response.json())  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    pydantic_v1.parse_obj_as(GenericErrorResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(FailedReponseModelV2, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def async_compare_llm(
        self,
        *,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        input_prompt: typing.Optional[str] = OMIT,
        selected_models: typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[CompareLlmPageRequestResponseFormatType] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        input_prompt : typing.Optional[str]

        selected_models : typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[CompareLlmPageRequestResponseFormatType]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncApiResponseModelV3
            Successful Response

        Examples
        --------
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
        )
        client.large_language_models_gpt3.async_compare_llm()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/CompareLLM/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_prompt": input_prompt,
                "selected_models": selected_models,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "response_format_type": response_format_type,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(AsyncApiResponseModelV3, _response.json())  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    pydantic_v1.parse_obj_as(GenericErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def status_compare_llm(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CompareLlmPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareLlmPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
        )
        client.large_language_models_gpt3.status_compare_llm(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/CompareLLM/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CompareLlmPageStatusResponse, _response.json())  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    pydantic_v1.parse_obj_as(GenericErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncLargeLanguageModelsGpt3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def compare_llm(
        self,
        *,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        input_prompt: typing.Optional[str] = OMIT,
        selected_models: typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[CompareLlmPageRequestResponseFormatType] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> CompareLlmPageResponse:
        """
        Parameters
        ----------
        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        input_prompt : typing.Optional[str]

        selected_models : typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[CompareLlmPageRequestResponseFormatType]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareLlmPageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
        )


        async def main() -> None:
            await client.large_language_models_gpt3.compare_llm()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/CompareLLM/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_prompt": input_prompt,
                "selected_models": selected_models,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "response_format_type": response_format_type,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CompareLlmPageResponse, _response.json())  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    pydantic_v1.parse_obj_as(GenericErrorResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(FailedReponseModelV2, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def async_compare_llm(
        self,
        *,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        input_prompt: typing.Optional[str] = OMIT,
        selected_models: typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[CompareLlmPageRequestResponseFormatType] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        input_prompt : typing.Optional[str]

        selected_models : typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[CompareLlmPageRequestResponseFormatType]

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

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
        )


        async def main() -> None:
            await client.large_language_models_gpt3.async_compare_llm()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/CompareLLM/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_prompt": input_prompt,
                "selected_models": selected_models,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "response_format_type": response_format_type,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(AsyncApiResponseModelV3, _response.json())  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    pydantic_v1.parse_obj_as(GenericErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def status_compare_llm(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CompareLlmPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompareLlmPageStatusResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
        )


        async def main() -> None:
            await client.large_language_models_gpt3.status_compare_llm(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/CompareLLM/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CompareLlmPageStatusResponse, _response.json())  # type: ignore
            if _response.status_code == 402:
                raise PaymentRequiredError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(HttpValidationError, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    pydantic_v1.parse_obj_as(GenericErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
