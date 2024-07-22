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
from ..types.image_segmentation_page_request_selected_model import ImageSegmentationPageRequestSelectedModel
from ..types.image_segmentation_page_response import ImageSegmentationPageResponse
from ..types.image_segmentation_page_status_response import ImageSegmentationPageStatusResponse
from ..types.recipe_function import RecipeFunction
from ..types.run_settings import RunSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AiBackgroundChangerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def image_segmentation(
        self,
        *,
        input_image: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        selected_model: typing.Optional[ImageSegmentationPageRequestSelectedModel] = OMIT,
        mask_threshold: typing.Optional[float] = OMIT,
        rect_persepective_transform: typing.Optional[bool] = OMIT,
        reflection_opacity: typing.Optional[float] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> ImageSegmentationPageResponse:
        """
        Parameters
        ----------
        input_image : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        selected_model : typing.Optional[ImageSegmentationPageRequestSelectedModel]

        mask_threshold : typing.Optional[float]

        rect_persepective_transform : typing.Optional[bool]

        reflection_opacity : typing.Optional[float]

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageSegmentationPageResponse
            Successful Response

        Examples
        --------
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
        )
        client.ai_background_changer.image_segmentation(
            input_image="input_image",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/ImageSegmentation/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "selected_model": selected_model,
                "mask_threshold": mask_threshold,
                "rect_persepective_transform": rect_persepective_transform,
                "reflection_opacity": reflection_opacity,
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
                return pydantic_v1.parse_obj_as(ImageSegmentationPageResponse, _response.json())  # type: ignore
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

    def async_image_segmentation(
        self,
        *,
        input_image: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        selected_model: typing.Optional[ImageSegmentationPageRequestSelectedModel] = OMIT,
        mask_threshold: typing.Optional[float] = OMIT,
        rect_persepective_transform: typing.Optional[bool] = OMIT,
        reflection_opacity: typing.Optional[float] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
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

        selected_model : typing.Optional[ImageSegmentationPageRequestSelectedModel]

        mask_threshold : typing.Optional[float]

        rect_persepective_transform : typing.Optional[bool]

        reflection_opacity : typing.Optional[float]

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
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
        )
        client.ai_background_changer.async_image_segmentation(
            input_image="input_image",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/ImageSegmentation/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "selected_model": selected_model,
                "mask_threshold": mask_threshold,
                "rect_persepective_transform": rect_persepective_transform,
                "reflection_opacity": reflection_opacity,
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

    def status_image_segmentation(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ImageSegmentationPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageSegmentationPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey.client import Gooey

        client = Gooey(
            authorization="YOUR_AUTHORIZATION",
        )
        client.ai_background_changer.status_image_segmentation(
            run_id="run_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/ImageSegmentation/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ImageSegmentationPageStatusResponse, _response.json())  # type: ignore
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


class AsyncAiBackgroundChangerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def image_segmentation(
        self,
        *,
        input_image: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        selected_model: typing.Optional[ImageSegmentationPageRequestSelectedModel] = OMIT,
        mask_threshold: typing.Optional[float] = OMIT,
        rect_persepective_transform: typing.Optional[bool] = OMIT,
        reflection_opacity: typing.Optional[float] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> ImageSegmentationPageResponse:
        """
        Parameters
        ----------
        input_image : str

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        selected_model : typing.Optional[ImageSegmentationPageRequestSelectedModel]

        mask_threshold : typing.Optional[float]

        rect_persepective_transform : typing.Optional[bool]

        reflection_opacity : typing.Optional[float]

        obj_scale : typing.Optional[float]

        obj_pos_x : typing.Optional[float]

        obj_pos_y : typing.Optional[float]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageSegmentationPageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
        )


        async def main() -> None:
            await client.ai_background_changer.image_segmentation(
                input_image="input_image",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/ImageSegmentation/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "selected_model": selected_model,
                "mask_threshold": mask_threshold,
                "rect_persepective_transform": rect_persepective_transform,
                "reflection_opacity": reflection_opacity,
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
                return pydantic_v1.parse_obj_as(ImageSegmentationPageResponse, _response.json())  # type: ignore
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

    async def async_image_segmentation(
        self,
        *,
        input_image: str,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        selected_model: typing.Optional[ImageSegmentationPageRequestSelectedModel] = OMIT,
        mask_threshold: typing.Optional[float] = OMIT,
        rect_persepective_transform: typing.Optional[bool] = OMIT,
        reflection_opacity: typing.Optional[float] = OMIT,
        obj_scale: typing.Optional[float] = OMIT,
        obj_pos_x: typing.Optional[float] = OMIT,
        obj_pos_y: typing.Optional[float] = OMIT,
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

        selected_model : typing.Optional[ImageSegmentationPageRequestSelectedModel]

        mask_threshold : typing.Optional[float]

        rect_persepective_transform : typing.Optional[bool]

        reflection_opacity : typing.Optional[float]

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

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
        )


        async def main() -> None:
            await client.ai_background_changer.async_image_segmentation(
                input_image="input_image",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/ImageSegmentation/async/",
            method="POST",
            json={
                "functions": functions,
                "variables": variables,
                "input_image": input_image,
                "selected_model": selected_model,
                "mask_threshold": mask_threshold,
                "rect_persepective_transform": rect_persepective_transform,
                "reflection_opacity": reflection_opacity,
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

    async def status_image_segmentation(
        self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ImageSegmentationPageStatusResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageSegmentationPageStatusResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey.client import AsyncGooey

        client = AsyncGooey(
            authorization="YOUR_AUTHORIZATION",
        )


        async def main() -> None:
            await client.ai_background_changer.status_image_segmentation(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/ImageSegmentation/status/", method="GET", params={"run_id": run_id}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ImageSegmentationPageStatusResponse, _response.json())  # type: ignore
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
