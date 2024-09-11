# This file was auto-generated by Fern from our API Definition.

import typing
from ...types.conversation_start import ConversationStart
from ...types.run_start import RunStart
from ...types.message_part import MessagePart
from ...types.final_response import FinalResponse
from ...types.stream_error import StreamError

VideoBotsStreamResponse = typing.Union[ConversationStart, RunStart, MessagePart, FinalResponse, StreamError]
