# This file was auto-generated by Fern from our API Definition.

import typing

from .img2img_page_request_selected_controlnet_model_item import Img2ImgPageRequestSelectedControlnetModelItem

Img2ImgPageRequestSelectedControlnetModel = typing.Union[
    typing.List[Img2ImgPageRequestSelectedControlnetModelItem],
    typing.Literal["sd_controlnet_canny"],
    typing.Literal["sd_controlnet_depth"],
    typing.Literal["sd_controlnet_hed"],
    typing.Literal["sd_controlnet_mlsd"],
    typing.Literal["sd_controlnet_normal"],
    typing.Literal["sd_controlnet_openpose"],
    typing.Literal["sd_controlnet_scribble"],
    typing.Literal["sd_controlnet_seg"],
    typing.Literal["sd_controlnet_tile"],
    typing.Literal["sd_controlnet_brightness"],
    typing.Literal["control_v1p_sd15_qrcode_monster_v2"],
]
