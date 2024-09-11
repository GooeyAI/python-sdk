# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .types.copilot_completion_request_functions_item import CopilotCompletionRequestFunctionsItem
from .. import core
from .types.copilot_completion_request_messages_item import CopilotCompletionRequestMessagesItem
from .types.copilot_completion_request_selected_model import CopilotCompletionRequestSelectedModel
from .types.copilot_completion_request_embedding_model import CopilotCompletionRequestEmbeddingModel
from .types.copilot_completion_request_citation_style import CopilotCompletionRequestCitationStyle
from .types.copilot_completion_request_asr_model import CopilotCompletionRequestAsrModel
from .types.copilot_completion_request_translation_model import CopilotCompletionRequestTranslationModel
from .types.copilot_completion_request_lipsync_model import CopilotCompletionRequestLipsyncModel
from .types.copilot_completion_request_response_format_type import CopilotCompletionRequestResponseFormatType
from .types.copilot_completion_request_tts_provider import CopilotCompletionRequestTtsProvider
from .types.copilot_completion_request_openai_voice_name import CopilotCompletionRequestOpenaiVoiceName
from .types.copilot_completion_request_openai_tts_model import CopilotCompletionRequestOpenaiTtsModel
from .types.copilot_completion_request_sadtalker_settings import CopilotCompletionRequestSadtalkerSettings
from ..types.run_settings import RunSettings
from ..core.request_options import RequestOptions
from ..types.video_bots_page_output import VideoBotsPageOutput
from ..core.pydantic_utilities import parse_obj_as
from ..errors.payment_required_error import PaymentRequiredError
from ..types.generic_error_response import GenericErrorResponse
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..errors.too_many_requests_error import TooManyRequestsError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CopilotClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def completion(
        self,
        *,
        example_id: typing.Optional[str] = None,
        functions: typing.Optional[typing.List[CopilotCompletionRequestFunctionsItem]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        input_prompt: typing.Optional[str] = OMIT,
        input_audio: typing.Optional[str] = OMIT,
        input_images: typing.Optional[typing.List[core.File]] = OMIT,
        input_documents: typing.Optional[typing.List[core.File]] = OMIT,
        doc_extract_url: typing.Optional[str] = OMIT,
        messages: typing.Optional[typing.List[CopilotCompletionRequestMessagesItem]] = OMIT,
        bot_script: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[CopilotCompletionRequestSelectedModel] = OMIT,
        document_model: typing.Optional[str] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        keyword_instructions: typing.Optional[str] = OMIT,
        documents: typing.Optional[typing.List[core.File]] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        embedding_model: typing.Optional[CopilotCompletionRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        citation_style: typing.Optional[CopilotCompletionRequestCitationStyle] = OMIT,
        use_url_shortener: typing.Optional[bool] = OMIT,
        asr_model: typing.Optional[CopilotCompletionRequestAsrModel] = OMIT,
        asr_language: typing.Optional[str] = OMIT,
        translation_model: typing.Optional[CopilotCompletionRequestTranslationModel] = OMIT,
        user_language: typing.Optional[str] = OMIT,
        input_glossary_document: typing.Optional[core.File] = OMIT,
        output_glossary_document: typing.Optional[core.File] = OMIT,
        lipsync_model: typing.Optional[CopilotCompletionRequestLipsyncModel] = OMIT,
        tools: typing.Optional[typing.List[typing.Literal["json_to_pdf"]]] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[CopilotCompletionRequestResponseFormatType] = OMIT,
        tts_provider: typing.Optional[CopilotCompletionRequestTtsProvider] = OMIT,
        uberduck_voice_name: typing.Optional[str] = OMIT,
        uberduck_speaking_rate: typing.Optional[float] = OMIT,
        google_voice_name: typing.Optional[str] = OMIT,
        google_speaking_rate: typing.Optional[float] = OMIT,
        google_pitch: typing.Optional[float] = OMIT,
        bark_history_prompt: typing.Optional[str] = OMIT,
        elevenlabs_voice_name: typing.Optional[str] = OMIT,
        elevenlabs_api_key: typing.Optional[str] = OMIT,
        elevenlabs_voice_id: typing.Optional[str] = OMIT,
        elevenlabs_model: typing.Optional[str] = OMIT,
        elevenlabs_stability: typing.Optional[float] = OMIT,
        elevenlabs_similarity_boost: typing.Optional[float] = OMIT,
        elevenlabs_style: typing.Optional[float] = OMIT,
        elevenlabs_speaker_boost: typing.Optional[bool] = OMIT,
        azure_voice_name: typing.Optional[str] = OMIT,
        openai_voice_name: typing.Optional[CopilotCompletionRequestOpenaiVoiceName] = OMIT,
        openai_tts_model: typing.Optional[CopilotCompletionRequestOpenaiTtsModel] = OMIT,
        input_face: typing.Optional[core.File] = OMIT,
        face_padding_top: typing.Optional[int] = OMIT,
        face_padding_bottom: typing.Optional[int] = OMIT,
        face_padding_left: typing.Optional[int] = OMIT,
        face_padding_right: typing.Optional[int] = OMIT,
        sadtalker_settings: typing.Optional[CopilotCompletionRequestSadtalkerSettings] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VideoBotsPageOutput:
        """
        Parameters
        ----------
        example_id : typing.Optional[str]

        functions : typing.Optional[typing.List[CopilotCompletionRequestFunctionsItem]]

        variables : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        input_prompt : typing.Optional[str]

        input_audio : typing.Optional[str]

        input_images : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        input_documents : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        doc_extract_url : typing.Optional[str]
            Select a workflow to extract text from documents and images.

        messages : typing.Optional[typing.List[CopilotCompletionRequestMessagesItem]]

        bot_script : typing.Optional[str]

        selected_model : typing.Optional[CopilotCompletionRequestSelectedModel]

        document_model : typing.Optional[str]
            When your copilot users upload a photo or pdf, what kind of document are they mostly likely to upload? (via [Azure](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api?view=doc-intel-3.1.0&tabs=linux&pivots=programming-language-rest-api))

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        keyword_instructions : typing.Optional[str]

        documents : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        embedding_model : typing.Optional[CopilotCompletionRequestEmbeddingModel]

        dense_weight : typing.Optional[float]

            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.


        citation_style : typing.Optional[CopilotCompletionRequestCitationStyle]

        use_url_shortener : typing.Optional[bool]

        asr_model : typing.Optional[CopilotCompletionRequestAsrModel]
            Choose a model to transcribe incoming audio messages to text.

        asr_language : typing.Optional[str]
            Choose a language to transcribe incoming audio messages to text.

        translation_model : typing.Optional[CopilotCompletionRequestTranslationModel]

        user_language : typing.Optional[str]
            Choose a language to translate incoming text & audio messages to English and responses back to your selected language. Useful for low-resource languages.

        input_glossary_document : typing.Optional[core.File]
            See core.File for more documentation

        output_glossary_document : typing.Optional[core.File]
            See core.File for more documentation

        lipsync_model : typing.Optional[CopilotCompletionRequestLipsyncModel]

        tools : typing.Optional[typing.List[typing.Literal["json_to_pdf"]]]
            Give your copilot superpowers by giving it access to tools. Powered by [Function calling](https://platform.openai.com/docs/guides/function-calling).

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[CopilotCompletionRequestResponseFormatType]

        tts_provider : typing.Optional[CopilotCompletionRequestTtsProvider]

        uberduck_voice_name : typing.Optional[str]

        uberduck_speaking_rate : typing.Optional[float]

        google_voice_name : typing.Optional[str]

        google_speaking_rate : typing.Optional[float]

        google_pitch : typing.Optional[float]

        bark_history_prompt : typing.Optional[str]

        elevenlabs_voice_name : typing.Optional[str]
            Use `elevenlabs_voice_id` instead

        elevenlabs_api_key : typing.Optional[str]

        elevenlabs_voice_id : typing.Optional[str]

        elevenlabs_model : typing.Optional[str]

        elevenlabs_stability : typing.Optional[float]

        elevenlabs_similarity_boost : typing.Optional[float]

        elevenlabs_style : typing.Optional[float]

        elevenlabs_speaker_boost : typing.Optional[bool]

        azure_voice_name : typing.Optional[str]

        openai_voice_name : typing.Optional[CopilotCompletionRequestOpenaiVoiceName]

        openai_tts_model : typing.Optional[CopilotCompletionRequestOpenaiTtsModel]

        input_face : typing.Optional[core.File]
            See core.File for more documentation

        face_padding_top : typing.Optional[int]

        face_padding_bottom : typing.Optional[int]

        face_padding_left : typing.Optional[int]

        face_padding_right : typing.Optional[int]

        sadtalker_settings : typing.Optional[CopilotCompletionRequestSadtalkerSettings]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VideoBotsPageOutput
            Successful Response

        Examples
        --------
        from gooey import Gooey

        client = Gooey(
            api_key="YOUR_API_KEY",
        )
        client.copilot.completion()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/video-bots/async",
            method="POST",
            params={
                "example_id": example_id,
            },
            data={
                "functions": functions,
                "variables": variables,
                "input_prompt": input_prompt,
                "input_audio": input_audio,
                "doc_extract_url": doc_extract_url,
                "messages": messages,
                "bot_script": bot_script,
                "selected_model": selected_model,
                "document_model": document_model,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "keyword_instructions": keyword_instructions,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
                "citation_style": citation_style,
                "use_url_shortener": use_url_shortener,
                "asr_model": asr_model,
                "asr_language": asr_language,
                "translation_model": translation_model,
                "user_language": user_language,
                "lipsync_model": lipsync_model,
                "tools": tools,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "response_format_type": response_format_type,
                "tts_provider": tts_provider,
                "uberduck_voice_name": uberduck_voice_name,
                "uberduck_speaking_rate": uberduck_speaking_rate,
                "google_voice_name": google_voice_name,
                "google_speaking_rate": google_speaking_rate,
                "google_pitch": google_pitch,
                "bark_history_prompt": bark_history_prompt,
                "elevenlabs_voice_name": elevenlabs_voice_name,
                "elevenlabs_api_key": elevenlabs_api_key,
                "elevenlabs_voice_id": elevenlabs_voice_id,
                "elevenlabs_model": elevenlabs_model,
                "elevenlabs_stability": elevenlabs_stability,
                "elevenlabs_similarity_boost": elevenlabs_similarity_boost,
                "elevenlabs_style": elevenlabs_style,
                "elevenlabs_speaker_boost": elevenlabs_speaker_boost,
                "azure_voice_name": azure_voice_name,
                "openai_voice_name": openai_voice_name,
                "openai_tts_model": openai_tts_model,
                "face_padding_top": face_padding_top,
                "face_padding_bottom": face_padding_bottom,
                "face_padding_left": face_padding_left,
                "face_padding_right": face_padding_right,
                "sadtalker_settings": sadtalker_settings,
                "settings": settings,
            },
            files={
                "input_images": input_images,
                "input_documents": input_documents,
                "documents": documents,
                "input_glossary_document": input_glossary_document,
                "output_glossary_document": output_glossary_document,
                "input_face": input_face,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    VideoBotsPageOutput,
                    parse_obj_as(
                        type_=VideoBotsPageOutput,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        GenericErrorResponse,
                        parse_obj_as(
                            type_=GenericErrorResponse,  # type: ignore
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


class AsyncCopilotClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def completion(
        self,
        *,
        example_id: typing.Optional[str] = None,
        functions: typing.Optional[typing.List[CopilotCompletionRequestFunctionsItem]] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        input_prompt: typing.Optional[str] = OMIT,
        input_audio: typing.Optional[str] = OMIT,
        input_images: typing.Optional[typing.List[core.File]] = OMIT,
        input_documents: typing.Optional[typing.List[core.File]] = OMIT,
        doc_extract_url: typing.Optional[str] = OMIT,
        messages: typing.Optional[typing.List[CopilotCompletionRequestMessagesItem]] = OMIT,
        bot_script: typing.Optional[str] = OMIT,
        selected_model: typing.Optional[CopilotCompletionRequestSelectedModel] = OMIT,
        document_model: typing.Optional[str] = OMIT,
        task_instructions: typing.Optional[str] = OMIT,
        query_instructions: typing.Optional[str] = OMIT,
        keyword_instructions: typing.Optional[str] = OMIT,
        documents: typing.Optional[typing.List[core.File]] = OMIT,
        max_references: typing.Optional[int] = OMIT,
        max_context_words: typing.Optional[int] = OMIT,
        scroll_jump: typing.Optional[int] = OMIT,
        embedding_model: typing.Optional[CopilotCompletionRequestEmbeddingModel] = OMIT,
        dense_weight: typing.Optional[float] = OMIT,
        citation_style: typing.Optional[CopilotCompletionRequestCitationStyle] = OMIT,
        use_url_shortener: typing.Optional[bool] = OMIT,
        asr_model: typing.Optional[CopilotCompletionRequestAsrModel] = OMIT,
        asr_language: typing.Optional[str] = OMIT,
        translation_model: typing.Optional[CopilotCompletionRequestTranslationModel] = OMIT,
        user_language: typing.Optional[str] = OMIT,
        input_glossary_document: typing.Optional[core.File] = OMIT,
        output_glossary_document: typing.Optional[core.File] = OMIT,
        lipsync_model: typing.Optional[CopilotCompletionRequestLipsyncModel] = OMIT,
        tools: typing.Optional[typing.List[typing.Literal["json_to_pdf"]]] = OMIT,
        avoid_repetition: typing.Optional[bool] = OMIT,
        num_outputs: typing.Optional[int] = OMIT,
        quality: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        sampling_temperature: typing.Optional[float] = OMIT,
        response_format_type: typing.Optional[CopilotCompletionRequestResponseFormatType] = OMIT,
        tts_provider: typing.Optional[CopilotCompletionRequestTtsProvider] = OMIT,
        uberduck_voice_name: typing.Optional[str] = OMIT,
        uberduck_speaking_rate: typing.Optional[float] = OMIT,
        google_voice_name: typing.Optional[str] = OMIT,
        google_speaking_rate: typing.Optional[float] = OMIT,
        google_pitch: typing.Optional[float] = OMIT,
        bark_history_prompt: typing.Optional[str] = OMIT,
        elevenlabs_voice_name: typing.Optional[str] = OMIT,
        elevenlabs_api_key: typing.Optional[str] = OMIT,
        elevenlabs_voice_id: typing.Optional[str] = OMIT,
        elevenlabs_model: typing.Optional[str] = OMIT,
        elevenlabs_stability: typing.Optional[float] = OMIT,
        elevenlabs_similarity_boost: typing.Optional[float] = OMIT,
        elevenlabs_style: typing.Optional[float] = OMIT,
        elevenlabs_speaker_boost: typing.Optional[bool] = OMIT,
        azure_voice_name: typing.Optional[str] = OMIT,
        openai_voice_name: typing.Optional[CopilotCompletionRequestOpenaiVoiceName] = OMIT,
        openai_tts_model: typing.Optional[CopilotCompletionRequestOpenaiTtsModel] = OMIT,
        input_face: typing.Optional[core.File] = OMIT,
        face_padding_top: typing.Optional[int] = OMIT,
        face_padding_bottom: typing.Optional[int] = OMIT,
        face_padding_left: typing.Optional[int] = OMIT,
        face_padding_right: typing.Optional[int] = OMIT,
        sadtalker_settings: typing.Optional[CopilotCompletionRequestSadtalkerSettings] = OMIT,
        settings: typing.Optional[RunSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VideoBotsPageOutput:
        """
        Parameters
        ----------
        example_id : typing.Optional[str]

        functions : typing.Optional[typing.List[CopilotCompletionRequestFunctionsItem]]

        variables : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Variables to be used as Jinja prompt templates and in functions as arguments

        input_prompt : typing.Optional[str]

        input_audio : typing.Optional[str]

        input_images : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        input_documents : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        doc_extract_url : typing.Optional[str]
            Select a workflow to extract text from documents and images.

        messages : typing.Optional[typing.List[CopilotCompletionRequestMessagesItem]]

        bot_script : typing.Optional[str]

        selected_model : typing.Optional[CopilotCompletionRequestSelectedModel]

        document_model : typing.Optional[str]
            When your copilot users upload a photo or pdf, what kind of document are they mostly likely to upload? (via [Azure](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api?view=doc-intel-3.1.0&tabs=linux&pivots=programming-language-rest-api))

        task_instructions : typing.Optional[str]

        query_instructions : typing.Optional[str]

        keyword_instructions : typing.Optional[str]

        documents : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        max_references : typing.Optional[int]

        max_context_words : typing.Optional[int]

        scroll_jump : typing.Optional[int]

        embedding_model : typing.Optional[CopilotCompletionRequestEmbeddingModel]

        dense_weight : typing.Optional[float]

            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.


        citation_style : typing.Optional[CopilotCompletionRequestCitationStyle]

        use_url_shortener : typing.Optional[bool]

        asr_model : typing.Optional[CopilotCompletionRequestAsrModel]
            Choose a model to transcribe incoming audio messages to text.

        asr_language : typing.Optional[str]
            Choose a language to transcribe incoming audio messages to text.

        translation_model : typing.Optional[CopilotCompletionRequestTranslationModel]

        user_language : typing.Optional[str]
            Choose a language to translate incoming text & audio messages to English and responses back to your selected language. Useful for low-resource languages.

        input_glossary_document : typing.Optional[core.File]
            See core.File for more documentation

        output_glossary_document : typing.Optional[core.File]
            See core.File for more documentation

        lipsync_model : typing.Optional[CopilotCompletionRequestLipsyncModel]

        tools : typing.Optional[typing.List[typing.Literal["json_to_pdf"]]]
            Give your copilot superpowers by giving it access to tools. Powered by [Function calling](https://platform.openai.com/docs/guides/function-calling).

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[CopilotCompletionRequestResponseFormatType]

        tts_provider : typing.Optional[CopilotCompletionRequestTtsProvider]

        uberduck_voice_name : typing.Optional[str]

        uberduck_speaking_rate : typing.Optional[float]

        google_voice_name : typing.Optional[str]

        google_speaking_rate : typing.Optional[float]

        google_pitch : typing.Optional[float]

        bark_history_prompt : typing.Optional[str]

        elevenlabs_voice_name : typing.Optional[str]
            Use `elevenlabs_voice_id` instead

        elevenlabs_api_key : typing.Optional[str]

        elevenlabs_voice_id : typing.Optional[str]

        elevenlabs_model : typing.Optional[str]

        elevenlabs_stability : typing.Optional[float]

        elevenlabs_similarity_boost : typing.Optional[float]

        elevenlabs_style : typing.Optional[float]

        elevenlabs_speaker_boost : typing.Optional[bool]

        azure_voice_name : typing.Optional[str]

        openai_voice_name : typing.Optional[CopilotCompletionRequestOpenaiVoiceName]

        openai_tts_model : typing.Optional[CopilotCompletionRequestOpenaiTtsModel]

        input_face : typing.Optional[core.File]
            See core.File for more documentation

        face_padding_top : typing.Optional[int]

        face_padding_bottom : typing.Optional[int]

        face_padding_left : typing.Optional[int]

        face_padding_right : typing.Optional[int]

        sadtalker_settings : typing.Optional[CopilotCompletionRequestSadtalkerSettings]

        settings : typing.Optional[RunSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VideoBotsPageOutput
            Successful Response

        Examples
        --------
        import asyncio

        from gooey import AsyncGooey

        client = AsyncGooey(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.copilot.completion()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/video-bots/async",
            method="POST",
            params={
                "example_id": example_id,
            },
            data={
                "functions": functions,
                "variables": variables,
                "input_prompt": input_prompt,
                "input_audio": input_audio,
                "doc_extract_url": doc_extract_url,
                "messages": messages,
                "bot_script": bot_script,
                "selected_model": selected_model,
                "document_model": document_model,
                "task_instructions": task_instructions,
                "query_instructions": query_instructions,
                "keyword_instructions": keyword_instructions,
                "max_references": max_references,
                "max_context_words": max_context_words,
                "scroll_jump": scroll_jump,
                "embedding_model": embedding_model,
                "dense_weight": dense_weight,
                "citation_style": citation_style,
                "use_url_shortener": use_url_shortener,
                "asr_model": asr_model,
                "asr_language": asr_language,
                "translation_model": translation_model,
                "user_language": user_language,
                "lipsync_model": lipsync_model,
                "tools": tools,
                "avoid_repetition": avoid_repetition,
                "num_outputs": num_outputs,
                "quality": quality,
                "max_tokens": max_tokens,
                "sampling_temperature": sampling_temperature,
                "response_format_type": response_format_type,
                "tts_provider": tts_provider,
                "uberduck_voice_name": uberduck_voice_name,
                "uberduck_speaking_rate": uberduck_speaking_rate,
                "google_voice_name": google_voice_name,
                "google_speaking_rate": google_speaking_rate,
                "google_pitch": google_pitch,
                "bark_history_prompt": bark_history_prompt,
                "elevenlabs_voice_name": elevenlabs_voice_name,
                "elevenlabs_api_key": elevenlabs_api_key,
                "elevenlabs_voice_id": elevenlabs_voice_id,
                "elevenlabs_model": elevenlabs_model,
                "elevenlabs_stability": elevenlabs_stability,
                "elevenlabs_similarity_boost": elevenlabs_similarity_boost,
                "elevenlabs_style": elevenlabs_style,
                "elevenlabs_speaker_boost": elevenlabs_speaker_boost,
                "azure_voice_name": azure_voice_name,
                "openai_voice_name": openai_voice_name,
                "openai_tts_model": openai_tts_model,
                "face_padding_top": face_padding_top,
                "face_padding_bottom": face_padding_bottom,
                "face_padding_left": face_padding_left,
                "face_padding_right": face_padding_right,
                "sadtalker_settings": sadtalker_settings,
                "settings": settings,
            },
            files={
                "input_images": input_images,
                "input_documents": input_documents,
                "documents": documents,
                "input_glossary_document": input_glossary_document,
                "output_glossary_document": output_glossary_document,
                "input_face": input_face,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    VideoBotsPageOutput,
                    parse_obj_as(
                        type_=VideoBotsPageOutput,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(
                        GenericErrorResponse,
                        parse_obj_as(
                            type_=GenericErrorResponse,  # type: ignore
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