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
from ..types.object_inpainting_page_request_selected_model import ObjectInpaintingPageRequestSelectedModel
from ..types.object_inpainting_page_response import ObjectInpaintingPageResponse
from ..types.object_inpainting_page_status_response import ObjectInpaintingPageStatusResponse
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GenerateProductPhotoBackgroundsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def object_inpainting(
        self,
        *,
        input_image: str,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
        mask_threshold: typing.Optional[float] = OMIT,
        selected_model: typing.Optional[ObjectInpaintingPageRequestSelectedModel] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        sd2upscaling: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> ObjectInpaintingPageResponse:
        """
        Parameters
        ----------
        input_image : str

        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

        mask_threshold : typing.Optional[float]

        selected_model : typing.Optional[ObjectInpaintingPageRequestSelectedModel]

        negative_prompt : typing.Optional[str]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        sd2upscaling : typing.Optional[bool]

        seed : typing.Optional[int]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectInpaintingPageResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.generate_product_photo_backgrounds.object_inpainting(
            input_image="input_image",
            text_prompt="text_prompt",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/ObjectInpainting/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "text_prompt": text_prompt,
                "obj_scale": obj_scale,
                "obj_pos_x": obj_pos_x,
                "obj_pos_y": obj_pos_y,
                "mask_threshold": mask_threshold,
                "selected_model": selected_model,
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
                "quality": quality,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "sd_2_upscaling": sd2upscaling,
                "seed": seed,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ObjectInpaintingPageResponse, parse_obj_as(type_=ObjectInpaintingPageResponse, object_=_response.json()))  # type: ignore
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

    def async_object_inpainting(
        self,
        *,
        input_image: str,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
        mask_threshold: typing.Optional[float] = OMIT,
        selected_model: typing.Optional[ObjectInpaintingPageRequestSelectedModel] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        sd2upscaling: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        input_image : str

        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

        mask_threshold : typing.Optional[float]

        selected_model : typing.Optional[ObjectInpaintingPageRequestSelectedModel]

        negative_prompt : typing.Optional[str]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        sd2upscaling : typing.Optional[bool]

        seed : typing.Optional[int]

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
        client.generate_product_photo_backgrounds.async_object_inpainting(
            input_image="input_image",
            text_prompt="text_prompt",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/ObjectInpainting/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "text_prompt": text_prompt,
                "obj_scale": obj_scale,
                "obj_pos_x": obj_pos_x,
                "obj_pos_y": obj_pos_y,
                "mask_threshold": mask_threshold,
                "selected_model": selected_model,
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
                "quality": quality,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "sd_2_upscaling": sd2upscaling,
                "seed": seed,
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

    def status_object_inpainting(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ObjectInpaintingPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectInpaintingPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
            api_key="YOUR_API_KEY",
        )
        client.generate_product_photo_backgrounds.status_object_inpainting(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/ObjectInpainting/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ObjectInpaintingPageStatusResponse, parse_obj_as(type_=ObjectInpaintingPageStatusResponse, object_=_response.json()))  # type: ignore
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


class AsyncGenerateProductPhotoBackgroundsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def object_inpainting(
        self,
        *,
        input_image: str,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
        mask_threshold: typing.Optional[float] = OMIT,
        selected_model: typing.Optional[ObjectInpaintingPageRequestSelectedModel] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        sd2upscaling: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> ObjectInpaintingPageResponse:
        """
        Parameters
        ----------
        input_image : str

        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

        mask_threshold : typing.Optional[float]

        selected_model : typing.Optional[ObjectInpaintingPageRequestSelectedModel]

        negative_prompt : typing.Optional[str]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        sd2upscaling : typing.Optional[bool]

        seed : typing.Optional[int]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectInpaintingPageResponse
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
            await client.generate_product_photo_backgrounds.object_inpainting(
                input_image="input_image",
                text_prompt="text_prompt",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/ObjectInpainting/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "text_prompt": text_prompt,
                "obj_scale": obj_scale,
                "obj_pos_x": obj_pos_x,
                "obj_pos_y": obj_pos_y,
                "mask_threshold": mask_threshold,
                "selected_model": selected_model,
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
                "quality": quality,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "sd_2_upscaling": sd2upscaling,
                "seed": seed,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ObjectInpaintingPageResponse, parse_obj_as(type_=ObjectInpaintingPageResponse, object_=_response.json()))  # type: ignore
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

    async def async_object_inpainting(
        self,
        *,
        input_image: str,
        text_prompt: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
        mask_threshold: typing.Optional[float] = OMIT,
        selected_model: typing.Optional[ObjectInpaintingPageRequestSelectedModel] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[int] = OMIT,
        output_width: typing.Optional[int] = OMIT,
        output_height: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        sd2upscaling: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncApiResponseModelV3:
        """
        Parameters
        ----------
        input_image : str

        text_prompt : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

        mask_threshold : typing.Optional[float]

        selected_model : typing.Optional[ObjectInpaintingPageRequestSelectedModel]

        negative_prompt : typing.Optional[str]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[int]

        output_width : typing.Optional[int]

        output_height : typing.Optional[int]

        guidance_scale : typing.Optional[float]

        sd2upscaling : typing.Optional[bool]

        seed : typing.Optional[int]

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
            await client.generate_product_photo_backgrounds.async_object_inpainting(
                input_image="input_image",
                text_prompt="text_prompt",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/ObjectInpainting/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "text_prompt": text_prompt,
                "obj_scale": obj_scale,
                "obj_pos_x": obj_pos_x,
                "obj_pos_y": obj_pos_y,
                "mask_threshold": mask_threshold,
                "selected_model": selected_model,
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
                "quality": quality,
                "output_width": output_width,
                "output_height": output_height,
                "guidance_scale": guidance_scale,
                "sd_2_upscaling": sd2upscaling,
                "seed": seed,
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

    async def status_object_inpainting(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ObjectInpaintingPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObjectInpaintingPageStatusResponse
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
            await client.generate_product_photo_backgrounds.status_object_inpainting(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/ObjectInpainting/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ObjectInpaintingPageStatusResponse, parse_obj_as(type_=ObjectInpaintingPageStatusResponse, object_=_response.json()))  # type: ignore
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
