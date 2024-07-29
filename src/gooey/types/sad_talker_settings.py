# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .preprocess import Preprocess


class SadTalkerSettings(UniversalBaseModel):
    still: typing.Optional[bool] = None
    preprocess: typing.Optional[Preprocess] = pydantic.Field(default=None)
    """
    SadTalker only generates 512x512 output. 'crop' handles this by cropping the input to 512x512. 'resize' scales down the input to fit 512x512 and scales it back up after lipsyncing (does not work well for full person images, better for portraits). 'full' processes the cropped region and pastes it back into the original input. 'extcrop' and 'extfull' are similar to 'crop' and 'full' but with extended cropping.
    """

    pose_style: typing.Optional[int] = pydantic.Field(default=None)
    """
    Random seed 0-45 inclusive that affects how the pose is animated.
    """

    expression_scale: typing.Optional[float] = pydantic.Field(default=None)
    """
    Scale the amount of expression motion. 1.0 is normal, 0.5 is very reduced, and 2.0 is quite a lot.
    """

    ref_eyeblink: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional reference video for eyeblinks to make the eyebrow movement more natural.
    """

    ref_pose: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional reference video to pose the head.
    """

    input_yaw: typing.Optional[typing.List[int]] = None
    input_pitch: typing.Optional[typing.List[int]] = None
    input_roll: typing.Optional[typing.List[int]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow