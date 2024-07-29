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
from ..types.asr_page_request_output_format import AsrPageRequestOutputFormat
from ..types.asr_page_request_selected_model import AsrPageRequestSelectedModel
from ..types.asr_page_request_translation_model import AsrPageRequestTranslationModel
from ..types.asr_page_response import AsrPageResponse
from ..types.asr_page_status_response import AsrPageStatusResponse
from ..types.async_api_response_model_v3 import AsyncApiResponseModelV3
from ..types.failed_reponse_model_v2 import FailedReponseModelV2
from ..types.generic_error_response import GenericErrorResponse
from ..types.http_validation_error import HttpValidationError
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SpeechRecognitionTranslationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def asr(
        self,
        *,
        documents: typing.Sequence[str],
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        selected_model: typing.Optional[AsrPageRequestSelectedModel] = OMIT,
        language: typing.Optional[str] = OMIT,
        translation_model: typing.Optional[AsrPageRequestTranslationModel] = OMIT,
        output_format: typing.Optional[AsrPageRequestOutputFormat] = OMIT,
        google_translate_target: typing.Optional[str] = OMIT,
        translation_source: typing.Optional[str] = OMIT,
        translation_target: typing.Optional[str] = OMIT,
        glossary_document: typing.Optional[str] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsrPageResponse:
        """
        Parameters
        ----------
        documents : typing.Sequence[str]

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        selected_model : typing.Optional[AsrPageRequestSelectedModel]

        language : typing.Optional[str]

        translation_model : typing.Optional[AsrPageRequestTranslationModel]

        output_format : typing.Optional[AsrPageRequestOutputFormat]

        google_translate_target : typing.Optional[str]
            use `translation_model` & `translation_target` instead.

        translation_source : typing.Optional[str]

        translation_target : typing.Optional[str]

        glossary_document : typing.Optional[str]
            Provide a glossary to customize translation and improve accuracy of domain-specific terms.
            If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsrPageResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.speech_recognition_translation.asr(
            documents=["documents"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/asr/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "documents": documents,
                "selected_model": selected_model,
                "language": language,
                "translation_model": translation_model,
                "output_format": output_format,
                "google_translate_target": google_translate_target,
                "translation_source": translation_source,
                "translation_target": translation_target,
                "glossary_document": glossary_document,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AsrPageResponse, parse_obj_as(type_=AsrPageResponse, object_=_response.json()))  # type: ignore
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

    def async_asr(
        self,
        *,
        documents: typing.Sequence[str],
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        selected_model: typing.Optional[AsrPageRequestSelectedModel] = OMIT,
        language: typing.Optional[str] = OMIT,
        translation_model: typing.Optional[AsrPageRequestTranslationModel] = OMIT,
        output_format: typing.Optional[AsrPageRequestOutputFormat] = OMIT,
        google_translate_target: typing.Optional[str] = OMIT,
        translation_source: typing.Optional[str] = OMIT,
        translation_target: typing.Optional[str] = OMIT,
        glossary_document: typing.Optional[str] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        documents : typing.Sequence[str]

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        selected_model : typing.Optional[AsrPageRequestSelectedModel]

        language : typing.Optional[str]

        translation_model : typing.Optional[AsrPageRequestTranslationModel]

        output_format : typing.Optional[AsrPageRequestOutputFormat]

        google_translate_target : typing.Optional[str]
            use `translation_model` & `translation_target` instead.

        translation_source : typing.Optional[str]

        translation_target : typing.Optional[str]

        glossary_document : typing.Optional[str]
            Provide a glossary to customize translation and improve accuracy of domain-specific terms.
            If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).

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
        client.speech_recognition_translation.async_asr(
            documents=["documents"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/asr/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "documents": documents,
                "selected_model": selected_model,
                "language": language,
                "translation_model": translation_model,
                "output_format": output_format,
                "google_translate_target": google_translate_target,
                "translation_source": translation_source,
                "translation_target": translation_target,
                "glossary_document": glossary_document,
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

    def status_asr(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsrPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsrPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.speech_recognition_translation.status_asr(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/asr/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AsrPageStatusResponse, parse_obj_as(type_=AsrPageStatusResponse, object_=_response.json()))  # type: ignore
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


class AsyncSpeechRecognitionTranslationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def asr(
        self,
        *,
        documents: typing.Sequence[str],
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        selected_model: typing.Optional[AsrPageRequestSelectedModel] = OMIT,
        language: typing.Optional[str] = OMIT,
        translation_model: typing.Optional[AsrPageRequestTranslationModel] = OMIT,
        output_format: typing.Optional[AsrPageRequestOutputFormat] = OMIT,
        google_translate_target: typing.Optional[str] = OMIT,
        translation_source: typing.Optional[str] = OMIT,
        translation_target: typing.Optional[str] = OMIT,
        glossary_document: typing.Optional[str] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsrPageResponse:
        """
        Parameters
        ----------
        documents : typing.Sequence[str]

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        selected_model : typing.Optional[AsrPageRequestSelectedModel]

        language : typing.Optional[str]

        translation_model : typing.Optional[AsrPageRequestTranslationModel]

        output_format : typing.Optional[AsrPageRequestOutputFormat]

        google_translate_target : typing.Optional[str]
            use `translation_model` & `translation_target` instead.

        translation_source : typing.Optional[str]

        translation_target : typing.Optional[str]

        glossary_document : typing.Optional[str]
            Provide a glossary to customize translation and improve accuracy of domain-specific terms.
            If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsrPageResponse
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
            await client.speech_recognition_translation.asr(
                documents=["documents"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/asr/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "documents": documents,
                "selected_model": selected_model,
                "language": language,
                "translation_model": translation_model,
                "output_format": output_format,
                "google_translate_target": google_translate_target,
                "translation_source": translation_source,
                "translation_target": translation_target,
                "glossary_document": glossary_document,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AsrPageResponse, parse_obj_as(type_=AsrPageResponse, object_=_response.json()))  # type: ignore
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

    async def async_asr(
        self,
        *,
        documents: typing.Sequence[str],
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        selected_model: typing.Optional[AsrPageRequestSelectedModel] = OMIT,
        language: typing.Optional[str] = OMIT,
        translation_model: typing.Optional[AsrPageRequestTranslationModel] = OMIT,
        output_format: typing.Optional[AsrPageRequestOutputFormat] = OMIT,
        google_translate_target: typing.Optional[str] = OMIT,
        translation_source: typing.Optional[str] = OMIT,
        translation_target: typing.Optional[str] = OMIT,
        glossary_document: typing.Optional[str] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        documents : typing.Sequence[str]

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        selected_model : typing.Optional[AsrPageRequestSelectedModel]

        language : typing.Optional[str]

        translation_model : typing.Optional[AsrPageRequestTranslationModel]

        output_format : typing.Optional[AsrPageRequestOutputFormat]

        google_translate_target : typing.Optional[str]
            use `translation_model` & `translation_target` instead.

        translation_source : typing.Optional[str]

        translation_target : typing.Optional[str]

        glossary_document : typing.Optional[str]
            Provide a glossary to customize translation and improve accuracy of domain-specific terms.
            If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).

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
            await client.speech_recognition_translation.async_asr(
                documents=["documents"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/asr/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "documents": documents,
                "selected_model": selected_model,
                "language": language,
                "translation_model": translation_model,
                "output_format": output_format,
                "google_translate_target": google_translate_target,
                "translation_source": translation_source,
                "translation_target": translation_target,
                "glossary_document": glossary_document,
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

    async def status_asr(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsrPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsrPageStatusResponse
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
            await client.speech_recognition_translation.status_asr(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/asr/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AsrPageStatusResponse, parse_obj_as(type_=AsrPageStatusResponse, object_=_response.json()))  # type: ignore
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
