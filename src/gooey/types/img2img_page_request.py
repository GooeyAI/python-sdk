# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .recipe_function import RecipeFunction
import pydantic
from .image_to_image_models import ImageToImageModels
from .selected_control_net_models import SelectedControlNetModels
from .run_settings import RunSettings
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Img2ImgPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    input_image: str
    text_prompt: typing.Optional[str] = None
    selected_model: typing.Optional[ImageToImageModels] = None
    selected_controlnet_model: typing.Optional[SelectedControlNetModels] = None
    negative_prompt: typing.Optional[str] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[int] = None
    output_width: typing.Optional[int] = None
    output_height: typing.Optional[int] = None
    guidance_scale: typing.Optional[float] = None
    prompt_strength: typing.Optional[float] = None
    controlnet_conditioning_scale: typing.Optional[typing.List[float]] = None
    seed: typing.Optional[int] = None
    image_guidance_scale: typing.Optional[float] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
