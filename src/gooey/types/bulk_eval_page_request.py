# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agg_function import AggFunction
from .bulk_eval_page_request_response_format_type import BulkEvalPageRequestResponseFormatType
from .bulk_eval_page_request_selected_model import BulkEvalPageRequestSelectedModel
from .eval_prompt import EvalPrompt
from .recipe_function import RecipeFunction
from .run_settings import RunSettings


class BulkEvalPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[RecipeFunction]] = None
    variables: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    documents: typing.List[str] = pydantic.Field()
    """
    Upload or link to a CSV or google sheet that contains your sample input data.
    For example, for Copilot, this would sample questions or for Art QR Code, would would be pairs of image descriptions and URLs.
    Remember to includes header names in your CSV too.
    """

    eval_prompts: typing.Optional[typing.List[EvalPrompt]] = pydantic.Field(default=None)
    """
    Specify custom LLM prompts to calculate metrics that evaluate each row of the input data. The output should be a JSON object mapping the metric names to values.  
    _The `columns` dictionary can be used to reference the spreadsheet columns._  
    """

    agg_functions: typing.Optional[typing.List[AggFunction]] = pydantic.Field(default=None)
    """
    Aggregate using one or more operations. Uses [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html#dataframegroupby-computations-descriptive-stats).
    """

    selected_model: typing.Optional[BulkEvalPageRequestSelectedModel] = None
    avoid_repetition: typing.Optional[bool] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[float] = None
    max_tokens: typing.Optional[int] = None
    sampling_temperature: typing.Optional[float] = None
    response_format_type: typing.Optional[BulkEvalPageRequestResponseFormatType] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
