# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .video_bots_page_request_functions_item import VideoBotsPageRequestFunctionsItem
import pydantic
from .video_bots_page_request_messages_item import VideoBotsPageRequestMessagesItem
from .video_bots_page_request_selected_model import VideoBotsPageRequestSelectedModel
from .video_bots_page_request_embedding_model import VideoBotsPageRequestEmbeddingModel
from .video_bots_page_request_citation_style import VideoBotsPageRequestCitationStyle
from .video_bots_page_request_asr_model import VideoBotsPageRequestAsrModel
from .video_bots_page_request_translation_model import VideoBotsPageRequestTranslationModel
from .video_bots_page_request_lipsync_model import VideoBotsPageRequestLipsyncModel
from .video_bots_page_request_response_format_type import VideoBotsPageRequestResponseFormatType
from .video_bots_page_request_tts_provider import VideoBotsPageRequestTtsProvider
from .video_bots_page_request_openai_voice_name import VideoBotsPageRequestOpenaiVoiceName
from .video_bots_page_request_openai_tts_model import VideoBotsPageRequestOpenaiTtsModel
from .video_bots_page_request_sadtalker_settings import VideoBotsPageRequestSadtalkerSettings
from .run_settings import RunSettings
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VideoBotsPageRequest(UniversalBaseModel):
    functions: typing.Optional[typing.List[VideoBotsPageRequestFunctionsItem]] = None
    variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Variables to be used as Jinja prompt templates and in functions as arguments
    """

    input_prompt: typing.Optional[str] = None
    input_audio: typing.Optional[str] = None
    input_images: typing.Optional[typing.List[str]] = None
    input_documents: typing.Optional[typing.List[str]] = None
    doc_extract_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Select a workflow to extract text from documents and images.
    """

    messages: typing.Optional[typing.List[VideoBotsPageRequestMessagesItem]] = None
    bot_script: typing.Optional[str] = None
    selected_model: typing.Optional[VideoBotsPageRequestSelectedModel] = None
    document_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    When your copilot users upload a photo or pdf, what kind of document are they mostly likely to upload? (via [Azure](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api?view=doc-intel-3.1.0&tabs=linux&pivots=programming-language-rest-api))
    """

    task_instructions: typing.Optional[str] = None
    query_instructions: typing.Optional[str] = None
    keyword_instructions: typing.Optional[str] = None
    documents: typing.Optional[typing.List[str]] = None
    max_references: typing.Optional[int] = None
    max_context_words: typing.Optional[int] = None
    scroll_jump: typing.Optional[int] = None
    embedding_model: typing.Optional[VideoBotsPageRequestEmbeddingModel] = None
    dense_weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
    Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    """

    citation_style: typing.Optional[VideoBotsPageRequestCitationStyle] = None
    use_url_shortener: typing.Optional[bool] = None
    asr_model: typing.Optional[VideoBotsPageRequestAsrModel] = pydantic.Field(default=None)
    """
    Choose a model to transcribe incoming audio messages to text.
    """

    asr_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Choose a language to transcribe incoming audio messages to text.
    """

    translation_model: typing.Optional[VideoBotsPageRequestTranslationModel] = None
    user_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Choose a language to translate incoming text & audio messages to English and responses back to your selected language. Useful for low-resource languages.
    """

    input_glossary_document: typing.Optional[str] = None
    output_glossary_document: typing.Optional[str] = None
    lipsync_model: typing.Optional[VideoBotsPageRequestLipsyncModel] = None
    tools: typing.Optional[typing.List[typing.Literal["json_to_pdf"]]] = pydantic.Field(default=None)
    """
    Give your copilot superpowers by giving it access to tools. Powered by [Function calling](https://platform.openai.com/docs/guides/function-calling).
    """

    avoid_repetition: typing.Optional[bool] = None
    num_outputs: typing.Optional[int] = None
    quality: typing.Optional[float] = None
    max_tokens: typing.Optional[int] = None
    sampling_temperature: typing.Optional[float] = None
    response_format_type: typing.Optional[VideoBotsPageRequestResponseFormatType] = None
    tts_provider: typing.Optional[VideoBotsPageRequestTtsProvider] = None
    uberduck_voice_name: typing.Optional[str] = None
    uberduck_speaking_rate: typing.Optional[float] = None
    google_voice_name: typing.Optional[str] = None
    google_speaking_rate: typing.Optional[float] = None
    google_pitch: typing.Optional[float] = None
    bark_history_prompt: typing.Optional[str] = None
    elevenlabs_voice_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Use `elevenlabs_voice_id` instead
    """

    elevenlabs_api_key: typing.Optional[str] = None
    elevenlabs_voice_id: typing.Optional[str] = None
    elevenlabs_model: typing.Optional[str] = None
    elevenlabs_stability: typing.Optional[float] = None
    elevenlabs_similarity_boost: typing.Optional[float] = None
    elevenlabs_style: typing.Optional[float] = None
    elevenlabs_speaker_boost: typing.Optional[bool] = None
    azure_voice_name: typing.Optional[str] = None
    openai_voice_name: typing.Optional[VideoBotsPageRequestOpenaiVoiceName] = None
    openai_tts_model: typing.Optional[VideoBotsPageRequestOpenaiTtsModel] = None
    input_face: typing.Optional[str] = None
    face_padding_top: typing.Optional[int] = None
    face_padding_bottom: typing.Optional[int] = None
    face_padding_left: typing.Optional[int] = None
    face_padding_right: typing.Optional[int] = None
    sadtalker_settings: typing.Optional[VideoBotsPageRequestSadtalkerSettings] = None
    settings: typing.Optional[RunSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow