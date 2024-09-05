# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .face_inpainting_page_request_selected_model import FaceInpaintingPageRequestSelectedModel
from .recipe_function import RecipeFunction
from .run_settings import RunSettings


class FaceInpaintingPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    input_image: str
    text_prompt: str
    face_scale: typing.Optional[float] = None
    face_pos_x: typing.Optional[float] = None
    face_pos_y: typing.Optional[float] = None
    selected_model: typing.Optional[FaceInpaintingPageRequestSelectedModel] = None
    negative_prompt: typing.Optional[str] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[int] = None
    upscale_factor: typing.Optional[float] = None
    output_width: typing.Optional[int] = None
    output_height: typing.Optional[int] = None
    guidance_scale: typing.Optional[float] = None
    seed: typing.Optional[int] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
