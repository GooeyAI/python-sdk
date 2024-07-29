# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.balance_response import BalanceResponse
from ..types.bot_broadcast_filters import BotBroadcastFilters
from ..types.http_validation_error import HttpValidationError
from ..types.reply_button import ReplyButton

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MiscClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> BalanceResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BalanceResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.misc.get_balance()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/balance/", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(BalanceResponse, parse_obj_as(type_=BalanceResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def video_bots_broadcast(
        self,
        *,
        text: str,
        example_id: typing.Optional[str] = None,
        run_id: typing.Optional[str] = None,
        audio: typing.Optional[str] = OMIT,
        video: typing.Optional[str] = OMIT,
        documents: typing.Optional[typing.Sequence[str]] = OMIT,
        buttons: typing.Optional[typing.Sequence[ReplyButton]] = OMIT,
        filters: typing.Optional[BotBroadcastFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        text : str
            Message to broadcast to all users

        example_id : typing.Optional[str]

        run_id : typing.Optional[str]

        audio : typing.Optional[str]
            Audio URL to send to all users

        video : typing.Optional[str]
            Video URL to send to all users

        documents : typing.Optional[typing.Sequence[str]]
            Video URL to send to all users

        buttons : typing.Optional[typing.Sequence[ReplyButton]]
            Buttons to send to all users

        filters : typing.Optional[BotBroadcastFilters]
            Filters to select users to broadcast to. If not provided, will broadcast to all users of this bot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.misc.video_bots_broadcast(
            text="text",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/video-bots/broadcast/send/",
            method="POST",
            params={"example_id": example_id, "run_id": run_id},
            json={
                "text": text,
                "audio": audio,
                "video": video,
                "documents": documents,
                "buttons": buttons,
                "filters": filters,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.misc.health()
        """
        _response = self._client_wrapper.httpx_client.request(method="GET", request_options=request_options)
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMiscClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> BalanceResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BalanceResponse
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
            await client.misc.get_balance()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/balance/", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(BalanceResponse, parse_obj_as(type_=BalanceResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def video_bots_broadcast(
        self,
        *,
        text: str,
        example_id: typing.Optional[str] = None,
        run_id: typing.Optional[str] = None,
        audio: typing.Optional[str] = OMIT,
        video: typing.Optional[str] = OMIT,
        documents: typing.Optional[typing.Sequence[str]] = OMIT,
        buttons: typing.Optional[typing.Sequence[ReplyButton]] = OMIT,
        filters: typing.Optional[BotBroadcastFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        text : str
            Message to broadcast to all users

        example_id : typing.Optional[str]

        run_id : typing.Optional[str]

        audio : typing.Optional[str]
            Audio URL to send to all users

        video : typing.Optional[str]
            Video URL to send to all users

        documents : typing.Optional[typing.Sequence[str]]
            Video URL to send to all users

        buttons : typing.Optional[typing.Sequence[ReplyButton]]
            Buttons to send to all users

        filters : typing.Optional[BotBroadcastFilters]
            Filters to select users to broadcast to. If not provided, will broadcast to all users of this bot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
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
            await client.misc.video_bots_broadcast(
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/video-bots/broadcast/send/",
            method="POST",
            params={"example_id": example_id, "run_id": run_id},
            json={
                "text": text,
                "audio": audio,
                "video": video,
                "documents": documents,
                "buttons": buttons,
                "filters": filters,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, parse_obj_as(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
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
            await client.misc.health()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(method="GET", request_options=request_options)
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Any, parse_obj_as(type_=typing.Any, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)