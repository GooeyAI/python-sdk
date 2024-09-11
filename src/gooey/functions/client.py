# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.run_settings import RunSettings
from ..core.request_options import RequestOptions
from ..types.functions_page_output import FunctionsPageOutput
from ..core.pydantic_utilities import parse_obj_as
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.generic_error_response import GenericErrorResponse
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FunctionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def async_functions(
        self,
        *,
        example_id: typing.Optional[str] = None,
        code: typing.Optional[str] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FunctionsPageOutput:
        """
        Parameters
        ----------
        example_id : typing.Optional[str]

        code : typing.Optional[str]
            The JS code to be executed.

        variables : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Variables to be used in the code

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionsPageOutput
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            api_key="YOUR_API_KEY",
        )
        client.functions.async_functions()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/functions/async",
            method="POST",
            params={
                "example_id": example_id,
            },
            json={
                "code": code,
                "variables": variables,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    FunctionsPageOutput,
                    parse_obj_as(
                        type_=FunctionsPageOutput,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        GenericErrorResponse,
                        parse_obj_as(
                            type_=GenericErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncFunctionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def async_functions(
        self,
        *,
        example_id: typing.Optional[str] = None,
        code: typing.Optional[str] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FunctionsPageOutput:
        """
        Parameters
        ----------
        example_id : typing.Optional[str]

        code : typing.Optional[str]
            The JS code to be executed.

        variables : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Variables to be used in the code

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionsPageOutput
            Successful Response

        Examples
        --------
        import asyncio

        from gooey import AsyncGooey

        client = AsyncGooey(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.functions.async_functions()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/functions/async",
            method="POST",
            params={
                "example_id": example_id,
            },
            json={
                "code": code,
                "variables": variables,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    FunctionsPageOutput,
                    parse_obj_as(
                        type_=FunctionsPageOutput,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        GenericErrorResponse,
                        parse_obj_as(
                            type_=GenericErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
