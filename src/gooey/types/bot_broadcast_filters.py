# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class BotBroadcastFilters(pydantic_v1.BaseModel):
    wa_phone_number_in: typing.Optional[typing.List[str]] = pydantic_v1.Field(alias="wa_phone_number__in", default=None)
    """
    A list of WhatsApp phone numbers to broadcast to.
    """

    slack_user_id_in: typing.Optional[typing.List[str]] = pydantic_v1.Field(alias="slack_user_id__in", default=None)
    """
    A list of Slack user IDs to broadcast to.
    """

    slack_user_name_icontains: typing.Optional[str] = pydantic_v1.Field(
        alias="slack_user_name__icontains", default=None
    )
    """
    Filter by the Slack user's name. Case insensitive.
    """

    slack_channel_is_personal: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Filter by whether the Slack channel is personal. By default, will broadcast to both public and personal slack channels.
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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
