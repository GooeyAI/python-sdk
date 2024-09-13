# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .types.copilot_completion_request_functions_item import CopilotCompletionRequestFunctionsItem
from .. import core
from ..types.conversation_entry import ConversationEntry
from ..types.large_language_models import LargeLanguageModels
from ..types.embedding_models import EmbeddingModels
from ..types.citation_styles import CitationStyles
from ..types.asr_models import AsrModels
from ..types.translation_models import TranslationModels
from ..types.lipsync_models import LipsyncModels
from ..types.llm_tools import LlmTools
from ..types.response_format_type import ResponseFormatType
from ..types.text_to_speech_providers import TextToSpeechProviders
from ..types.open_ai_tts_voices import OpenAiTtsVoices
from ..types.open_ai_tts_models import OpenAiTtsModels
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
        functions: typing.Optional[typing.List[CopilotCompletionRequestFunctionsItem]] = None,
        variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        input_prompt: typing.Optional[str] = None,
        input_audio: typing.Optional[str] = None,
        input_images: typing.Optional[typing.List[core.File]] = None,
        input_documents: typing.Optional[typing.List[core.File]] = None,
        doc_extract_url: typing.Optional[str] = None,
        messages: typing.Optional[typing.List[ConversationEntry]] = None,
        bot_script: typing.Optional[str] = None,
        selected_model: typing.Optional[LargeLanguageModels] = None,
        document_model: typing.Optional[str] = None,
        task_instructions: typing.Optional[str] = None,
        query_instructions: typing.Optional[str] = None,
        keyword_instructions: typing.Optional[str] = None,
        documents: typing.Optional[typing.List[core.File]] = None,
        max_references: typing.Optional[int] = None,
        max_context_words: typing.Optional[int] = None,
        scroll_jump: typing.Optional[int] = None,
        embedding_model: typing.Optional[EmbeddingModels] = None,
        dense_weight: typing.Optional[float] = None,
        citation_style: typing.Optional[CitationStyles] = None,
        use_url_shortener: typing.Optional[bool] = None,
        asr_model: typing.Optional[AsrModels] = None,
        asr_language: typing.Optional[str] = None,
        translation_model: typing.Optional[TranslationModels] = None,
        user_language: typing.Optional[str] = None,
        input_glossary_document: typing.Optional[core.File] = None,
        output_glossary_document: typing.Optional[core.File] = None,
        lipsync_model: typing.Optional[LipsyncModels] = None,
        tools: typing.Optional[typing.List[LlmTools]] = None,
        avoid_repetition: typing.Optional[bool] = None,
        num_outputs: typing.Optional[int] = None,
        quality: typing.Optional[float] = None,
        max_tokens: typing.Optional[int] = None,
        sampling_temperature: typing.Optional[float] = None,
        response_format_type: typing.Optional[ResponseFormatType] = None,
        tts_provider: typing.Optional[TextToSpeechProviders] = None,
        uberduck_voice_name: typing.Optional[str] = None,
        uberduck_speaking_rate: typing.Optional[float] = None,
        google_voice_name: typing.Optional[str] = None,
        google_speaking_rate: typing.Optional[float] = None,
        google_pitch: typing.Optional[float] = None,
        bark_history_prompt: typing.Optional[str] = None,
        elevenlabs_voice_name: typing.Optional[str] = None,
        elevenlabs_api_key: typing.Optional[str] = None,
        elevenlabs_voice_id: typing.Optional[str] = None,
        elevenlabs_model: typing.Optional[str] = None,
        elevenlabs_stability: typing.Optional[float] = None,
        elevenlabs_similarity_boost: typing.Optional[float] = None,
        elevenlabs_style: typing.Optional[float] = None,
        elevenlabs_speaker_boost: typing.Optional[bool] = None,
        azure_voice_name: typing.Optional[str] = None,
        openai_voice_name: typing.Optional[OpenAiTtsVoices] = None,
        openai_tts_model: typing.Optional[OpenAiTtsModels] = None,
        input_face: typing.Optional[core.File] = None,
        face_padding_top: typing.Optional[int] = None,
        face_padding_bottom: typing.Optional[int] = None,
        face_padding_left: typing.Optional[int] = None,
        face_padding_right: typing.Optional[int] = None,
        sadtalker_settings: typing.Optional[CopilotCompletionRequestSadtalkerSettings] = None,
        settings: typing.Optional[RunSettings] = None,
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

        messages : typing.Optional[typing.List[ConversationEntry]]

        bot_script : typing.Optional[str]

        selected_model : typing.Optional[LargeLanguageModels]

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

        embedding_model : typing.Optional[EmbeddingModels]

        dense_weight : typing.Optional[float]

            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.


        citation_style : typing.Optional[CitationStyles]

        use_url_shortener : typing.Optional[bool]

        asr_model : typing.Optional[AsrModels]
            Choose a model to transcribe incoming audio messages to text.

        asr_language : typing.Optional[str]
            Choose a language to transcribe incoming audio messages to text.

        translation_model : typing.Optional[TranslationModels]

        user_language : typing.Optional[str]
            Choose a language to translate incoming text & audio messages to English and responses back to your selected language. Useful for low-resource languages.

        input_glossary_document : typing.Optional[core.File]
            See core.File for more documentation

        output_glossary_document : typing.Optional[core.File]
            See core.File for more documentation

        lipsync_model : typing.Optional[LipsyncModels]

        tools : typing.Optional[typing.List[LlmTools]]
            Give your copilot superpowers by giving it access to tools. Powered by [Function calling](https://platform.openai.com/docs/guides/function-calling).

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[ResponseFormatType]

        tts_provider : typing.Optional[TextToSpeechProviders]

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

        openai_voice_name : typing.Optional[OpenAiTtsVoices]

        openai_tts_model : typing.Optional[OpenAiTtsModels]

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
        functions: typing.Optional[typing.List[CopilotCompletionRequestFunctionsItem]] = None,
        variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        input_prompt: typing.Optional[str] = None,
        input_audio: typing.Optional[str] = None,
        input_images: typing.Optional[typing.List[core.File]] = None,
        input_documents: typing.Optional[typing.List[core.File]] = None,
        doc_extract_url: typing.Optional[str] = None,
        messages: typing.Optional[typing.List[ConversationEntry]] = None,
        bot_script: typing.Optional[str] = None,
        selected_model: typing.Optional[LargeLanguageModels] = None,
        document_model: typing.Optional[str] = None,
        task_instructions: typing.Optional[str] = None,
        query_instructions: typing.Optional[str] = None,
        keyword_instructions: typing.Optional[str] = None,
        documents: typing.Optional[typing.List[core.File]] = None,
        max_references: typing.Optional[int] = None,
        max_context_words: typing.Optional[int] = None,
        scroll_jump: typing.Optional[int] = None,
        embedding_model: typing.Optional[EmbeddingModels] = None,
        dense_weight: typing.Optional[float] = None,
        citation_style: typing.Optional[CitationStyles] = None,
        use_url_shortener: typing.Optional[bool] = None,
        asr_model: typing.Optional[AsrModels] = None,
        asr_language: typing.Optional[str] = None,
        translation_model: typing.Optional[TranslationModels] = None,
        user_language: typing.Optional[str] = None,
        input_glossary_document: typing.Optional[core.File] = None,
        output_glossary_document: typing.Optional[core.File] = None,
        lipsync_model: typing.Optional[LipsyncModels] = None,
        tools: typing.Optional[typing.List[LlmTools]] = None,
        avoid_repetition: typing.Optional[bool] = None,
        num_outputs: typing.Optional[int] = None,
        quality: typing.Optional[float] = None,
        max_tokens: typing.Optional[int] = None,
        sampling_temperature: typing.Optional[float] = None,
        response_format_type: typing.Optional[ResponseFormatType] = None,
        tts_provider: typing.Optional[TextToSpeechProviders] = None,
        uberduck_voice_name: typing.Optional[str] = None,
        uberduck_speaking_rate: typing.Optional[float] = None,
        google_voice_name: typing.Optional[str] = None,
        google_speaking_rate: typing.Optional[float] = None,
        google_pitch: typing.Optional[float] = None,
        bark_history_prompt: typing.Optional[str] = None,
        elevenlabs_voice_name: typing.Optional[str] = None,
        elevenlabs_api_key: typing.Optional[str] = None,
        elevenlabs_voice_id: typing.Optional[str] = None,
        elevenlabs_model: typing.Optional[str] = None,
        elevenlabs_stability: typing.Optional[float] = None,
        elevenlabs_similarity_boost: typing.Optional[float] = None,
        elevenlabs_style: typing.Optional[float] = None,
        elevenlabs_speaker_boost: typing.Optional[bool] = None,
        azure_voice_name: typing.Optional[str] = None,
        openai_voice_name: typing.Optional[OpenAiTtsVoices] = None,
        openai_tts_model: typing.Optional[OpenAiTtsModels] = None,
        input_face: typing.Optional[core.File] = None,
        face_padding_top: typing.Optional[int] = None,
        face_padding_bottom: typing.Optional[int] = None,
        face_padding_left: typing.Optional[int] = None,
        face_padding_right: typing.Optional[int] = None,
        sadtalker_settings: typing.Optional[CopilotCompletionRequestSadtalkerSettings] = None,
        settings: typing.Optional[RunSettings] = None,
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

        messages : typing.Optional[typing.List[ConversationEntry]]

        bot_script : typing.Optional[str]

        selected_model : typing.Optional[LargeLanguageModels]

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

        embedding_model : typing.Optional[EmbeddingModels]

        dense_weight : typing.Optional[float]

            Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
            Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.


        citation_style : typing.Optional[CitationStyles]

        use_url_shortener : typing.Optional[bool]

        asr_model : typing.Optional[AsrModels]
            Choose a model to transcribe incoming audio messages to text.

        asr_language : typing.Optional[str]
            Choose a language to transcribe incoming audio messages to text.

        translation_model : typing.Optional[TranslationModels]

        user_language : typing.Optional[str]
            Choose a language to translate incoming text & audio messages to English and responses back to your selected language. Useful for low-resource languages.

        input_glossary_document : typing.Optional[core.File]
            See core.File for more documentation

        output_glossary_document : typing.Optional[core.File]
            See core.File for more documentation

        lipsync_model : typing.Optional[LipsyncModels]

        tools : typing.Optional[typing.List[LlmTools]]
            Give your copilot superpowers by giving it access to tools. Powered by [Function calling](https://platform.openai.com/docs/guides/function-calling).

        avoid_repetition : typing.Optional[bool]

        num_outputs : typing.Optional[int]

        quality : typing.Optional[float]

        max_tokens : typing.Optional[int]

        sampling_temperature : typing.Optional[float]

        response_format_type : typing.Optional[ResponseFormatType]

        tts_provider : typing.Optional[TextToSpeechProviders]

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

        openai_voice_name : typing.Optional[OpenAiTtsVoices]

        openai_tts_model : typing.Optional[OpenAiTtsModels]

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
