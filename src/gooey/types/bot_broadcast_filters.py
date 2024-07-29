# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BotBroadcastFilters(UniversalBaseModel):
    wa_phone_number_in: typing.Optional[typing.List[str]] = pydantic.Field(alias="wa_phone_number__in", default=None)
    """
    A list of WhatsApp phone numbers to broadcast to.
    """

    slack_user_id_in: typing.Optional[typing.List[str]] = pydantic.Field(alias="slack_user_id__in", default=None)
    """
    A list of Slack user IDs to broadcast to.
    """

    slack_user_name_icontains: typing.Optional[str] = pydantic.Field(alias="slack_user_name__icontains", default=None)
    """
    Filter by the Slack user's name. Case insensitive.
    """

    slack_channel_is_personal: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Filter by whether the Slack channel is personal. By default, will broadcast to both public and personal slack channels.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
