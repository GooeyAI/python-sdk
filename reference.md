# Reference
## CopilotIntegrations
<details><summary><code>client.copilot_integrations.<a href="src/gooey/copilot_integrations/client.py">video_bots_stream_create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.copilot_integrations.video_bots_stream_create(
    integration_id="integration_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**integration_id:** `str` — Your Integration ID as shown in the Copilot Integrations tab
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` 

The gooey conversation ID.

If not provided, a new conversation will be started and a new ID will be returned in the response. Use this to maintain the state of the conversation between requests.

Note that you may not provide a custom ID here, and must only use the `conversation_id` returned in a previous response.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 

Your app's custom user ID.

If not provided, a random user will be created and a new ID will be returned in the response. If a `conversation_id` is provided, this field is automatically set to the user's id associated with that conversation.
    
</dd>
</dl>

<dl>
<dd>

**user_message_id:** `typing.Optional[str]` 

Your app's custom message ID for the user message.

If not provided, a random ID will be generated and returned in the response. This is useful for tracking messages in the conversation.
    
</dd>
</dl>

<dl>
<dd>

**button_pressed:** `typing.Optional[ButtonPressed]` — The button that was pressed by the user.
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**input_audio:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**input_images:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**input_documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**doc_extract_url:** `typing.Optional[str]` — Select a workflow to extract text from documents and images.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.Sequence[ConversationEntry]]` 
    
</dd>
</dl>

<dl>
<dd>

**bot_script:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[CreateStreamRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**document_model:** `typing.Optional[str]` — When your copilot users upload a photo or pdf, what kind of document are they mostly likely to upload? (via [Azure](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api?view=doc-intel-3.1.0&tabs=linux&pivots=programming-language-rest-api))
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**keyword_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[CreateStreamRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 


Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
        
    
</dd>
</dl>

<dl>
<dd>

**citation_style:** `typing.Optional[CreateStreamRequestCitationStyle]` 
    
</dd>
</dl>

<dl>
<dd>

**use_url_shortener:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**asr_model:** `typing.Optional[CreateStreamRequestAsrModel]` — Choose a model to transcribe incoming audio messages to text.
    
</dd>
</dl>

<dl>
<dd>

**asr_language:** `typing.Optional[str]` — Choose a language to transcribe incoming audio messages to text.
    
</dd>
</dl>

<dl>
<dd>

**translation_model:** `typing.Optional[CreateStreamRequestTranslationModel]` 
    
</dd>
</dl>

<dl>
<dd>

**user_language:** `typing.Optional[str]` — Choose a language to translate incoming text & audio messages to English and responses back to your selected language. Useful for low-resource languages.
    
</dd>
</dl>

<dl>
<dd>

**input_glossary_document:** `typing.Optional[str]` 


Translation Glossary for User Langauge -> LLM Language (English)
            
    
</dd>
</dl>

<dl>
<dd>

**output_glossary_document:** `typing.Optional[str]` 


Translation Glossary for LLM Language (English) -> User Langauge
            
    
</dd>
</dl>

<dl>
<dd>

**lipsync_model:** `typing.Optional[CreateStreamRequestLipsyncModel]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.Sequence[LlmTools]]` — Give your copilot superpowers by giving it access to tools. Powered by [Function calling](https://platform.openai.com/docs/guides/function-calling).
    
</dd>
</dl>

<dl>
<dd>

**tts_provider:** `typing.Optional[CreateStreamRequestTtsProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**google_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_pitch:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bark_history_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_name:** `typing.Optional[str]` — Use `elevenlabs_voice_id` instead
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_stability:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_similarity_boost:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_style:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_speaker_boost:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**azure_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_voice_name:** `typing.Optional[CreateStreamRequestOpenaiVoiceName]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_tts_model:** `typing.Optional[CreateStreamRequestOpenaiTtsModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_top:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_bottom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_left:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_right:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sadtalker_settings:** `typing.Optional[SadTalkerSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**input_text:** `typing.Optional[str]` — Use `input_prompt` instead
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilot_integrations.<a href="src/gooey/copilot_integrations/client.py">video_bots_stream</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.copilot_integrations.video_bots_stream(
    request_id="request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CopilotForYourEnterprise
<details><summary><code>client.copilot_for_your_enterprise.<a href="src/gooey/copilot_for_your_enterprise/client.py">video_bots</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.copilot_for_your_enterprise.video_bots()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**input_audio:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**input_images:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**input_documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**doc_extract_url:** `typing.Optional[str]` — Select a workflow to extract text from documents and images.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.Sequence[ConversationEntry]]` 
    
</dd>
</dl>

<dl>
<dd>

**bot_script:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[VideoBotsPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**document_model:** `typing.Optional[str]` — When your copilot users upload a photo or pdf, what kind of document are they mostly likely to upload? (via [Azure](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api?view=doc-intel-3.1.0&tabs=linux&pivots=programming-language-rest-api))
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**keyword_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[VideoBotsPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**citation_style:** `typing.Optional[VideoBotsPageRequestCitationStyle]` 
    
</dd>
</dl>

<dl>
<dd>

**use_url_shortener:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**asr_model:** `typing.Optional[VideoBotsPageRequestAsrModel]` — Choose a model to transcribe incoming audio messages to text.
    
</dd>
</dl>

<dl>
<dd>

**asr_language:** `typing.Optional[str]` — Choose a language to transcribe incoming audio messages to text.
    
</dd>
</dl>

<dl>
<dd>

**translation_model:** `typing.Optional[VideoBotsPageRequestTranslationModel]` 
    
</dd>
</dl>

<dl>
<dd>

**user_language:** `typing.Optional[str]` — Choose a language to translate incoming text & audio messages to English and responses back to your selected language. Useful for low-resource languages.
    
</dd>
</dl>

<dl>
<dd>

**input_glossary_document:** `typing.Optional[str]` — Translation Glossary for User Langauge -> LLM Language (English)
    
</dd>
</dl>

<dl>
<dd>

**output_glossary_document:** `typing.Optional[str]` — Translation Glossary for LLM Language (English) -> User Langauge
    
</dd>
</dl>

<dl>
<dd>

**lipsync_model:** `typing.Optional[VideoBotsPageRequestLipsyncModel]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.Sequence[LlmTools]]` — Give your copilot superpowers by giving it access to tools. Powered by [Function calling](https://platform.openai.com/docs/guides/function-calling).
    
</dd>
</dl>

<dl>
<dd>

**tts_provider:** `typing.Optional[VideoBotsPageRequestTtsProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**google_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_pitch:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bark_history_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_name:** `typing.Optional[str]` — Use `elevenlabs_voice_id` instead
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_stability:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_similarity_boost:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_style:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_speaker_boost:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**azure_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_voice_name:** `typing.Optional[VideoBotsPageRequestOpenaiVoiceName]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_tts_model:** `typing.Optional[VideoBotsPageRequestOpenaiTtsModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_top:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_bottom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_left:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_right:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sadtalker_settings:** `typing.Optional[SadTalkerSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilot_for_your_enterprise.<a href="src/gooey/copilot_for_your_enterprise/client.py">async_video_bots</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.copilot_for_your_enterprise.async_video_bots()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**input_audio:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**input_images:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**input_documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**doc_extract_url:** `typing.Optional[str]` — Select a workflow to extract text from documents and images.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.Sequence[ConversationEntry]]` 
    
</dd>
</dl>

<dl>
<dd>

**bot_script:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[VideoBotsPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**document_model:** `typing.Optional[str]` — When your copilot users upload a photo or pdf, what kind of document are they mostly likely to upload? (via [Azure](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api?view=doc-intel-3.1.0&tabs=linux&pivots=programming-language-rest-api))
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**keyword_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[VideoBotsPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**citation_style:** `typing.Optional[VideoBotsPageRequestCitationStyle]` 
    
</dd>
</dl>

<dl>
<dd>

**use_url_shortener:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**asr_model:** `typing.Optional[VideoBotsPageRequestAsrModel]` — Choose a model to transcribe incoming audio messages to text.
    
</dd>
</dl>

<dl>
<dd>

**asr_language:** `typing.Optional[str]` — Choose a language to transcribe incoming audio messages to text.
    
</dd>
</dl>

<dl>
<dd>

**translation_model:** `typing.Optional[VideoBotsPageRequestTranslationModel]` 
    
</dd>
</dl>

<dl>
<dd>

**user_language:** `typing.Optional[str]` — Choose a language to translate incoming text & audio messages to English and responses back to your selected language. Useful for low-resource languages.
    
</dd>
</dl>

<dl>
<dd>

**input_glossary_document:** `typing.Optional[str]` — Translation Glossary for User Langauge -> LLM Language (English)
    
</dd>
</dl>

<dl>
<dd>

**output_glossary_document:** `typing.Optional[str]` — Translation Glossary for LLM Language (English) -> User Langauge
    
</dd>
</dl>

<dl>
<dd>

**lipsync_model:** `typing.Optional[VideoBotsPageRequestLipsyncModel]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.Sequence[LlmTools]]` — Give your copilot superpowers by giving it access to tools. Powered by [Function calling](https://platform.openai.com/docs/guides/function-calling).
    
</dd>
</dl>

<dl>
<dd>

**tts_provider:** `typing.Optional[VideoBotsPageRequestTtsProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**google_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_pitch:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bark_history_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_name:** `typing.Optional[str]` — Use `elevenlabs_voice_id` instead
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_stability:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_similarity_boost:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_style:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_speaker_boost:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**azure_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_voice_name:** `typing.Optional[VideoBotsPageRequestOpenaiVoiceName]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_tts_model:** `typing.Optional[VideoBotsPageRequestOpenaiTtsModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_top:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_bottom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_left:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_right:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sadtalker_settings:** `typing.Optional[SadTalkerSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilot_for_your_enterprise.<a href="src/gooey/copilot_for_your_enterprise/client.py">status_video_bots</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.copilot_for_your_enterprise.status_video_bots(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AiAnimationGenerator
<details><summary><code>client.ai_animation_generator.<a href="src/gooey/ai_animation_generator/client.py">deforum_sd</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import AnimationPrompt, Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_animation_generator.deforum_sd(
    animation_prompts=[
        AnimationPrompt(
            frame="frame",
            prompt="prompt",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**animation_prompts:** `typing.Sequence[AnimationPrompt]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**max_frames:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[DeforumSdPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**animation_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**zoom:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_x:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_y:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rotation3d_x:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rotation3d_y:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rotation3d_z:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fps:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_animation_generator.<a href="src/gooey/ai_animation_generator/client.py">async_deforum_sd</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import AnimationPrompt, Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_animation_generator.async_deforum_sd(
    animation_prompts=[
        AnimationPrompt(
            frame="frame",
            prompt="prompt",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**animation_prompts:** `typing.Sequence[AnimationPrompt]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**max_frames:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[DeforumSdPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**animation_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**zoom:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_x:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_y:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rotation3d_x:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rotation3d_y:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rotation3d_z:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fps:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_animation_generator.<a href="src/gooey/ai_animation_generator/client.py">status_deforum_sd</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_animation_generator.status_deforum_sd(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AiArtQrCode
<details><summary><code>client.ai_art_qr_code.<a href="src/gooey/ai_art_qr_code/client.py">art_qr_code</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_art_qr_code.art_qr_code(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**qr_code_data:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**qr_code_input_image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**qr_code_vcard:** `typing.Optional[Vcard]` 
    
</dd>
</dl>

<dl>
<dd>

**qr_code_file:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**use_url_shortener:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_controlnet_models:** `typing.Optional[
    typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]
]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_strength:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[QrCodeGeneratorPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_controlnet_model:** `typing.Optional[
    typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]
]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**controlnet_conditioning_scale:** `typing.Optional[typing.Sequence[float]]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scheduler:** `typing.Optional[Scheduler]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_art_qr_code.<a href="src/gooey/ai_art_qr_code/client.py">async_art_qr_code</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_art_qr_code.async_art_qr_code(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**qr_code_data:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**qr_code_input_image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**qr_code_vcard:** `typing.Optional[Vcard]` 
    
</dd>
</dl>

<dl>
<dd>

**qr_code_file:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**use_url_shortener:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_controlnet_models:** `typing.Optional[
    typing.Sequence[QrCodeGeneratorPageRequestImagePromptControlnetModelsItem]
]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_strength:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**image_prompt_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[QrCodeGeneratorPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_controlnet_model:** `typing.Optional[
    typing.Sequence[QrCodeGeneratorPageRequestSelectedControlnetModelItem]
]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**controlnet_conditioning_scale:** `typing.Optional[typing.Sequence[float]]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scheduler:** `typing.Optional[Scheduler]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_art_qr_code.<a href="src/gooey/ai_art_qr_code/client.py">status_art_qr_code</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_art_qr_code.status_art_qr_code(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GeneratePeopleAlsoAskSeoContent
<details><summary><code>client.generate_people_also_ask_seo_content.<a href="src/gooey/generate_people_also_ask_seo_content/client.py">related_qna_maker</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.generate_people_also_ask_seo_content.related_qna_maker(
    search_query="search_query",
    site_filter="site_filter",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**site_filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**serp_search_type:** `typing.Optional[SerpSearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_search_field:** `typing.Optional[str]` — DEPRECATED: use `serp_search_type` instead
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[RelatedQnAPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_search_urls:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[RelatedQnAPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.generate_people_also_ask_seo_content.<a href="src/gooey/generate_people_also_ask_seo_content/client.py">async_related_qna_maker</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.generate_people_also_ask_seo_content.async_related_qna_maker(
    search_query="search_query",
    site_filter="site_filter",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**site_filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**serp_search_type:** `typing.Optional[SerpSearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_search_field:** `typing.Optional[str]` — DEPRECATED: use `serp_search_type` instead
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[RelatedQnAPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_search_urls:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[RelatedQnAPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.generate_people_also_ask_seo_content.<a href="src/gooey/generate_people_also_ask_seo_content/client.py">status_related_qna_maker</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.generate_people_also_ask_seo_content.status_related_qna_maker(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CreateAPerfectSeoOptimizedTitleParagraph
<details><summary><code>client.create_a_perfect_seo_optimized_title_paragraph.<a href="src/gooey/create_a_perfect_seo_optimized_title_paragraph/client.py">seo_summary</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.create_a_perfect_seo_optimized_title_paragraph.seo_summary(
    search_query="search_query",
    keywords="keywords",
    title="title",
    company_url="company_url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**company_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**serp_search_type:** `typing.Optional[SerpSearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_search_field:** `typing.Optional[str]` — DEPRECATED: use `serp_search_type` instead
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enable_html:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[SeoSummaryPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**max_search_urls:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**enable_crosslinks:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.create_a_perfect_seo_optimized_title_paragraph.<a href="src/gooey/create_a_perfect_seo_optimized_title_paragraph/client.py">async_seo_summary</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.create_a_perfect_seo_optimized_title_paragraph.async_seo_summary(
    search_query="search_query",
    keywords="keywords",
    title="title",
    company_url="company_url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**company_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**serp_search_type:** `typing.Optional[SerpSearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_search_field:** `typing.Optional[str]` — DEPRECATED: use `serp_search_type` instead
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enable_html:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[SeoSummaryPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**max_search_urls:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**enable_crosslinks:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.create_a_perfect_seo_optimized_title_paragraph.<a href="src/gooey/create_a_perfect_seo_optimized_title_paragraph/client.py">status_seo_summary</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.create_a_perfect_seo_optimized_title_paragraph.status_seo_summary(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WebSearchGpt3
<details><summary><code>client.web_search_gpt3.<a href="src/gooey/web_search_gpt3/client.py">google_gpt</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.web_search_gpt3.google_gpt(
    search_query="search_query",
    site_filter="site_filter",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**site_filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**serp_search_type:** `typing.Optional[SerpSearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_search_field:** `typing.Optional[str]` — DEPRECATED: use `serp_search_type` instead
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[GoogleGptPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_search_urls:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[GoogleGptPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_search_gpt3.<a href="src/gooey/web_search_gpt3/client.py">async_google_gpt</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.web_search_gpt3.async_google_gpt(
    search_query="search_query",
    site_filter="site_filter",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**site_filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**serp_search_type:** `typing.Optional[SerpSearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_search_field:** `typing.Optional[str]` — DEPRECATED: use `serp_search_type` instead
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[GoogleGptPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_search_urls:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[GoogleGptPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_search_gpt3.<a href="src/gooey/web_search_gpt3/client.py">status_google_gpt</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.web_search_gpt3.status_google_gpt(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProfileLookupGpt3ForAiPersonalizedEmails
<details><summary><code>client.profile_lookup_gpt3for_ai_personalized_emails.<a href="src/gooey/profile_lookup_gpt3for_ai_personalized_emails/client.py">social_lookup_email</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.profile_lookup_gpt3for_ai_personalized_emails.social_lookup_email(
    email_address="email_address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email_address:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[SocialLookupEmailPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profile_lookup_gpt3for_ai_personalized_emails.<a href="src/gooey/profile_lookup_gpt3for_ai_personalized_emails/client.py">async_social_lookup_email</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.profile_lookup_gpt3for_ai_personalized_emails.async_social_lookup_email(
    email_address="email_address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email_address:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[SocialLookupEmailPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profile_lookup_gpt3for_ai_personalized_emails.<a href="src/gooey/profile_lookup_gpt3for_ai_personalized_emails/client.py">status_social_lookup_email</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.profile_lookup_gpt3for_ai_personalized_emails.status_social_lookup_email(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BulkRunner
<details><summary><code>client.bulk_runner.<a href="src/gooey/bulk_runner/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.bulk_runner.post(
    documents=["documents"],
    run_urls=["run_urls"],
    input_columns={"key": "value"},
    output_columns={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 

Upload or link to a CSV or google sheet that contains your sample input data.
For example, for Copilot, this would sample questions or for Art QR Code, would would be pairs of image descriptions and URLs.
Remember to includes header names in your CSV too.
    
</dd>
</dl>

<dl>
<dd>

**run_urls:** `typing.Sequence[str]` 

Provide one or more Gooey.AI workflow runs.
You can add multiple runs from the same recipe (e.g. two versions of your copilot) and we'll run the inputs over both of them.
    
</dd>
</dl>

<dl>
<dd>

**input_columns:** `typing.Dict[str, str]` — For each input field in the Gooey.AI workflow, specify the column in your input data that corresponds to it.
    
</dd>
</dl>

<dl>
<dd>

**output_columns:** `typing.Dict[str, str]` — For each output field in the Gooey.AI workflow, specify the column name that you'd like to use for it in the output data.
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**eval_urls:** `typing.Optional[typing.Sequence[str]]` — _(optional)_ Add one or more Gooey.AI Evaluator Workflows to evaluate the results of your runs.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_runner.<a href="src/gooey/bulk_runner/client.py">async_bulk_runner</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.bulk_runner.async_bulk_runner(
    documents=["documents"],
    run_urls=["run_urls"],
    input_columns={"key": "value"},
    output_columns={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 

Upload or link to a CSV or google sheet that contains your sample input data.
For example, for Copilot, this would sample questions or for Art QR Code, would would be pairs of image descriptions and URLs.
Remember to includes header names in your CSV too.
    
</dd>
</dl>

<dl>
<dd>

**run_urls:** `typing.Sequence[str]` 

Provide one or more Gooey.AI workflow runs.
You can add multiple runs from the same recipe (e.g. two versions of your copilot) and we'll run the inputs over both of them.
    
</dd>
</dl>

<dl>
<dd>

**input_columns:** `typing.Dict[str, str]` — For each input field in the Gooey.AI workflow, specify the column in your input data that corresponds to it.
    
</dd>
</dl>

<dl>
<dd>

**output_columns:** `typing.Dict[str, str]` — For each output field in the Gooey.AI workflow, specify the column name that you'd like to use for it in the output data.
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**eval_urls:** `typing.Optional[typing.Sequence[str]]` — _(optional)_ Add one or more Gooey.AI Evaluator Workflows to evaluate the results of your runs.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_runner.<a href="src/gooey/bulk_runner/client.py">status_bulk_runner</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.bulk_runner.status_bulk_runner(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Evaluator
<details><summary><code>client.evaluator.<a href="src/gooey/evaluator/client.py">bulk_eval</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.evaluator.bulk_eval(
    documents=["documents"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 

Upload or link to a CSV or google sheet that contains your sample input data.
For example, for Copilot, this would sample questions or for Art QR Code, would would be pairs of image descriptions and URLs.
Remember to includes header names in your CSV too.
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[BulkEvalPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**eval_prompts:** `typing.Optional[typing.Sequence[EvalPrompt]]` 

Specify custom LLM prompts to calculate metrics that evaluate each row of the input data. The output should be a JSON object mapping the metric names to values.  
_The `columns` dictionary can be used to reference the spreadsheet columns._  

    
</dd>
</dl>

<dl>
<dd>

**agg_functions:** `typing.Optional[typing.Sequence[AggFunction]]` — Aggregate using one or more operations. Uses [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html#dataframegroupby-computations-descriptive-stats).
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluator.<a href="src/gooey/evaluator/client.py">async_bulk_eval</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.evaluator.async_bulk_eval(
    documents=["documents"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 

Upload or link to a CSV or google sheet that contains your sample input data.
For example, for Copilot, this would sample questions or for Art QR Code, would would be pairs of image descriptions and URLs.
Remember to includes header names in your CSV too.
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[BulkEvalPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**eval_prompts:** `typing.Optional[typing.Sequence[EvalPrompt]]` 

Specify custom LLM prompts to calculate metrics that evaluate each row of the input data. The output should be a JSON object mapping the metric names to values.  
_The `columns` dictionary can be used to reference the spreadsheet columns._  

    
</dd>
</dl>

<dl>
<dd>

**agg_functions:** `typing.Optional[typing.Sequence[AggFunction]]` — Aggregate using one or more operations. Uses [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html#dataframegroupby-computations-descriptive-stats).
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluator.<a href="src/gooey/evaluator/client.py">status_bulk_eval</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.evaluator.status_bulk_eval(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SyntheticDataMakerForVideosPdFs
<details><summary><code>client.synthetic_data_maker_for_videos_pd_fs.<a href="src/gooey/synthetic_data_maker_for_videos_pd_fs/client.py">doc_extract</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.synthetic_data_maker_for_videos_pd_fs.doc_extract(
    documents=["documents"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**sheet_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_asr_model:** `typing.Optional[DocExtractPageRequestSelectedAsrModel]` 
    
</dd>
</dl>

<dl>
<dd>

**google_translate_target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**glossary_document:** `typing.Optional[str]` 

Provide a glossary to customize translation and improve accuracy of domain-specific terms.
If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[DocExtractPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.synthetic_data_maker_for_videos_pd_fs.<a href="src/gooey/synthetic_data_maker_for_videos_pd_fs/client.py">async_doc_extract</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.synthetic_data_maker_for_videos_pd_fs.async_doc_extract(
    documents=["documents"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**sheet_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_asr_model:** `typing.Optional[DocExtractPageRequestSelectedAsrModel]` 
    
</dd>
</dl>

<dl>
<dd>

**google_translate_target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**glossary_document:** `typing.Optional[str]` 

Provide a glossary to customize translation and improve accuracy of domain-specific terms.
If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[DocExtractPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.synthetic_data_maker_for_videos_pd_fs.<a href="src/gooey/synthetic_data_maker_for_videos_pd_fs/client.py">status_doc_extract</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.synthetic_data_maker_for_videos_pd_fs.status_doc_extract(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LargeLanguageModelsGpt3
<details><summary><code>client.large_language_models_gpt3.<a href="src/gooey/large_language_models_gpt3/client.py">compare_llm</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.large_language_models_gpt3.compare_llm()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_models:** `typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**response_format_type:** `typing.Optional[CompareLlmPageRequestResponseFormatType]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.large_language_models_gpt3.<a href="src/gooey/large_language_models_gpt3/client.py">async_compare_llm</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.large_language_models_gpt3.async_compare_llm()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_models:** `typing.Optional[typing.Sequence[CompareLlmPageRequestSelectedModelsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**response_format_type:** `typing.Optional[CompareLlmPageRequestResponseFormatType]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.large_language_models_gpt3.<a href="src/gooey/large_language_models_gpt3/client.py">status_compare_llm</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.large_language_models_gpt3.status_compare_llm(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SearchYourDocsWithGpt
<details><summary><code>client.search_your_docs_with_gpt.<a href="src/gooey/search_your_docs_with_gpt/client.py">doc_search</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.search_your_docs_with_gpt.doc_search(
    search_query="search_query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**keyword_query:** `typing.Optional[DocSearchPageRequestKeywordQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**doc_extract_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[DocSearchPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[DocSearchPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**citation_style:** `typing.Optional[DocSearchPageRequestCitationStyle]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.search_your_docs_with_gpt.<a href="src/gooey/search_your_docs_with_gpt/client.py">async_doc_search</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.search_your_docs_with_gpt.async_doc_search(
    search_query="search_query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**keyword_query:** `typing.Optional[DocSearchPageRequestKeywordQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**doc_extract_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[DocSearchPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[DocSearchPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**citation_style:** `typing.Optional[DocSearchPageRequestCitationStyle]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.search_your_docs_with_gpt.<a href="src/gooey/search_your_docs_with_gpt/client.py">status_doc_search</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.search_your_docs_with_gpt.status_doc_search(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SmartGpt
<details><summary><code>client.smart_gpt.<a href="src/gooey/smart_gpt/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.smart_gpt.post(
    input_prompt="input_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**cot_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**reflexion_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**dera_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[SmartGptPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.smart_gpt.<a href="src/gooey/smart_gpt/client.py">async_smart_gpt</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.smart_gpt.async_smart_gpt(
    input_prompt="input_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**cot_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**reflexion_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**dera_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[SmartGptPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.smart_gpt.<a href="src/gooey/smart_gpt/client.py">status_smart_gpt</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.smart_gpt.status_smart_gpt(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SummarizeYourDocsWithGpt
<details><summary><code>client.summarize_your_docs_with_gpt.<a href="src/gooey/summarize_your_docs_with_gpt/client.py">doc_summary</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.summarize_your_docs_with_gpt.doc_summary(
    documents=["documents"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**merge_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[DocSummaryPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**chain_type:** `typing.Optional[typing.Literal["map_reduce"]]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_asr_model:** `typing.Optional[DocSummaryPageRequestSelectedAsrModel]` 
    
</dd>
</dl>

<dl>
<dd>

**google_translate_target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.summarize_your_docs_with_gpt.<a href="src/gooey/summarize_your_docs_with_gpt/client.py">async_doc_summary</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.summarize_your_docs_with_gpt.async_doc_summary(
    documents=["documents"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**merge_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[DocSummaryPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**chain_type:** `typing.Optional[typing.Literal["map_reduce"]]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_asr_model:** `typing.Optional[DocSummaryPageRequestSelectedAsrModel]` 
    
</dd>
</dl>

<dl>
<dd>

**google_translate_target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.summarize_your_docs_with_gpt.<a href="src/gooey/summarize_your_docs_with_gpt/client.py">status_doc_summary</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.summarize_your_docs_with_gpt.status_doc_summary(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Functions
<details><summary><code>client.functions.<a href="src/gooey/functions/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.functions.post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `typing.Optional[str]` — The JS code to be executed.
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used in the code
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/gooey/functions/client.py">async_functions</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.functions.async_functions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `typing.Optional[str]` — The JS code to be executed.
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used in the code
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/gooey/functions/client.py">status_functions</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.functions.status_functions(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LipSyncing
<details><summary><code>client.lip_syncing.<a href="src/gooey/lip_syncing/client.py">lipsync</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.lip_syncing.lipsync()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_top:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_bottom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_left:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_right:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sadtalker_settings:** `typing.Optional[SadTalkerSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[LipsyncPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_audio:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lip_syncing.<a href="src/gooey/lip_syncing/client.py">async_lipsync</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.lip_syncing.async_lipsync()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_top:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_bottom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_left:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_right:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sadtalker_settings:** `typing.Optional[SadTalkerSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[LipsyncPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_audio:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lip_syncing.<a href="src/gooey/lip_syncing/client.py">status_lipsync</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.lip_syncing.status_lipsync(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LipsyncVideoWithAnyText
<details><summary><code>client.lipsync_video_with_any_text.<a href="src/gooey/lipsync_video_with_any_text/client.py">lipsync_tts</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.lipsync_video_with_any_text.lipsync_tts(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**tts_provider:** `typing.Optional[LipsyncTtsPageRequestTtsProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**google_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_pitch:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bark_history_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_name:** `typing.Optional[str]` — Use `elevenlabs_voice_id` instead
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_stability:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_similarity_boost:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_style:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_speaker_boost:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**azure_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_voice_name:** `typing.Optional[LipsyncTtsPageRequestOpenaiVoiceName]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_tts_model:** `typing.Optional[LipsyncTtsPageRequestOpenaiTtsModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_top:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_bottom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_left:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_right:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sadtalker_settings:** `typing.Optional[SadTalkerSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[LipsyncTtsPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lipsync_video_with_any_text.<a href="src/gooey/lipsync_video_with_any_text/client.py">async_lipsync_tts</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.lipsync_video_with_any_text.async_lipsync_tts(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**tts_provider:** `typing.Optional[LipsyncTtsPageRequestTtsProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**google_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_pitch:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bark_history_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_name:** `typing.Optional[str]` — Use `elevenlabs_voice_id` instead
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_stability:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_similarity_boost:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_style:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_speaker_boost:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**azure_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_voice_name:** `typing.Optional[LipsyncTtsPageRequestOpenaiVoiceName]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_tts_model:** `typing.Optional[LipsyncTtsPageRequestOpenaiTtsModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_top:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_bottom:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_left:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**face_padding_right:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sadtalker_settings:** `typing.Optional[SadTalkerSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[LipsyncTtsPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lipsync_video_with_any_text.<a href="src/gooey/lipsync_video_with_any_text/client.py">status_lipsync_tts</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.lipsync_video_with_any_text.status_lipsync_tts(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CompareAiVoiceGenerators
<details><summary><code>client.compare_ai_voice_generators.<a href="src/gooey/compare_ai_voice_generators/client.py">text_to_speech</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_voice_generators.text_to_speech(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**tts_provider:** `typing.Optional[TextToSpeechPageRequestTtsProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**google_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_pitch:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bark_history_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_name:** `typing.Optional[str]` — Use `elevenlabs_voice_id` instead
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_stability:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_similarity_boost:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_style:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_speaker_boost:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**azure_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_voice_name:** `typing.Optional[TextToSpeechPageRequestOpenaiVoiceName]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_tts_model:** `typing.Optional[TextToSpeechPageRequestOpenaiTtsModel]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compare_ai_voice_generators.<a href="src/gooey/compare_ai_voice_generators/client.py">async_text_to_speech</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_voice_generators.async_text_to_speech(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**tts_provider:** `typing.Optional[TextToSpeechPageRequestTtsProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**uberduck_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**google_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**google_pitch:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bark_history_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_name:** `typing.Optional[str]` — Use `elevenlabs_voice_id` instead
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_voice_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_stability:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_similarity_boost:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_style:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**elevenlabs_speaker_boost:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**azure_voice_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_voice_name:** `typing.Optional[TextToSpeechPageRequestOpenaiVoiceName]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_tts_model:** `typing.Optional[TextToSpeechPageRequestOpenaiTtsModel]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compare_ai_voice_generators.<a href="src/gooey/compare_ai_voice_generators/client.py">status_text_to_speech</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_voice_generators.status_text_to_speech(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SpeechRecognitionTranslation
<details><summary><code>client.speech_recognition_translation.<a href="src/gooey/speech_recognition_translation/client.py">asr</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.speech_recognition_translation.asr(
    documents=["documents"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[AsrPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_model:** `typing.Optional[AsrPageRequestTranslationModel]` 
    
</dd>
</dl>

<dl>
<dd>

**output_format:** `typing.Optional[AsrPageRequestOutputFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**google_translate_target:** `typing.Optional[str]` — use `translation_model` & `translation_target` instead.
    
</dd>
</dl>

<dl>
<dd>

**translation_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**glossary_document:** `typing.Optional[str]` 

Provide a glossary to customize translation and improve accuracy of domain-specific terms.
If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.speech_recognition_translation.<a href="src/gooey/speech_recognition_translation/client.py">async_asr</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.speech_recognition_translation.async_asr(
    documents=["documents"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**documents:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[AsrPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_model:** `typing.Optional[AsrPageRequestTranslationModel]` 
    
</dd>
</dl>

<dl>
<dd>

**output_format:** `typing.Optional[AsrPageRequestOutputFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**google_translate_target:** `typing.Optional[str]` — use `translation_model` & `translation_target` instead.
    
</dd>
</dl>

<dl>
<dd>

**translation_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**glossary_document:** `typing.Optional[str]` 

Provide a glossary to customize translation and improve accuracy of domain-specific terms.
If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.speech_recognition_translation.<a href="src/gooey/speech_recognition_translation/client.py">status_asr</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.speech_recognition_translation.status_asr(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TextGuidedAudioGenerator
<details><summary><code>client.text_guided_audio_generator.<a href="src/gooey/text_guided_audio_generator/client.py">text2audio</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.text_guided_audio_generator.text2audio(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**duration_sec:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sd2upscaling:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_models:** `typing.Optional[typing.Sequence[typing.Literal["audio_ldm"]]]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.text_guided_audio_generator.<a href="src/gooey/text_guided_audio_generator/client.py">async_text2audio</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.text_guided_audio_generator.async_text2audio(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**duration_sec:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sd2upscaling:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_models:** `typing.Optional[typing.Sequence[typing.Literal["audio_ldm"]]]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.text_guided_audio_generator.<a href="src/gooey/text_guided_audio_generator/client.py">status_text2audio</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.text_guided_audio_generator.status_text2audio(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CompareAiTranslations
<details><summary><code>client.compare_ai_translations.<a href="src/gooey/compare_ai_translations/client.py">translate</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_translations.translate()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**texts:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[TranslationPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**glossary_document:** `typing.Optional[str]` 

Provide a glossary to customize translation and improve accuracy of domain-specific terms.
If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compare_ai_translations.<a href="src/gooey/compare_ai_translations/client.py">async_translate</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_translations.async_translate()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**texts:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[TranslationPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**glossary_document:** `typing.Optional[str]` 

Provide a glossary to customize translation and improve accuracy of domain-specific terms.
If not specified or invalid, no glossary will be used. Read about the expected format [here](https://docs.google.com/document/d/1TwzAvFmFYekloRKql2PXNPIyqCbsHRL8ZtnWkzAYrh8/edit?usp=sharing).
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compare_ai_translations.<a href="src/gooey/compare_ai_translations/client.py">status_translate</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_translations.status_translate(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EditAnImageWithAiPrompt
<details><summary><code>client.edit_an_image_with_ai_prompt.<a href="src/gooey/edit_an_image_with_ai_prompt/client.py">img2img</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.edit_an_image_with_ai_prompt.img2img(
    input_image="input_image",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_image:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[Img2ImgPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_controlnet_model:** `typing.Optional[Img2ImgPageRequestSelectedControlnetModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_strength:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**controlnet_conditioning_scale:** `typing.Optional[typing.Sequence[float]]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**image_guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.edit_an_image_with_ai_prompt.<a href="src/gooey/edit_an_image_with_ai_prompt/client.py">async_img2img</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.edit_an_image_with_ai_prompt.async_img2img(
    input_image="input_image",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_image:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[Img2ImgPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_controlnet_model:** `typing.Optional[Img2ImgPageRequestSelectedControlnetModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_strength:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**controlnet_conditioning_scale:** `typing.Optional[typing.Sequence[float]]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**image_guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.edit_an_image_with_ai_prompt.<a href="src/gooey/edit_an_image_with_ai_prompt/client.py">status_img2img</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.edit_an_image_with_ai_prompt.status_img2img(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CompareAiImageGenerators
<details><summary><code>client.compare_ai_image_generators.<a href="src/gooey/compare_ai_image_generators/client.py">compare_text2img</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_image_generators.compare_text2img(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**dall_e3quality:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**dall_e3style:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sd2upscaling:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_models:** `typing.Optional[typing.Sequence[CompareText2ImgPageRequestSelectedModelsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**scheduler:** `typing.Optional[Scheduler]` 
    
</dd>
</dl>

<dl>
<dd>

**edit_instruction:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image_guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compare_ai_image_generators.<a href="src/gooey/compare_ai_image_generators/client.py">async_compare_text2img</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_image_generators.async_compare_text2img(
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**dall_e3quality:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**dall_e3style:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sd2upscaling:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_models:** `typing.Optional[typing.Sequence[CompareText2ImgPageRequestSelectedModelsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**scheduler:** `typing.Optional[Scheduler]` 
    
</dd>
</dl>

<dl>
<dd>

**edit_instruction:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image_guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compare_ai_image_generators.<a href="src/gooey/compare_ai_image_generators/client.py">status_compare_text2img</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_image_generators.status_compare_text2img(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GenerateProductPhotoBackgrounds
<details><summary><code>client.generate_product_photo_backgrounds.<a href="src/gooey/generate_product_photo_backgrounds/client.py">object_inpainting</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.generate_product_photo_backgrounds.object_inpainting(
    input_image="input_image",
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_image:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**obj_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**mask_threshold:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[ObjectInpaintingPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sd2upscaling:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.generate_product_photo_backgrounds.<a href="src/gooey/generate_product_photo_backgrounds/client.py">async_object_inpainting</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.generate_product_photo_backgrounds.async_object_inpainting(
    input_image="input_image",
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_image:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**obj_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**mask_threshold:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[ObjectInpaintingPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sd2upscaling:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.generate_product_photo_backgrounds.<a href="src/gooey/generate_product_photo_backgrounds/client.py">status_object_inpainting</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.generate_product_photo_backgrounds.status_object_inpainting(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AiImageWithAFace
<details><summary><code>client.ai_image_with_a_face.<a href="src/gooey/ai_image_with_a_face/client.py">face_inpainting</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_image_with_a_face.face_inpainting(
    input_image="input_image",
    text_prompt="tony stark from the iron man",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_image:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**face_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**face_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**face_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[FaceInpaintingPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**upscale_factor:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_image_with_a_face.<a href="src/gooey/ai_image_with_a_face/client.py">async_face_inpainting</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_image_with_a_face.async_face_inpainting(
    input_image="input_image",
    text_prompt="tony stark from the iron man",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_image:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**face_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**face_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**face_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[FaceInpaintingPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**upscale_factor:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_image_with_a_face.<a href="src/gooey/ai_image_with_a_face/client.py">status_face_inpainting</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_image_with_a_face.status_face_inpainting(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AiGeneratedPhotoFromEmailProfileLookup
<details><summary><code>client.ai_generated_photo_from_email_profile_lookup.<a href="src/gooey/ai_generated_photo_from_email_profile_lookup/client.py">email_face_inpainting</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_generated_photo_from_email_profile_lookup.email_face_inpainting(
    email_address="sean@dara.network",
    text_prompt="winter's day in paris",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**twitter_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**face_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**face_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**face_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[EmailFaceInpaintingPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**upscale_factor:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**should_send_email:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**email_from:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_cc:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_bcc:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_subject:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_body_enable_html:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**fallback_email_body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_generated_photo_from_email_profile_lookup.<a href="src/gooey/ai_generated_photo_from_email_profile_lookup/client.py">async_email_face_inpainting</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_generated_photo_from_email_profile_lookup.async_email_face_inpainting(
    email_address="sean@dara.network",
    text_prompt="winter's day in paris",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**twitter_handle:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**face_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**face_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**face_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[EmailFaceInpaintingPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**upscale_factor:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**output_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**output_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**should_send_email:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**email_from:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_cc:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_bcc:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_subject:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_body_enable_html:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**fallback_email_body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_generated_photo_from_email_profile_lookup.<a href="src/gooey/ai_generated_photo_from_email_profile_lookup/client.py">status_email_face_inpainting</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_generated_photo_from_email_profile_lookup.status_email_face_inpainting(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## RenderImageSearchResultsWithAi
<details><summary><code>client.render_image_search_results_with_ai.<a href="src/gooey/render_image_search_results_with_ai/client.py">google_image_gen</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.render_image_search_results_with_ai.google_image_gen(
    search_query="search_query",
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[GoogleImageGenPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_strength:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sd2upscaling:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**image_guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.render_image_search_results_with_ai.<a href="src/gooey/render_image_search_results_with_ai/client.py">async_google_image_gen</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.render_image_search_results_with_ai.async_google_image_gen(
    search_query="search_query",
    text_prompt="text_prompt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[GoogleImageGenPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**negative_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_strength:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sd2upscaling:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**image_guidance_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.render_image_search_results_with_ai.<a href="src/gooey/render_image_search_results_with_ai/client.py">status_google_image_gen</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.render_image_search_results_with_ai.status_google_image_gen(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AiBackgroundChanger
<details><summary><code>client.ai_background_changer.<a href="src/gooey/ai_background_changer/client.py">image_segmentation</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_background_changer.image_segmentation(
    input_image="input_image",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_image:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[ImageSegmentationPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**mask_threshold:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**rect_persepective_transform:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**reflection_opacity:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_background_changer.<a href="src/gooey/ai_background_changer/client.py">async_image_segmentation</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_background_changer.async_image_segmentation(
    input_image="input_image",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_image:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[ImageSegmentationPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**mask_threshold:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**rect_persepective_transform:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**reflection_opacity:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_scale:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_x:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**obj_pos_y:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_background_changer.<a href="src/gooey/ai_background_changer/client.py">status_image_segmentation</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.ai_background_changer.status_image_segmentation(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CompareAiImageUpscalers
<details><summary><code>client.compare_ai_image_upscalers.<a href="src/gooey/compare_ai_image_upscalers/client.py">compare_ai_upscalers</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_image_upscalers.compare_ai_upscalers(
    scale=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scale:** `int` — The final upsampling scale of the image
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_image:** `typing.Optional[str]` — Input Image
    
</dd>
</dl>

<dl>
<dd>

**input_video:** `typing.Optional[str]` — Input Video
    
</dd>
</dl>

<dl>
<dd>

**selected_models:** `typing.Optional[typing.Sequence[CompareUpscalerPageRequestSelectedModelsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_bg_model:** `typing.Optional[typing.Literal["real_esrgan_x2"]]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compare_ai_image_upscalers.<a href="src/gooey/compare_ai_image_upscalers/client.py">async_compare_ai_upscalers</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_image_upscalers.async_compare_ai_upscalers(
    scale=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scale:** `int` — The final upsampling scale of the image
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_image:** `typing.Optional[str]` — Input Image
    
</dd>
</dl>

<dl>
<dd>

**input_video:** `typing.Optional[str]` — Input Video
    
</dd>
</dl>

<dl>
<dd>

**selected_models:** `typing.Optional[typing.Sequence[CompareUpscalerPageRequestSelectedModelsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_bg_model:** `typing.Optional[typing.Literal["real_esrgan_x2"]]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compare_ai_image_upscalers.<a href="src/gooey/compare_ai_image_upscalers/client.py">status_compare_ai_upscalers</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.compare_ai_image_upscalers.status_compare_ai_upscalers(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ChyronPlantBot
<details><summary><code>client.chyron_plant_bot.<a href="src/gooey/chyron_plant_bot/client.py">chyron_plant</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.chyron_plant_bot.chyron_plant(
    midi_notes="C#1 B6 A2 A1 A3 A2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**midi_notes:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**midi_notes_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**chyron_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chyron_plant_bot.<a href="src/gooey/chyron_plant_bot/client.py">async_chyron_plant</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.chyron_plant_bot.async_chyron_plant(
    midi_notes="C#1 B6 A2 A1 A3 A2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**midi_notes:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**midi_notes_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**chyron_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chyron_plant_bot.<a href="src/gooey/chyron_plant_bot/client.py">status_chyron_plant</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.chyron_plant_bot.status_chyron_plant(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LetterWriter
<details><summary><code>client.letter_writer.<a href="src/gooey/letter_writer/client.py">letter_writer</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.letter_writer.letter_writer(
    action_id="action_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**prompt_header:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**example_letters:** `typing.Optional[typing.Sequence[TrainingDataModel]]` 
    
</dd>
</dl>

<dl>
<dd>

**lm_selected_api:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lm_selected_engine:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**lm_sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**api_http_method:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**api_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**api_headers:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**api_json_body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**input_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**strip_html2text:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.letter_writer.<a href="src/gooey/letter_writer/client.py">async_letter_writer</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.letter_writer.async_letter_writer(
    action_id="action_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**prompt_header:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**example_letters:** `typing.Optional[typing.Sequence[TrainingDataModel]]` 
    
</dd>
</dl>

<dl>
<dd>

**lm_selected_api:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lm_selected_engine:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**lm_sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**api_http_method:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**api_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**api_headers:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**api_json_body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**input_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**strip_html2text:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.letter_writer.<a href="src/gooey/letter_writer/client.py">status_letter_writer</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.letter_writer.status_letter_writer(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Embeddings
<details><summary><code>client.embeddings.<a href="src/gooey/embeddings/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.embeddings.post(
    texts=["texts"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**texts:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[EmbeddingsPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.embeddings.<a href="src/gooey/embeddings/client.py">async_embeddings</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.embeddings.async_embeddings(
    texts=["texts"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**texts:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[EmbeddingsPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.embeddings.<a href="src/gooey/embeddings/client.py">status_embeddings</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.embeddings.status_embeddings(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PeopleAlsoAskAnswersFromADoc
<details><summary><code>client.people_also_ask_answers_from_a_doc.<a href="src/gooey/people_also_ask_answers_from_a_doc/client.py">related_qna_maker_doc</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.people_also_ask_answers_from_a_doc.related_qna_maker_doc(
    search_query="search_query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**keyword_query:** `typing.Optional[RelatedQnADocPageRequestKeywordQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**doc_extract_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[RelatedQnADocPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[RelatedQnADocPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**citation_style:** `typing.Optional[RelatedQnADocPageRequestCitationStyle]` 
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**serp_search_type:** `typing.Optional[SerpSearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_search_field:** `typing.Optional[str]` — DEPRECATED: use `serp_search_type` instead
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.people_also_ask_answers_from_a_doc.<a href="src/gooey/people_also_ask_answers_from_a_doc/client.py">async_related_qna_maker_doc</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.people_also_ask_answers_from_a_doc.async_related_qna_maker_doc(
    search_query="search_query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RecipeFunction]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Any]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**keyword_query:** `typing.Optional[RelatedQnADocPageRequestKeywordQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_references:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_context_words:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_jump:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**doc_extract_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model:** `typing.Optional[RelatedQnADocPageRequestEmbeddingModel]` 
    
</dd>
</dl>

<dl>
<dd>

**dense_weight:** `typing.Optional[float]` 

Weightage for dense vs sparse embeddings. `0` for sparse, `1` for dense, `0.5` for equal weight.
Generally speaking, dense embeddings excel at understanding the context of the query, whereas sparse vectors excel at keyword matches.
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[RelatedQnADocPageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**avoid_repetition:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**num_outputs:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_tokens:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sampling_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**citation_style:** `typing.Optional[RelatedQnADocPageRequestCitationStyle]` 
    
</dd>
</dl>

<dl>
<dd>

**serp_search_location:** `typing.Optional[SerpSearchLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_locations:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED: use `serp_search_location` instead
    
</dd>
</dl>

<dl>
<dd>

**serp_search_type:** `typing.Optional[SerpSearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**scaleserp_search_field:** `typing.Optional[str]` — DEPRECATED: use `serp_search_type` instead
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RunSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.people_also_ask_answers_from_a_doc.<a href="src/gooey/people_also_ask_answers_from_a_doc/client.py">status_related_qna_maker_doc</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.people_also_ask_answers_from_a_doc.status_related_qna_maker_doc(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Misc
<details><summary><code>client.misc.<a href="src/gooey/misc/client.py">get_balance</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.misc.get_balance()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.misc.<a href="src/gooey/misc/client.py">video_bots_broadcast</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.misc.video_bots_broadcast(
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text:** `str` — Message to broadcast to all users
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**audio:** `typing.Optional[str]` — Audio URL to send to all users
    
</dd>
</dl>

<dl>
<dd>

**video:** `typing.Optional[str]` — Video URL to send to all users
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.Sequence[str]]` — Video URL to send to all users
    
</dd>
</dl>

<dl>
<dd>

**buttons:** `typing.Optional[typing.Sequence[ReplyButton]]` — Buttons to send to all users
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[BotBroadcastFilters]` — Filters to select users to broadcast to. If not provided, will broadcast to all users of this bot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.misc.<a href="src/gooey/misc/client.py">health</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import Gooey

client = Gooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)
client.misc.health()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

