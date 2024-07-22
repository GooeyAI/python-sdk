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
from ..types.chyron_plant_page_response import ChyronPlantPageResponse
from ..types.chyron_plant_page_status_response import ChyronPlantPageStatusResponse
from ..types.failed_reponse_model_v2 import FailedReponseModelV2
from ..types.generic_error_response import GenericErrorResponse
from ..types.http_validation_error import HttpValidationError
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ChyronPlantBotClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def chyron_plant(
        self,
        *,
        midi_notes: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        midi_notes_prompt: typing.Optional[str] = OMIT,
        chyron_prompt: typing.Optional[str] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> ChyronPlantPageResponse:
        """
        Parameters
        ----------
        midi_notes : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        midi_notes_prompt : typing.Optional[str]

        chyron_prompt : typing.Optional[str]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChyronPlantPageResponse
            Successful Response

        Examples
        --------
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
        )
        client.chyron_plant_bot.chyron_plant(
            midi_notes="C#1 B6 A2 A1 A3 A2",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/ChyronPlant/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "midi_notes": midi_notes,
                "midi_notes_prompt": midi_notes_prompt,
                "chyron_prompt": chyron_prompt,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ChyronPlantPageResponse, _response.json())  # type: ignore
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

    def async_chyron_plant(
        self,
        *,
        midi_notes: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        midi_notes_prompt: typing.Optional[str] = OMIT,
        chyron_prompt: typing.Optional[str] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        midi_notes : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        midi_notes_prompt : typing.Optional[str]

        chyron_prompt : typing.Optional[str]

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
        client.chyron_plant_bot.async_chyron_plant(
            midi_notes="C#1 B6 A2 A1 A3 A2",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/ChyronPlant/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "midi_notes": midi_notes,
                "midi_notes_prompt": midi_notes_prompt,
                "chyron_prompt": chyron_prompt,
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

    def status_chyron_plant(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ChyronPlantPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChyronPlantPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
        )
        client.chyron_plant_bot.status_chyron_plant(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/ChyronPlant/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ChyronPlantPageStatusResponse, _response.json())  # type: ignore
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


class AsyncChyronPlantBotClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def chyron_plant(
        self,
        *,
        midi_notes: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        midi_notes_prompt: typing.Optional[str] = OMIT,
        chyron_prompt: typing.Optional[str] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> ChyronPlantPageResponse:
        """
        Parameters
        ----------
        midi_notes : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        midi_notes_prompt : typing.Optional[str]

        chyron_prompt : typing.Optional[str]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChyronPlantPageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
        )


        async def main() -> None:
            await client.chyron_plant_bot.chyron_plant(
                midi_notes="C#1 B6 A2 A1 A3 A2",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/ChyronPlant/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "midi_notes": midi_notes,
                "midi_notes_prompt": midi_notes_prompt,
                "chyron_prompt": chyron_prompt,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ChyronPlantPageResponse, _response.json())  # type: ignore
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

    async def async_chyron_plant(
        self,
        *,
        midi_notes: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        midi_notes_prompt: typing.Optional[str] = OMIT,
        chyron_prompt: typing.Optional[str] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        midi_notes : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        midi_notes_prompt : typing.Optional[str]

        chyron_prompt : typing.Optional[str]

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
            await client.chyron_plant_bot.async_chyron_plant(
                midi_notes="C#1 B6 A2 A1 A3 A2",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/ChyronPlant/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "midi_notes": midi_notes,
                "midi_notes_prompt": midi_notes_prompt,
                "chyron_prompt": chyron_prompt,
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

    async def status_chyron_plant(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ChyronPlantPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChyronPlantPageStatusResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
        )


        async def main() -> None:
            await client.chyron_plant_bot.status_chyron_plant(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/ChyronPlant/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ChyronPlantPageStatusResponse, _response.json())  # type: ignore
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
