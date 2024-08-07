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
from ..types.qr_code_generator_page_request_image_prompt_controlnet_models_item import (
    QrCodeGeneratorPageRequestImagePromptControlnetModelsItem,
)
from ..types.qr_code_generator_page_request_scheduler import QrCodeGeneratorPageRequestScheduler
from ..types.qr_code_generator_page_request_selected_controlnet_model_item import (
    QrCodeGeneratorPageRequestSelectedControlnetModelItem,
)
from ..types.qr_code_generator_page_request_selected_model import QrCodeGeneratorPageRequestSelectedModel
from ..types.qr_code_generator_page_response import QrCodeGeneratorPageResponse
from ..types.qr_code_generator_page_status_response import QrCodeGeneratorPageStatusResponse
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings
from ..types.vcard import Vcard

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AiArtQrCodeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def art_qr_code(
        self,
        *,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        qr_code_data: typing.Optional[str] = OMIT,
        qr_code_input_image: typing.Optional[str] = OMIT,
        qr_code_vcard: typing.Optional[Vcard] = OMIT,
        qr_code_file: typing.Optional[str] = OMIT,
        use_url_shortener: typing.Optional[bool] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        image_prompt: typing.Optional[str] = OMIT,
        image_prompt_controlnet_models: typing.Optional[
            typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]
        ] = OMIT,
        image_prompt_strength: typing.Optional[float] = OMIT,
        image_prompt_scale: typing.Optional[float] = OMIT,
        image_prompt_pos_x: typing.Optional[float] = OMIT,
        image_prompt_pos_y: typing.Optional[float] = OMIT,
        selected_model: typing.Optional[QrCodeGeneratorPageRequestSelectedModel] = OMIT,
        selected_controlnet_model: typing.Optional[
            typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]
        ] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        controlnet_conditioning_scale: typing.Optional[typing.Sequence[float]] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        scheduler: typing.Optional[QrCodeGeneratorPageRequestScheduler] = OMIT,
        seed: typing.Optional[int] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> QrCodeGeneratorPageResponse:
        """
        Parameters
        ----------
        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        qr_code_data : typing.Optional[str]

        qr_code_input_image : typing.Optional[str]

        qr_code_vcard : typing.Optional[Vcard]

        qr_code_file : typing.Optional[str]

        use_url_shortener : typing.Optional[bool]

        negative_prompt : typing.Optional[str]

        image_prompt : typing.Optional[str]

        image_prompt_controlnet_models : typing.Optional[typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]]

        image_prompt_strength : typing.Optional[float]

        image_prompt_scale : typing.Optional[float]

        image_prompt_pos_x : typing.Optional[float]

        image_prompt_pos_y : typing.Optional[float]

        selected_model : typing.Optional[QrCodeGeneratorPageRequestSelectedModel]

        selected_controlnet_model : typing.Optional[typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        controlnet_conditioning_scale : typing.Optional[typing.Sequence[float]]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        scheduler : typing.Optional[QrCodeGeneratorPageRequestScheduler]

        seed : typing.Optional[int]

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QrCodeGeneratorPageResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.ai_art_qr_code.art_qr_code(
            text_prompt="text_prompt",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/art-qr-code/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "qr_code_data": qr_code_data,
                "qr_code_input_image": qr_code_input_image,
                "qr_code_vcard": qr_code_vcard,
                "qr_code_file": qr_code_file,
                "use_url_shortener": use_url_shortener,
                "text_prompt": text_prompt,
                "negative_prompt": negative_prompt,
                "image_prompt": image_prompt,
                "image_prompt_controlnet_models": image_prompt_controlnet_models,
                "image_prompt_strength": image_prompt_strength,
                "image_prompt_scale": image_prompt_scale,
                "image_prompt_pos_x": image_prompt_pos_x,
                "image_prompt_pos_y": image_prompt_pos_y,
                "selected_model": selected_model,
                "selected_controlnet_model": selected_controlnet_model,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "controlnet_conditioning_scale": controlnet_conditioning_scale,
                "num_outputs": num_outputs,
                "quality": quality,
                "scheduler": scheduler,
                "seed": seed,
                "obj_scale": obj_scale,
                "obj_pos_x": obj_pos_x,
                "obj_pos_y": obj_pos_y,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(QrCodeGeneratorPageResponse, parse_obj_as(type_=QrCodeGeneratorPageResponse, object_=_response.json()))  # type: ignore
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

    def async_art_qr_code(
        self,
        *,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        qr_code_data: typing.Optional[str] = OMIT,
        qr_code_input_image: typing.Optional[str] = OMIT,
        qr_code_vcard: typing.Optional[Vcard] = OMIT,
        qr_code_file: typing.Optional[str] = OMIT,
        use_url_shortener: typing.Optional[bool] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        image_prompt: typing.Optional[str] = OMIT,
        image_prompt_controlnet_models: typing.Optional[
            typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]
        ] = OMIT,
        image_prompt_strength: typing.Optional[float] = OMIT,
        image_prompt_scale: typing.Optional[float] = OMIT,
        image_prompt_pos_x: typing.Optional[float] = OMIT,
        image_prompt_pos_y: typing.Optional[float] = OMIT,
        selected_model: typing.Optional[QrCodeGeneratorPageRequestSelectedModel] = OMIT,
        selected_controlnet_model: typing.Optional[
            typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]
        ] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        controlnet_conditioning_scale: typing.Optional[typing.Sequence[float]] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        scheduler: typing.Optional[QrCodeGeneratorPageRequestScheduler] = OMIT,
        seed: typing.Optional[int] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
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

        qr_code_data : typing.Optional[str]

        qr_code_input_image : typing.Optional[str]

        qr_code_vcard : typing.Optional[Vcard]

        qr_code_file : typing.Optional[str]

        use_url_shortener : typing.Optional[bool]

        negative_prompt : typing.Optional[str]

        image_prompt : typing.Optional[str]

        image_prompt_controlnet_models : typing.Optional[typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]]

        image_prompt_strength : typing.Optional[float]

        image_prompt_scale : typing.Optional[float]

        image_prompt_pos_x : typing.Optional[float]

        image_prompt_pos_y : typing.Optional[float]

        selected_model : typing.Optional[QrCodeGeneratorPageRequestSelectedModel]

        selected_controlnet_model : typing.Optional[typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        controlnet_conditioning_scale : typing.Optional[typing.Sequence[float]]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        scheduler : typing.Optional[QrCodeGeneratorPageRequestScheduler]

        seed : typing.Optional[int]

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

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
        client.ai_art_qr_code.async_art_qr_code(
            text_prompt="text_prompt",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/art-qr-code/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "qr_code_data": qr_code_data,
                "qr_code_input_image": qr_code_input_image,
                "qr_code_vcard": qr_code_vcard,
                "qr_code_file": qr_code_file,
                "use_url_shortener": use_url_shortener,
                "text_prompt": text_prompt,
                "negative_prompt": negative_prompt,
                "image_prompt": image_prompt,
                "image_prompt_controlnet_models": image_prompt_controlnet_models,
                "image_prompt_strength": image_prompt_strength,
                "image_prompt_scale": image_prompt_scale,
                "image_prompt_pos_x": image_prompt_pos_x,
                "image_prompt_pos_y": image_prompt_pos_y,
                "selected_model": selected_model,
                "selected_controlnet_model": selected_controlnet_model,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "controlnet_conditioning_scale": controlnet_conditioning_scale,
                "num_outputs": num_outputs,
                "quality": quality,
                "scheduler": scheduler,
                "seed": seed,
                "obj_scale": obj_scale,
                "obj_pos_x": obj_pos_x,
                "obj_pos_y": obj_pos_y,
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

    def status_art_qr_code(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> QrCodeGeneratorPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QrCodeGeneratorPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.ai_art_qr_code.status_art_qr_code(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/art-qr-code/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(QrCodeGeneratorPageStatusResponse, parse_obj_as(type_=QrCodeGeneratorPageStatusResponse, object_=_response.json()))  # type: ignore
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


class AsyncAiArtQrCodeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def art_qr_code(
        self,
        *,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        qr_code_data: typing.Optional[str] = OMIT,
        qr_code_input_image: typing.Optional[str] = OMIT,
        qr_code_vcard: typing.Optional[Vcard] = OMIT,
        qr_code_file: typing.Optional[str] = OMIT,
        use_url_shortener: typing.Optional[bool] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        image_prompt: typing.Optional[str] = OMIT,
        image_prompt_controlnet_models: typing.Optional[
            typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]
        ] = OMIT,
        image_prompt_strength: typing.Optional[float] = OMIT,
        image_prompt_scale: typing.Optional[float] = OMIT,
        image_prompt_pos_x: typing.Optional[float] = OMIT,
        image_prompt_pos_y: typing.Optional[float] = OMIT,
        selected_model: typing.Optional[QrCodeGeneratorPageRequestSelectedModel] = OMIT,
        selected_controlnet_model: typing.Optional[
            typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]
        ] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        controlnet_conditioning_scale: typing.Optional[typing.Sequence[float]] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        scheduler: typing.Optional[QrCodeGeneratorPageRequestScheduler] = OMIT,
        seed: typing.Optional[int] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> QrCodeGeneratorPageResponse:
        """
        Parameters
        ----------
        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        qr_code_data : typing.Optional[str]

        qr_code_input_image : typing.Optional[str]

        qr_code_vcard : typing.Optional[Vcard]

        qr_code_file : typing.Optional[str]

        use_url_shortener : typing.Optional[bool]

        negative_prompt : typing.Optional[str]

        image_prompt : typing.Optional[str]

        image_prompt_controlnet_models : typing.Optional[typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]]

        image_prompt_strength : typing.Optional[float]

        image_prompt_scale : typing.Optional[float]

        image_prompt_pos_x : typing.Optional[float]

        image_prompt_pos_y : typing.Optional[float]

        selected_model : typing.Optional[QrCodeGeneratorPageRequestSelectedModel]

        selected_controlnet_model : typing.Optional[typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        controlnet_conditioning_scale : typing.Optional[typing.Sequence[float]]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        scheduler : typing.Optional[QrCodeGeneratorPageRequestScheduler]

        seed : typing.Optional[int]

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QrCodeGeneratorPageResponse
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
            await client.ai_art_qr_code.art_qr_code(
                text_prompt="text_prompt",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/art-qr-code/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "qr_code_data": qr_code_data,
                "qr_code_input_image": qr_code_input_image,
                "qr_code_vcard": qr_code_vcard,
                "qr_code_file": qr_code_file,
                "use_url_shortener": use_url_shortener,
                "text_prompt": text_prompt,
                "negative_prompt": negative_prompt,
                "image_prompt": image_prompt,
                "image_prompt_controlnet_models": image_prompt_controlnet_models,
                "image_prompt_strength": image_prompt_strength,
                "image_prompt_scale": image_prompt_scale,
                "image_prompt_pos_x": image_prompt_pos_x,
                "image_prompt_pos_y": image_prompt_pos_y,
                "selected_model": selected_model,
                "selected_controlnet_model": selected_controlnet_model,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "controlnet_conditioning_scale": controlnet_conditioning_scale,
                "num_outputs": num_outputs,
                "quality": quality,
                "scheduler": scheduler,
                "seed": seed,
                "obj_scale": obj_scale,
                "obj_pos_x": obj_pos_x,
                "obj_pos_y": obj_pos_y,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(QrCodeGeneratorPageResponse, parse_obj_as(type_=QrCodeGeneratorPageResponse, object_=_response.json()))  # type: ignore
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

    async def async_art_qr_code(
        self,
        *,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        qr_code_data: typing.Optional[str] = OMIT,
        qr_code_input_image: typing.Optional[str] = OMIT,
        qr_code_vcard: typing.Optional[Vcard] = OMIT,
        qr_code_file: typing.Optional[str] = OMIT,
        use_url_shortener: typing.Optional[bool] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        image_prompt: typing.Optional[str] = OMIT,
        image_prompt_controlnet_models: typing.Optional[
            typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]
        ] = OMIT,
        image_prompt_strength: typing.Optional[float] = OMIT,
        image_prompt_scale: typing.Optional[float] = OMIT,
        image_prompt_pos_x: typing.Optional[float] = OMIT,
        image_prompt_pos_y: typing.Optional[float] = OMIT,
        selected_model: typing.Optional[QrCodeGeneratorPageRequestSelectedModel] = OMIT,
        selected_controlnet_model: typing.Optional[
            typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]
        ] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        controlnet_conditioning_scale: typing.Optional[typing.Sequence[float]] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        scheduler: typing.Optional[QrCodeGeneratorPageRequestScheduler] = OMIT,
        seed: typing.Optional[int] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
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

        qr_code_data : typing.Optional[str]

        qr_code_input_image : typing.Optional[str]

        qr_code_vcard : typing.Optional[Vcard]

        qr_code_file : typing.Optional[str]

        use_url_shortener : typing.Optional[bool]

        negative_prompt : typing.Optional[str]

        image_prompt : typing.Optional[str]

        image_prompt_controlnet_models : typing.Optional[typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]]

        image_prompt_strength : typing.Optional[float]

        image_prompt_scale : typing.Optional[float]

        image_prompt_pos_x : typing.Optional[float]

        image_prompt_pos_y : typing.Optional[float]

        selected_model : typing.Optional[QrCodeGeneratorPageRequestSelectedModel]

        selected_controlnet_model : typing.Optional[typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        controlnet_conditioning_scale : typing.Optional[typing.Sequence[float]]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        scheduler : typing.Optional[QrCodeGeneratorPageRequestScheduler]

        seed : typing.Optional[int]

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

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
            await client.ai_art_qr_code.async_art_qr_code(
                text_prompt="text_prompt",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/art-qr-code/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "qr_code_data": qr_code_data,
                "qr_code_input_image": qr_code_input_image,
                "qr_code_vcard": qr_code_vcard,
                "qr_code_file": qr_code_file,
                "use_url_shortener": use_url_shortener,
                "text_prompt": text_prompt,
                "negative_prompt": negative_prompt,
                "image_prompt": image_prompt,
                "image_prompt_controlnet_models": image_prompt_controlnet_models,
                "image_prompt_strength": image_prompt_strength,
                "image_prompt_scale": image_prompt_scale,
                "image_prompt_pos_x": image_prompt_pos_x,
                "image_prompt_pos_y": image_prompt_pos_y,
                "selected_model": selected_model,
                "selected_controlnet_model": selected_controlnet_model,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "controlnet_conditioning_scale": controlnet_conditioning_scale,
                "num_outputs": num_outputs,
                "quality": quality,
                "scheduler": scheduler,
                "seed": seed,
                "obj_scale": obj_scale,
                "obj_pos_x": obj_pos_x,
                "obj_pos_y": obj_pos_y,
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

    async def status_art_qr_code(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> QrCodeGeneratorPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QrCodeGeneratorPageStatusResponse
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
            await client.ai_art_qr_code.status_art_qr_code(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/art-qr-code/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(QrCodeGeneratorPageStatusResponse, parse_obj_as(type_=QrCodeGeneratorPageStatusResponse, object_=_response.json()))  # type: ignore
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
