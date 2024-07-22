# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .email_face_inpainting_page_request_selected_model import EmailFaceInpaintingPageRequestSelectedModel
from .recipe_function import RecipeFunction
from .run_settings import RunSettings


class EmailFaceInpaintingPageRequest(pydantic_v1.BaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    email_address: typing.Optional[str] = None
    twitter_handle: typing.Optional[str] = None
    text_prompt: str
    face_scale: typing.Optional[float] = None
    face_pos_x: typing.Optional[float] = None
    face_pos_y: typing.Optional[float] = None
    selected_model: typing.Optional[EmailFaceInpaintingPageRequestSelectedModel] = None
    negative_prompt: typing.Optional[str] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[int] = None
    upscale_factor: typing.Optional[float] = None
    output_width: typing.Optional[int] = None
    output_height: typing.Optional[int] = None
    guidance_scale: typing.Optional[float] = None
    should_send_email: typing.Optional[bool] = None
    email_from: typing.Optional[str] = None
    email_cc: typing.Optional[str] = None
    email_bcc: typing.Optional[str] = None
    email_subject: typing.Optional[str] = None
    email_body: typing.Optional[str] = None
    email_body_enable_html: typing.Optional[bool] = None
    fallback_email_body: typing.Optional[str] = None
    seed: typing.Optional[int] = None
    settings: typing.Optional[RunSettings] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
