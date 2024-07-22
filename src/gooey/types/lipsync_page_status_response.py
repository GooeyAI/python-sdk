# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .lipsync_page_output import LipsyncPageOutput
from .recipe_run_state import RecipeRunState


class LipsyncPageStatusResponse(pydantic_v1.BaseModel):
    run_id: str = pydantic_v1.Field()
    """
    Unique ID for this run
    """

    web_url: str = pydantic_v1.Field()
    """
    Web URL for this run
    """

    created_at: str = pydantic_v1.Field()
    """
    Time when the run was created as ISO format
    """

    run_time_sec: int = pydantic_v1.Field()
    """
    Total run time in seconds
    """

    status: RecipeRunState = pydantic_v1.Field()
    """
    Status of the run
    """

    detail: str = pydantic_v1.Field()
    """
    Details about the status of the run as a human readable string
    """

    output: typing.Optional[LipsyncPageOutput] = pydantic_v1.Field(default=None)
    """
    Output of the run. Only available if status is `"completed"`
    """

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
