# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .recipe_run_state import RecipeRunState
import typing
from .embeddings_page_output import EmbeddingsPageOutput
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class EmbeddingsPageStatusResponse(UniversalBaseModel):
    run_id: str = pydantic.Field()
    """
    Unique ID for this run
    """

    web_url: str = pydantic.Field()
    """
    Web URL for this run
    """

    created_at: str = pydantic.Field()
    """
    Time when the run was created as ISO format
    """

    run_time_sec: float = pydantic.Field()
    """
    Total run time in seconds
    """

    status: RecipeRunState = pydantic.Field()
    """
    Status of the run
    """

    detail: str = pydantic.Field()
    """
    Details about the status of the run as a human readable string
    """

    output: typing.Optional[EmbeddingsPageOutput] = pydantic.Field(default=None)
    """
    Output of the run. Only available if status is `"completed"`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
