# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ConversationStart(UniversalBaseModel):
    conversation_id: str = pydantic.Field()
    """
    The conversation ID you provided in the request, or a random ID if not provided
    """

    user_id: str = pydantic.Field()
    """
    The user ID associated with this conversation
    """

    user_message_id: str = pydantic.Field()
    """
    The user message ID you provided in the request, or a random ID if not provided.
    """

    bot_message_id: str = pydantic.Field()
    """
    The bot message ID. Use this ID as the `context_msg_id` when sending a `button_pressed`.
    """

    created_at: str = pydantic.Field()
    """
    Time when the conversation was created as ISO format
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The conversation was started. Save the IDs for future requests.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
