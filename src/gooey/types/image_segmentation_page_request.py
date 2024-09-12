# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .recipe_function import RecipeFunction
import pydantic
from .image_segmentation_page_request_selected_model import ImageSegmentationPageRequestSelectedModel
from .run_settings import RunSettings
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ImageSegmentationPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    input_image: str
    selected_model: typing.Optional[ImageSegmentationPageRequestSelectedModel] = None
    mask_threshold: typing.Optional[float] = None
    rect_persepective_transform: typing.Optional[bool] = None
    reflection_opacity: typing.Optional[float] = None
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
