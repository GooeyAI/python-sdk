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
from ..types.img2img_page_request_selected_controlnet_model import Img2ImgPageRequestSelectedControlnetModel
from ..types.img2img_page_request_selected_model import Img2ImgPageRequestSelectedModel
from ..types.img2img_page_response import Img2ImgPageResponse
from ..types.img2img_page_status_response import Img2ImgPageStatusResponse
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EditAnImageWithAiPromptClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def img2img(
        self,
        *,
        input_image: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        text_prompt: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[Img2ImgPageRequestSelectedModel] = OMIT,
        selected_controlnet_model: typing.Optional[Img2ImgPageRequestSelectedControlnetModel] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        prompt_strength: typing.Optional[float] = OMIT,
        controlnet_conditioning_scale: typing.Optional[typing.Sequence[float]] = OMIT,
        seed: typing.Optional[int] = OMIT,
        image_guidance_scale: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> Img2ImgPageResponse:
        """
        Parameters
        ----------
        input_image : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        text_prompt : typing.Optional[str]

        selected_model : typing.Optional[Img2ImgPageRequestSelectedModel]

        selected_controlnet_model : typing.Optional[Img2ImgPageRequestSelectedControlnetModel]

        negative_prompt : typing.Optional[str]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        prompt_strength : typing.Optional[float]

        controlnet_conditioning_scale : typing.Optional[typing.Sequence[float]]

        seed : typing.Optional[int]

        image_guidance_scale : typing.Optional[float]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Img2ImgPageResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.edit_an_image_with_ai_prompt.img2img(
            input_image="input_image",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/Img2Img/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "text_prompt": text_prompt,
                "selected_model": selected_model,
                "selected_controlnet_model": selected_controlnet_model,
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
                "quality": quality,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "prompt_strength": prompt_strength,
                "controlnet_conditioning_scale": controlnet_conditioning_scale,
                "seed": seed,
                "image_guidance_scale": image_guidance_scale,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Img2ImgPageResponse, parse_obj_as(type_=Img2ImgPageResponse, object_=_response.json()))  # type: ignore
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

    def async_img2img(
        self,
        *,
        input_image: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        text_prompt: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[Img2ImgPageRequestSelectedModel] = OMIT,
        selected_controlnet_model: typing.Optional[Img2ImgPageRequestSelectedControlnetModel] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        prompt_strength: typing.Optional[float] = OMIT,
        controlnet_conditioning_scale: typing.Optional[typing.Sequence[float]] = OMIT,
        seed: typing.Optional[int] = OMIT,
        image_guidance_scale: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        input_image : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        text_prompt : typing.Optional[str]

        selected_model : typing.Optional[Img2ImgPageRequestSelectedModel]

        selected_controlnet_model : typing.Optional[Img2ImgPageRequestSelectedControlnetModel]

        negative_prompt : typing.Optional[str]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        prompt_strength : typing.Optional[float]

        controlnet_conditioning_scale : typing.Optional[typing.Sequence[float]]

        seed : typing.Optional[int]

        image_guidance_scale : typing.Optional[float]

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
        client.edit_an_image_with_ai_prompt.async_img2img(
            input_image="input_image",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/Img2Img/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "text_prompt": text_prompt,
                "selected_model": selected_model,
                "selected_controlnet_model": selected_controlnet_model,
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
                "quality": quality,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "prompt_strength": prompt_strength,
                "controlnet_conditioning_scale": controlnet_conditioning_scale,
                "seed": seed,
                "image_guidance_scale": image_guidance_scale,
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

    def status_img2img(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Img2ImgPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Img2ImgPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.edit_an_image_with_ai_prompt.status_img2img(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/Img2Img/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Img2ImgPageStatusResponse, parse_obj_as(type_=Img2ImgPageStatusResponse, object_=_response.json()))  # type: ignore
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


class AsyncEditAnImageWithAiPromptClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def img2img(
        self,
        *,
        input_image: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        text_prompt: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[Img2ImgPageRequestSelectedModel] = OMIT,
        selected_controlnet_model: typing.Optional[Img2ImgPageRequestSelectedControlnetModel] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        prompt_strength: typing.Optional[float] = OMIT,
        controlnet_conditioning_scale: typing.Optional[typing.Sequence[float]] = OMIT,
        seed: typing.Optional[int] = OMIT,
        image_guidance_scale: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> Img2ImgPageResponse:
        """
        Parameters
        ----------
        input_image : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        text_prompt : typing.Optional[str]

        selected_model : typing.Optional[Img2ImgPageRequestSelectedModel]

        selected_controlnet_model : typing.Optional[Img2ImgPageRequestSelectedControlnetModel]

        negative_prompt : typing.Optional[str]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        prompt_strength : typing.Optional[float]

        controlnet_conditioning_scale : typing.Optional[typing.Sequence[float]]

        seed : typing.Optional[int]

        image_guidance_scale : typing.Optional[float]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Img2ImgPageResponse
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
            await client.edit_an_image_with_ai_prompt.img2img(
                input_image="input_image",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/Img2Img/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "text_prompt": text_prompt,
                "selected_model": selected_model,
                "selected_controlnet_model": selected_controlnet_model,
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
                "quality": quality,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "prompt_strength": prompt_strength,
                "controlnet_conditioning_scale": controlnet_conditioning_scale,
                "seed": seed,
                "image_guidance_scale": image_guidance_scale,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Img2ImgPageResponse, parse_obj_as(type_=Img2ImgPageResponse, object_=_response.json()))  # type: ignore
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

    async def async_img2img(
        self,
        *,
        input_image: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        text_prompt: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[Img2ImgPageRequestSelectedModel] = OMIT,
        selected_controlnet_model: typing.Optional[Img2ImgPageRequestSelectedControlnetModel] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        prompt_strength: typing.Optional[float] = OMIT,
        controlnet_conditioning_scale: typing.Optional[typing.Sequence[float]] = OMIT,
        seed: typing.Optional[int] = OMIT,
        image_guidance_scale: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        input_image : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        text_prompt : typing.Optional[str]

        selected_model : typing.Optional[Img2ImgPageRequestSelectedModel]

        selected_controlnet_model : typing.Optional[Img2ImgPageRequestSelectedControlnetModel]

        negative_prompt : typing.Optional[str]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        prompt_strength : typing.Optional[float]

        controlnet_conditioning_scale : typing.Optional[typing.Sequence[float]]

        seed : typing.Optional[int]

        image_guidance_scale : typing.Optional[float]

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
            await client.edit_an_image_with_ai_prompt.async_img2img(
                input_image="input_image",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/Img2Img/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "text_prompt": text_prompt,
                "selected_model": selected_model,
                "selected_controlnet_model": selected_controlnet_model,
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
                "quality": quality,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "prompt_strength": prompt_strength,
                "controlnet_conditioning_scale": controlnet_conditioning_scale,
                "seed": seed,
                "image_guidance_scale": image_guidance_scale,
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

    async def status_img2img(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Img2ImgPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Img2ImgPageStatusResponse
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
            await client.edit_an_image_with_ai_prompt.status_img2img(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/Img2Img/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Img2ImgPageStatusResponse, parse_obj_as(type_=Img2ImgPageStatusResponse, object_=_response.json()))  # type: ignore
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