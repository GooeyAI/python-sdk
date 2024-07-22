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
from ..types.failed_reponse_model_v2 import FailedReponseModelV2
from ..types.generic_error_response import GenericErrorResponse
from ..types.http_validation_error import HttpValidationError
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings
from ..types.text_to_speech_page_request_openai_tts_model import TextToSpeechPageRequestOpenaiTtsModel
from ..types.text_to_speech_page_request_openai_voice_name import TextToSpeechPageRequestOpenaiVoiceName
from ..types.text_to_speech_page_request_tts_provider import TextToSpeechPageRequestTtsProvider
from ..types.text_to_speech_page_response import TextToSpeechPageResponse
from ..types.text_to_speech_page_status_response import TextToSpeechPageStatusResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CompareAiVoiceGeneratorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def text_to_speech(
        self,
        *,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tts_provider: typing.Optional[TextToSpeechPageRequestTtsProvider] = OMIT,
        uberduck_voice_name: typing.Optional[str] = OMIT,
        uberduck_speaking_rate: typing.Optional[float] = OMIT,
        google_voice_name: typing.Optional[str] = OMIT,
        google_speaking_rate: typing.Optional[float] = OMIT,
        google_pitch: typing.Optional[float] = OMIT,
        bark_history_prompt: typing.Optional[str] = OMIT,
        elevenlabs_voice_name: typing.Optional[str] = OMIT,
        elevenlabs_api_key: typing.Optional[str] = OMIT,
        elevenlabs_voice_id: typing.Optional[str] = OMIT,
        elevenlabs_model: typing.Optional[str] = OMIT,
        elevenlabs_stability: typing.Optional[float] = OMIT,
        elevenlabs_similarity_boost: typing.Optional[float] = OMIT,
        elevenlabs_style: typing.Optional[float] = OMIT,
        elevenlabs_speaker_boost: typing.Optional[bool] = OMIT,
        azure_voice_name: typing.Optional[str] = OMIT,
        openai_voice_name: typing.Optional[TextToSpeechPageRequestOpenaiVoiceName] = OMIT,
        openai_tts_model: typing.Optional[TextToSpeechPageRequestOpenaiTtsModel] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> TextToSpeechPageResponse:
        """
        Parameters
        ----------
        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        tts_provider : typing.Optional[TextToSpeechPageRequestTtsProvider]

        uberduck_voice_name : typing.Optional[str]

        uberduck_speaking_rate : typing.Optional[float]

        google_voice_name : typing.Optional[str]

        google_speaking_rate : typing.Optional[float]

        google_pitch : typing.Optional[float]

        bark_history_prompt : typing.Optional[str]

        elevenlabs_voice_name : typing.Optional[str]
            Use `elevenlabs_voice_id` instead

        elevenlabs_api_key : typing.Optional[str]

        elevenlabs_voice_id : typing.Optional[str]

        elevenlabs_model : typing.Optional[str]

        elevenlabs_stability : typing.Optional[float]

        elevenlabs_similarity_boost : typing.Optional[float]

        elevenlabs_style : typing.Optional[float]

        elevenlabs_speaker_boost : typing.Optional[bool]

        azure_voice_name : typing.Optional[str]

        openai_voice_name : typing.Optional[TextToSpeechPageRequestOpenaiVoiceName]

        openai_tts_model : typing.Optional[TextToSpeechPageRequestOpenaiTtsModel]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TextToSpeechPageResponse
            Successful Response

        Examples
        --------
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.compare_ai_voice_generators.text_to_speech(
            text_prompt="text_prompt",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/TextToSpeech/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "text_prompt": text_prompt,
                "tts_provider": tts_provider,
                "uberduck_voice_name": uberduck_voice_name,
                "uberduck_speaking_rate": uberduck_speaking_rate,
                "google_voice_name": google_voice_name,
                "google_speaking_rate": google_speaking_rate,
                "google_pitch": google_pitch,
                "bark_history_prompt": bark_history_prompt,
                "elevenlabs_voice_name": elevenlabs_voice_name,
                "elevenlabs_api_key": elevenlabs_api_key,
                "elevenlabs_voice_id": elevenlabs_voice_id,
                "elevenlabs_model": elevenlabs_model,
                "elevenlabs_stability": elevenlabs_stability,
                "elevenlabs_similarity_boost": elevenlabs_similarity_boost,
                "elevenlabs_style": elevenlabs_style,
                "elevenlabs_speaker_boost": elevenlabs_speaker_boost,
                "azure_voice_name": azure_voice_name,
                "openai_voice_name": openai_voice_name,
                "openai_tts_model": openai_tts_model,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TextToSpeechPageResponse, _response.json())  # type: ignore
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

    def async_text_to_speech(
        self,
        *,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tts_provider: typing.Optional[TextToSpeechPageRequestTtsProvider] = OMIT,
        uberduck_voice_name: typing.Optional[str] = OMIT,
        uberduck_speaking_rate: typing.Optional[float] = OMIT,
        google_voice_name: typing.Optional[str] = OMIT,
        google_speaking_rate: typing.Optional[float] = OMIT,
        google_pitch: typing.Optional[float] = OMIT,
        bark_history_prompt: typing.Optional[str] = OMIT,
        elevenlabs_voice_name: typing.Optional[str] = OMIT,
        elevenlabs_api_key: typing.Optional[str] = OMIT,
        elevenlabs_voice_id: typing.Optional[str] = OMIT,
        elevenlabs_model: typing.Optional[str] = OMIT,
        elevenlabs_stability: typing.Optional[float] = OMIT,
        elevenlabs_similarity_boost: typing.Optional[float] = OMIT,
        elevenlabs_style: typing.Optional[float] = OMIT,
        elevenlabs_speaker_boost: typing.Optional[bool] = OMIT,
        azure_voice_name: typing.Optional[str] = OMIT,
        openai_voice_name: typing.Optional[TextToSpeechPageRequestOpenaiVoiceName] = OMIT,
        openai_tts_model: typing.Optional[TextToSpeechPageRequestOpenaiTtsModel] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        tts_provider : typing.Optional[TextToSpeechPageRequestTtsProvider]

        uberduck_voice_name : typing.Optional[str]

        uberduck_speaking_rate : typing.Optional[float]

        google_voice_name : typing.Optional[str]

        google_speaking_rate : typing.Optional[float]

        google_pitch : typing.Optional[float]

        bark_history_prompt : typing.Optional[str]

        elevenlabs_voice_name : typing.Optional[str]
            Use `elevenlabs_voice_id` instead

        elevenlabs_api_key : typing.Optional[str]

        elevenlabs_voice_id : typing.Optional[str]

        elevenlabs_model : typing.Optional[str]

        elevenlabs_stability : typing.Optional[float]

        elevenlabs_similarity_boost : typing.Optional[float]

        elevenlabs_style : typing.Optional[float]

        elevenlabs_speaker_boost : typing.Optional[bool]

        azure_voice_name : typing.Optional[str]

        openai_voice_name : typing.Optional[TextToSpeechPageRequestOpenaiVoiceName]

        openai_tts_model : typing.Optional[TextToSpeechPageRequestOpenaiTtsModel]

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.compare_ai_voice_generators.async_text_to_speech(
            text_prompt="text_prompt",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/TextToSpeech/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "text_prompt": text_prompt,
                "tts_provider": tts_provider,
                "uberduck_voice_name": uberduck_voice_name,
                "uberduck_speaking_rate": uberduck_speaking_rate,
                "google_voice_name": google_voice_name,
                "google_speaking_rate": google_speaking_rate,
                "google_pitch": google_pitch,
                "bark_history_prompt": bark_history_prompt,
                "elevenlabs_voice_name": elevenlabs_voice_name,
                "elevenlabs_api_key": elevenlabs_api_key,
                "elevenlabs_voice_id": elevenlabs_voice_id,
                "elevenlabs_model": elevenlabs_model,
                "elevenlabs_stability": elevenlabs_stability,
                "elevenlabs_similarity_boost": elevenlabs_similarity_boost,
                "elevenlabs_style": elevenlabs_style,
                "elevenlabs_speaker_boost": elevenlabs_speaker_boost,
                "azure_voice_name": azure_voice_name,
                "openai_voice_name": openai_voice_name,
                "openai_tts_model": openai_tts_model,
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

    def status_text_to_speech(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TextToSpeechPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TextToSpeechPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.compare_ai_voice_generators.status_text_to_speech(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/TextToSpeech/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TextToSpeechPageStatusResponse, _response.json())  # type: ignore
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


class AsyncCompareAiVoiceGeneratorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def text_to_speech(
        self,
        *,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tts_provider: typing.Optional[TextToSpeechPageRequestTtsProvider] = OMIT,
        uberduck_voice_name: typing.Optional[str] = OMIT,
        uberduck_speaking_rate: typing.Optional[float] = OMIT,
        google_voice_name: typing.Optional[str] = OMIT,
        google_speaking_rate: typing.Optional[float] = OMIT,
        google_pitch: typing.Optional[float] = OMIT,
        bark_history_prompt: typing.Optional[str] = OMIT,
        elevenlabs_voice_name: typing.Optional[str] = OMIT,
        elevenlabs_api_key: typing.Optional[str] = OMIT,
        elevenlabs_voice_id: typing.Optional[str] = OMIT,
        elevenlabs_model: typing.Optional[str] = OMIT,
        elevenlabs_stability: typing.Optional[float] = OMIT,
        elevenlabs_similarity_boost: typing.Optional[float] = OMIT,
        elevenlabs_style: typing.Optional[float] = OMIT,
        elevenlabs_speaker_boost: typing.Optional[bool] = OMIT,
        azure_voice_name: typing.Optional[str] = OMIT,
        openai_voice_name: typing.Optional[TextToSpeechPageRequestOpenaiVoiceName] = OMIT,
        openai_tts_model: typing.Optional[TextToSpeechPageRequestOpenaiTtsModel] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> TextToSpeechPageResponse:
        """
        Parameters
        ----------
        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        tts_provider : typing.Optional[TextToSpeechPageRequestTtsProvider]

        uberduck_voice_name : typing.Optional[str]

        uberduck_speaking_rate : typing.Optional[float]

        google_voice_name : typing.Optional[str]

        google_speaking_rate : typing.Optional[float]

        google_pitch : typing.Optional[float]

        bark_history_prompt : typing.Optional[str]

        elevenlabs_voice_name : typing.Optional[str]
            Use `elevenlabs_voice_id` instead

        elevenlabs_api_key : typing.Optional[str]

        elevenlabs_voice_id : typing.Optional[str]

        elevenlabs_model : typing.Optional[str]

        elevenlabs_stability : typing.Optional[float]

        elevenlabs_similarity_boost : typing.Optional[float]

        elevenlabs_style : typing.Optional[float]

        elevenlabs_speaker_boost : typing.Optional[bool]

        azure_voice_name : typing.Optional[str]

        openai_voice_name : typing.Optional[TextToSpeechPageRequestOpenaiVoiceName]

        openai_tts_model : typing.Optional[TextToSpeechPageRequestOpenaiTtsModel]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TextToSpeechPageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.compare_ai_voice_generators.text_to_speech(
                text_prompt="text_prompt",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/TextToSpeech/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "text_prompt": text_prompt,
                "tts_provider": tts_provider,
                "uberduck_voice_name": uberduck_voice_name,
                "uberduck_speaking_rate": uberduck_speaking_rate,
                "google_voice_name": google_voice_name,
                "google_speaking_rate": google_speaking_rate,
                "google_pitch": google_pitch,
                "bark_history_prompt": bark_history_prompt,
                "elevenlabs_voice_name": elevenlabs_voice_name,
                "elevenlabs_api_key": elevenlabs_api_key,
                "elevenlabs_voice_id": elevenlabs_voice_id,
                "elevenlabs_model": elevenlabs_model,
                "elevenlabs_stability": elevenlabs_stability,
                "elevenlabs_similarity_boost": elevenlabs_similarity_boost,
                "elevenlabs_style": elevenlabs_style,
                "elevenlabs_speaker_boost": elevenlabs_speaker_boost,
                "azure_voice_name": azure_voice_name,
                "openai_voice_name": openai_voice_name,
                "openai_tts_model": openai_tts_model,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TextToSpeechPageResponse, _response.json())  # type: ignore
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

    async def async_text_to_speech(
        self,
        *,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tts_provider: typing.Optional[TextToSpeechPageRequestTtsProvider] = OMIT,
        uberduck_voice_name: typing.Optional[str] = OMIT,
        uberduck_speaking_rate: typing.Optional[float] = OMIT,
        google_voice_name: typing.Optional[str] = OMIT,
        google_speaking_rate: typing.Optional[float] = OMIT,
        google_pitch: typing.Optional[float] = OMIT,
        bark_history_prompt: typing.Optional[str] = OMIT,
        elevenlabs_voice_name: typing.Optional[str] = OMIT,
        elevenlabs_api_key: typing.Optional[str] = OMIT,
        elevenlabs_voice_id: typing.Optional[str] = OMIT,
        elevenlabs_model: typing.Optional[str] = OMIT,
        elevenlabs_stability: typing.Optional[float] = OMIT,
        elevenlabs_similarity_boost: typing.Optional[float] = OMIT,
        elevenlabs_style: typing.Optional[float] = OMIT,
        elevenlabs_speaker_boost: typing.Optional[bool] = OMIT,
        azure_voice_name: typing.Optional[str] = OMIT,
        openai_voice_name: typing.Optional[TextToSpeechPageRequestOpenaiVoiceName] = OMIT,
        openai_tts_model: typing.Optional[TextToSpeechPageRequestOpenaiTtsModel] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        tts_provider : typing.Optional[TextToSpeechPageRequestTtsProvider]

        uberduck_voice_name : typing.Optional[str]

        uberduck_speaking_rate : typing.Optional[float]

        google_voice_name : typing.Optional[str]

        google_speaking_rate : typing.Optional[float]

        google_pitch : typing.Optional[float]

        bark_history_prompt : typing.Optional[str]

        elevenlabs_voice_name : typing.Optional[str]
            Use `elevenlabs_voice_id` instead

        elevenlabs_api_key : typing.Optional[str]

        elevenlabs_voice_id : typing.Optional[str]

        elevenlabs_model : typing.Optional[str]

        elevenlabs_stability : typing.Optional[float]

        elevenlabs_similarity_boost : typing.Optional[float]

        elevenlabs_style : typing.Optional[float]

        elevenlabs_speaker_boost : typing.Optional[bool]

        azure_voice_name : typing.Optional[str]

        openai_voice_name : typing.Optional[TextToSpeechPageRequestOpenaiVoiceName]

        openai_tts_model : typing.Optional[TextToSpeechPageRequestOpenaiTtsModel]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.compare_ai_voice_generators.async_text_to_speech(
                text_prompt="text_prompt",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/TextToSpeech/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "text_prompt": text_prompt,
                "tts_provider": tts_provider,
                "uberduck_voice_name": uberduck_voice_name,
                "uberduck_speaking_rate": uberduck_speaking_rate,
                "google_voice_name": google_voice_name,
                "google_speaking_rate": google_speaking_rate,
                "google_pitch": google_pitch,
                "bark_history_prompt": bark_history_prompt,
                "elevenlabs_voice_name": elevenlabs_voice_name,
                "elevenlabs_api_key": elevenlabs_api_key,
                "elevenlabs_voice_id": elevenlabs_voice_id,
                "elevenlabs_model": elevenlabs_model,
                "elevenlabs_stability": elevenlabs_stability,
                "elevenlabs_similarity_boost": elevenlabs_similarity_boost,
                "elevenlabs_style": elevenlabs_style,
                "elevenlabs_speaker_boost": elevenlabs_speaker_boost,
                "azure_voice_name": azure_voice_name,
                "openai_voice_name": openai_voice_name,
                "openai_tts_model": openai_tts_model,
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

    async def status_text_to_speech(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TextToSpeechPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TextToSpeechPageStatusResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.compare_ai_voice_generators.status_text_to_speech(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/TextToSpeech/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TextToSpeechPageStatusResponse, _response.json())  # type: ignore
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
