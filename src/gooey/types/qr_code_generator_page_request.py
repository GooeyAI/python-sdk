# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .recipe_function import RecipeFunction
import pydantic
from .vcard import Vcard
from .control_net_models import ControlNetModels
from .text_to_image_models import TextToImageModels
from .schedulers import Schedulers
from .run_settings import RunSettings
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class QrCodeGeneratorPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    qr_code_data: typing.Optional[str] = None
    qr_code_input_image: typing.Optional[str] = None
    qr_code_vcard: typing.Optional[Vcard] = None
    qr_code_file: typing.Optional[str] = None
    use_url_shortener: typing.Optional[bool] = None
    text_prompt: str
    negative_prompt: typing.Optional[str] = None
    image_prompt: typing.Optional[str] = None
    image_prompt_controlnet_models: typing.Optional[typing.List[ControlNetModels]] = None
    image_prompt_strength: typing.Optional[float] = None
    image_prompt_scale: typing.Optional[float] = None
    image_prompt_pos_x: typing.Optional[float] = None
    image_prompt_pos_y: typing.Optional[float] = None
    selected_model: typing.Optional[TextToImageModels] = None
    selected_controlnet_model: typing.Optional[typing.List[ControlNetModels]] = None
    output_width: typing.Optional[int] = None
    output_height: typing.Optional[int] = None
    guidance_scale: typing.Optional[float] = None
    controlnet_conditioning_scale: typing.Optional[typing.List[float]] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[int] = None
    scheduler: typing.Optional[Schedulers] = None
    seed: typing.Optional[int] = None
    obj_scale: typing.Optional[float] = None
    obj_pos_x: typing.Optional[float] = None
    obj_pos_y: typing.Optional[float] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
