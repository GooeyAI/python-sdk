# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class RunStart(pydantic_v1.BaseModel):
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

    status_url: str = pydantic_v1.Field()
    """
    URL to check the status of the run. Also included in the `Location` header of the response.
    """

    type: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The run was started. Save the IDs for future requests.Use the `status_url` to check the status of the run and fetch the complete output.
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
