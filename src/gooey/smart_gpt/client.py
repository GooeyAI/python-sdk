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
from ..types.generic_error_response import GenericErrorResponse
from ..types.http_validation_error import HttpValidationError
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings
from ..types.smart_gpt_page_response import SmartGptPageResponse
from .types.smart_gpt_page_request_response_format_type import SmartGptPageRequestResponseFormatType
from .types.smart_gpt_page_request_selected_model import SmartGptPageRequestSelectedModel

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SmartGptClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def async_smart_gpt(
        self,
        *,
        input_prompt: str,
        example_id: typing.Optional[str] = None,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        cot_prompt: typing.Optional[str] = OMIT,
        reflexion_prompt: typing.Optional[str] = OMIT,
        dera_prompt: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[SmartGptPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[SmartGptPageRequestResponseFormatType] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> SmartGptPageResponse:
        """
        Parameters
        ----------
        input_prompt : str

        example_id : typing.Optional[str]

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        cot_prompt : typing.Optional[str]

        reflexion_prompt : typing.Optional[str]

        dera_prompt : typing.Optional[str]

        selected_model : typing.Optional[SmartGptPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[SmartGptPageRequestResponseFormatType]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmartGptPageResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            api_key="YOUR_API_KEY",
        )
        client.smart_gpt.async_smart_gpt(
            input_prompt="input_prompt",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/SmartGPT/async",
            method="POST",
            params={"example_id": example_id},
            json={
                "functions": functions,
                "variables": variables,
                "input_prompt": input_prompt,
                "cot_prompt": cot_prompt,
                "reflexion_prompt": reflexion_prompt,
                "dera_prompt": dera_prompt,
                "selected_model": selected_model,
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
                return typing.cast(SmartGptPageResponse, parse_obj_as(type_=SmartGptPageResponse, object_=_response.json()))  # type: ignore
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

    def post(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            api_key="YOUR_API_KEY",
        )
        client.smart_gpt.post()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/SmartGPT/", method="POST", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSmartGptClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def async_smart_gpt(
        self,
        *,
        input_prompt: str,
        example_id: typing.Optional[str] = None,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        cot_prompt: typing.Optional[str] = OMIT,
        reflexion_prompt: typing.Optional[str] = OMIT,
        dera_prompt: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[SmartGptPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[SmartGptPageRequestResponseFormatType] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> SmartGptPageResponse:
        """
        Parameters
        ----------
        input_prompt : str

        example_id : typing.Optional[str]

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        cot_prompt : typing.Optional[str]

        reflexion_prompt : typing.Optional[str]

        dera_prompt : typing.Optional[str]

        selected_model : typing.Optional[SmartGptPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[SmartGptPageRequestResponseFormatType]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmartGptPageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey import AsyncGooey

        client = AsyncGooey(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.smart_gpt.async_smart_gpt(
                input_prompt="input_prompt",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/SmartGPT/async",
            method="POST",
            params={"example_id": example_id},
            json={
                "functions": functions,
                "variables": variables,
                "input_prompt": input_prompt,
                "cot_prompt": cot_prompt,
                "reflexion_prompt": reflexion_prompt,
                "dera_prompt": dera_prompt,
                "selected_model": selected_model,
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
                return typing.cast(SmartGptPageResponse, parse_obj_as(type_=SmartGptPageResponse, object_=_response.json()))  # type: ignore
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

    async def post(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from gooey import AsyncGooey

        client = AsyncGooey(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.smart_gpt.post()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/SmartGPT/", method="POST", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
