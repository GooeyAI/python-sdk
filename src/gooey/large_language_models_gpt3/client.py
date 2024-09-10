# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.compare_llm_page_status_response import CompareLlmPageStatusResponse
from ..types.generic_error_response import GenericErrorResponse
from ..types.http_validation_error import HttpValidationError


class LargeLanguageModelsGpt3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
        from gooey import Gooey

        client = Gooey(
            api_key="YOUR_API_KEY",
        )
        client.large_language_models_gpt3.status_compare_llm(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/CompareLLM/status", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(CompareLlmPageStatusResponse, parse_obj_as(type_=CompareLlmPageStatusResponse, object_=_response.json()))  # type: ignore
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


class AsyncLargeLanguageModelsGpt3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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

        from gooey import AsyncGooey

        client = AsyncGooey(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.large_language_models_gpt3.status_compare_llm(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/CompareLLM/status", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(CompareLlmPageStatusResponse, parse_obj_as(type_=CompareLlmPageStatusResponse, object_=_response.json()))  # type: ignore
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
