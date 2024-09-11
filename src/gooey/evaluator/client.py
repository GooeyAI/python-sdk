# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.recipe_function import RecipeFunction
from ..types.eval_prompt import EvalPrompt
from ..types.agg_function import AggFunction
from .types.bulk_eval_page_request_selected_model import BulkEvalPageRequestSelectedModel
from .types.bulk_eval_page_request_response_format_type import BulkEvalPageRequestResponseFormatType
from ..types.run_settings import RunSettings
from ..core.request_options import RequestOptions
from ..types.bulk_eval_page_status_response import BulkEvalPageStatusResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.generic_error_response import GenericErrorResponse
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EvaluatorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def async_bulk_eval(
        self,
        *,
        documents: typing.Sequence[str],
        example_id: typing.Optional[str] = None,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        eval_prompts: typing.Optional[typing.Sequence[EvalPrompt]] = OMIT,
        agg_functions: typing.Optional[typing.Sequence[AggFunction]] = OMIT,
        selected_model: typing.Optional[BulkEvalPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[BulkEvalPageRequestResponseFormatType] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkEvalPageStatusResponse:
        """
        Parameters
        ----------
        documents : typing.Sequence[str]

            Upload or link to a CSV or google sheet that contains your sample input data.
            For example, for Copilot, this would sample questions or for Art QR Code, would would be pairs of image descriptions and URLs.
            Remember to includes header names in your CSV too.


        example_id : typing.Optional[str]

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        eval_prompts : typing.Optional[typing.Sequence[EvalPrompt]]

            Specify custom LLM prompts to calculate metrics that evaluate each row of the input data. The output should be a JSON object mapping the metric names to values.
            _The `columns` dictionary can be used to reference the spreadsheet columns._


        agg_functions : typing.Optional[typing.Sequence[AggFunction]]

            Aggregate using one or more operations. Uses [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html#dataframegroupby-computations-descriptive-stats).


        selected_model : typing.Optional[BulkEvalPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[BulkEvalPageRequestResponseFormatType]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkEvalPageStatusResponse
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            api_key="YOUR_API_KEY",
        )
        client.evaluator.async_bulk_eval(
            documents=["documents"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/bulk-eval/async",
            method="POST",
            params={
                "example_id": example_id,
            },
            json={
                "functions": functions,
                "variables": variables,
                "documents": documents,
                "eval_prompts": eval_prompts,
                "agg_functions": agg_functions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "response_format_type": response_format_type,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BulkEvalPageStatusResponse,
                    parse_obj_as(
                        type_=BulkEvalPageStatusResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        GenericErrorResponse,
                        parse_obj_as(
                            type_=GenericErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEvaluatorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def async_bulk_eval(
        self,
        *,
        documents: typing.Sequence[str],
        example_id: typing.Optional[str] = None,
        functions: typing.Optional[typing.Sequence[RecipeFunction]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        eval_prompts: typing.Optional[typing.Sequence[EvalPrompt]] = OMIT,
        agg_functions: typing.Optional[typing.Sequence[AggFunction]] = OMIT,
        selected_model: typing.Optional[BulkEvalPageRequestSelectedModel] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[BulkEvalPageRequestResponseFormatType] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkEvalPageStatusResponse:
        """
        Parameters
        ----------
        documents : typing.Sequence[str]

            Upload or link to a CSV or google sheet that contains your sample input data.
            For example, for Copilot, this would sample questions or for Art QR Code, would would be pairs of image descriptions and URLs.
            Remember to includes header names in your CSV too.


        example_id : typing.Optional[str]

        functions : typing.Optional[typing.Sequence[RecipeFunction]]

        variables : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        eval_prompts : typing.Optional[typing.Sequence[EvalPrompt]]

            Specify custom LLM prompts to calculate metrics that evaluate each row of the input data. The output should be a JSON object mapping the metric names to values.
            _The `columns` dictionary can be used to reference the spreadsheet columns._


        agg_functions : typing.Optional[typing.Sequence[AggFunction]]

            Aggregate using one or more operations. Uses [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html#dataframegroupby-computations-descriptive-stats).


        selected_model : typing.Optional[BulkEvalPageRequestSelectedModel]

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[BulkEvalPageRequestResponseFormatType]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkEvalPageStatusResponse
            Successful Response

        Examples
        --------
        import asyncio

        from gooey import AsyncGooey

        client = AsyncGooey(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.evaluator.async_bulk_eval(
                documents=["documents"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/bulk-eval/async",
            method="POST",
            params={
                "example_id": example_id,
            },
            json={
                "functions": functions,
                "variables": variables,
                "documents": documents,
                "eval_prompts": eval_prompts,
                "agg_functions": agg_functions,
                "selected_model": selected_model,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "response_format_type": response_format_type,
                "settings": settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BulkEvalPageStatusResponse,
                    parse_obj_as(
                        type_=BulkEvalPageStatusResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        GenericErrorResponse,
                        parse_obj_as(
                            type_=GenericErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
