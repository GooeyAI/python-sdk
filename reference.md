# Reference
<details><summary><code>client.<a href="src/gooey/client.py">animate</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from gooey import DeforumSdPageRequestAnimationPromptsItem, Gooey

client = Gooey(
    api_key="YOUR_API_KEY",
)
client.animate(
    animation_prompts=[
        DeforumSdPageRequestAnimationPromptsItem(
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

**animation_prompts:** `typing.Sequence[DeforumSdPageRequestAnimationPromptsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[DeforumSdPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

<details><summary><code>client.<a href="src/gooey/client.py">qr_code</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.qr_code(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[QrCodeRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**qr_code_data:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**qr_code_input_image:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**qr_code_vcard:** `typing.Optional[QrCodeRequestQrCodeVcard]` 
    
</dd>
</dl>

<dl>
<dd>

**qr_code_file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
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

**image_prompt_controlnet_models:** `typing.Optional[typing.List[QrCodeRequestImagePromptControlnetModelsItem]]` 
    
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

**selected_model:** `typing.Optional[QrCodeRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_controlnet_model:** `typing.Optional[typing.List[QrCodeRequestSelectedControlnetModelItem]]` 
    
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

**controlnet_conditioning_scale:** `typing.Optional[typing.List[float]]` 
    
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

**scheduler:** `typing.Optional[QrCodeRequestScheduler]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">seo_people_also_ask</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.seo_people_also_ask(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RelatedQnAPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**response_format_type:** `typing.Optional[RelatedQnAPageRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">seo_content</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.seo_content(
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

**example_id:** `typing.Optional[str]` 
    
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

**response_format_type:** `typing.Optional[SeoSummaryPageRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">web_search_llm</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.web_search_llm(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[GoogleGptPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**response_format_type:** `typing.Optional[GoogleGptPageRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">personalize_email</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.personalize_email(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[SocialLookupEmailPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**response_format_type:** `typing.Optional[SocialLookupEmailPageRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">bulk_run</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.bulk_run(
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

**documents:** `from __future__ import annotations

typing.List[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**run_urls:** `typing.List[str]` 


Provide one or more Gooey.AI workflow runs.
You can add multiple runs from the same recipe (e.g. two versions of your copilot) and we'll run the inputs over both of them.
            
    
</dd>
</dl>

<dl>
<dd>

**input_columns:** `typing.Dict[str, str]` 


For each input field in the Gooey.AI workflow, specify the column in your input data that corresponds to it.
            
    
</dd>
</dl>

<dl>
<dd>

**output_columns:** `typing.Dict[str, str]` 


For each output field in the Gooey.AI workflow, specify the column name that you'd like to use for it in the output data.
            
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[BulkRunRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**eval_urls:** `typing.Optional[typing.List[str]]` 


_(optional)_ Add one or more Gooey.AI Evaluator Workflows to evaluate the results of your runs.
            
    
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

<details><summary><code>client.<a href="src/gooey/client.py">eval</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.eval(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[BulkEvalPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**eval_prompts:** `typing.Optional[typing.Sequence[BulkEvalPageRequestEvalPromptsItem]]` 


Specify custom LLM prompts to calculate metrics that evaluate each row of the input data. The output should be a JSON object mapping the metric names to values.  
_The `columns` dictionary can be used to reference the spreadsheet columns._            
            
    
</dd>
</dl>

<dl>
<dd>

**agg_functions:** `typing.Optional[typing.Sequence[BulkEvalPageRequestAggFunctionsItem]]` 


Aggregate using one or more operations. Uses [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html#dataframegroupby-computations-descriptive-stats).
            
    
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

**response_format_type:** `typing.Optional[BulkEvalPageRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">synthesize_data</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.synthesize_data()

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

**documents:** `from __future__ import annotations

typing.List[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[SynthesizeDataRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**sheet_url:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**selected_asr_model:** `typing.Optional[SynthesizeDataRequestSelectedAsrModel]` 
    
</dd>
</dl>

<dl>
<dd>

**google_translate_target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**glossary_document:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**task_instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[SynthesizeDataRequestSelectedModel]` 
    
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

**response_format_type:** `typing.Optional[SynthesizeDataRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">llm</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.llm()

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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[CompareLlmPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

<details><summary><code>client.<a href="src/gooey/client.py">rag</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.rag(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[DocSearchPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**citation_style:** `typing.Optional[DocSearchPageRequestCitationStyle]` 
    
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

**response_format_type:** `typing.Optional[DocSearchPageRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">smart_gpt</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.smart_gpt(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[SmartGptPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**response_format_type:** `typing.Optional[SmartGptPageRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">doc_summary</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.doc_summary()

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

**documents:** `from __future__ import annotations

typing.List[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[DocSummaryRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**selected_model:** `typing.Optional[DocSummaryRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**chain_type:** `typing.Optional[typing.Literal["map_reduce"]]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_asr_model:** `typing.Optional[DocSummaryRequestSelectedAsrModel]` 
    
</dd>
</dl>

<dl>
<dd>

**google_translate_target:** `typing.Optional[str]` 
    
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

**response_format_type:** `typing.Optional[DocSummaryRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">functions</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.functions()

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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — The JS code to be executed.
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used in the code
    
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

<details><summary><code>client.<a href="src/gooey/client.py">lipsync</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.lipsync()

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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[LipsyncRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
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

**sadtalker_settings:** `typing.Optional[LipsyncRequestSadtalkerSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[LipsyncRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_audio:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
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

<details><summary><code>client.<a href="src/gooey/client.py">lipsync_tts</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.lipsync_tts(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[LipsyncTtsRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**tts_provider:** `typing.Optional[LipsyncTtsRequestTtsProvider]` 
    
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

**openai_voice_name:** `typing.Optional[LipsyncTtsRequestOpenaiVoiceName]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_tts_model:** `typing.Optional[LipsyncTtsRequestOpenaiTtsModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
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

**sadtalker_settings:** `typing.Optional[LipsyncTtsRequestSadtalkerSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[LipsyncTtsRequestSelectedModel]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">text_to_speech</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.text_to_speech(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[TextToSpeechPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

<details><summary><code>client.<a href="src/gooey/client.py">speech_recognition</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.speech_recognition()

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

**documents:** `from __future__ import annotations

typing.List[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[SpeechRecognitionRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[SpeechRecognitionRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**translation_model:** `typing.Optional[SpeechRecognitionRequestTranslationModel]` 
    
</dd>
</dl>

<dl>
<dd>

**output_format:** `typing.Optional[SpeechRecognitionRequestOutputFormat]` 
    
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

**glossary_document:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
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

<details><summary><code>client.<a href="src/gooey/client.py">text_to_music</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.text_to_music(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[Text2AudioPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

<details><summary><code>client.<a href="src/gooey/client.py">translate</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.translate()

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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[TranslateRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**texts:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[TranslateRequestSelectedModel]` 
    
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

**glossary_document:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
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

<details><summary><code>client.<a href="src/gooey/client.py">remix_image</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.remix_image()

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

**input_image:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[RemixImageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[RemixImageRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_controlnet_model:** `typing.Optional[RemixImageRequestSelectedControlnetModel]` 
    
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

**controlnet_conditioning_scale:** `typing.Optional[typing.List[float]]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">text_to_image</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.text_to_image(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[CompareText2ImgPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**scheduler:** `typing.Optional[CompareText2ImgPageRequestScheduler]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">product_image</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.product_image(
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

**input_image:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[ProductImageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**selected_model:** `typing.Optional[ProductImageRequestSelectedModel]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">portrait</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.portrait(
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

**input_image:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**text_prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[PortraitRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**selected_model:** `typing.Optional[PortraitRequestSelectedModel]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">image_from_email</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.image_from_email(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[EmailFaceInpaintingPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

<details><summary><code>client.<a href="src/gooey/client.py">image_from_web_search</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.image_from_web_search(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[GoogleImageGenPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

<details><summary><code>client.<a href="src/gooey/client.py">remove_background</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.remove_background()

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

**input_image:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[RemoveBackgroundRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[RemoveBackgroundRequestSelectedModel]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">upscale</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.upscale(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[UpscaleRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
</dd>
</dl>

<dl>
<dd>

**input_image:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**input_video:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**selected_models:** `typing.Optional[typing.List[UpscaleRequestSelectedModelsItem]]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">embed</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.embed(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[EmbeddingsPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

<details><summary><code>client.<a href="src/gooey/client.py">seo_people_also_ask_doc</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.seo_people_also_ask_doc(
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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.Sequence[RelatedQnADocPageRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**citation_style:** `typing.Optional[RelatedQnADocPageRequestCitationStyle]` 
    
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

**response_format_type:** `typing.Optional[RelatedQnADocPageRequestResponseFormatType]` 
    
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

<details><summary><code>client.<a href="src/gooey/client.py">health_status_get</a>()</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.health_status_get()

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

## Copilot
<details><summary><code>client.copilot.<a href="src/gooey/copilot/client.py">completion</a>(...)</code></summary>
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
    api_key="YOUR_API_KEY",
)
client.copilot.completion()

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

**example_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**functions:** `typing.Optional[typing.List[CopilotCompletionRequestFunctionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables to be used as Jinja prompt templates and in functions as arguments
    
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

**input_images:** `from __future__ import annotations

typing.Optional[typing.List[core.File]]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**input_documents:** `from __future__ import annotations

typing.Optional[typing.List[core.File]]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**doc_extract_url:** `typing.Optional[str]` — Select a workflow to extract text from documents and images.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.List[CopilotCompletionRequestMessagesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**bot_script:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_model:** `typing.Optional[CopilotCompletionRequestSelectedModel]` 
    
</dd>
</dl>

<dl>
<dd>

**document_model:** `typing.Optional[str]` — When your copilot users upload a photo or pdf, what kind of document are they mostly likely to upload? (via [Azure](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api?view=doc-intel-3.1.0&tabs=linux&pivots=programming-language-rest-api))
    
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

**documents:** `from __future__ import annotations

typing.Optional[typing.List[core.File]]` — See core.File for more documentation
    
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

**embedding_model:** `typing.Optional[CopilotCompletionRequestEmbeddingModel]` 
    
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

**citation_style:** `typing.Optional[CopilotCompletionRequestCitationStyle]` 
    
</dd>
</dl>

<dl>
<dd>

**use_url_shortener:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**asr_model:** `typing.Optional[CopilotCompletionRequestAsrModel]` — Choose a model to transcribe incoming audio messages to text.
    
</dd>
</dl>

<dl>
<dd>

**asr_language:** `typing.Optional[str]` — Choose a language to transcribe incoming audio messages to text.
    
</dd>
</dl>

<dl>
<dd>

**translation_model:** `typing.Optional[CopilotCompletionRequestTranslationModel]` 
    
</dd>
</dl>

<dl>
<dd>

**user_language:** `typing.Optional[str]` — Choose a language to translate incoming text & audio messages to English and responses back to your selected language. Useful for low-resource languages.
    
</dd>
</dl>

<dl>
<dd>

**input_glossary_document:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**output_glossary_document:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**lipsync_model:** `typing.Optional[CopilotCompletionRequestLipsyncModel]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[typing.Literal["json_to_pdf"]]]` — Give your copilot superpowers by giving it access to tools. Powered by [Function calling](https://platform.openai.com/docs/guides/function-calling).
    
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

**response_format_type:** `typing.Optional[CopilotCompletionRequestResponseFormatType]` 
    
</dd>
</dl>

<dl>
<dd>

**tts_provider:** `typing.Optional[CopilotCompletionRequestTtsProvider]` 
    
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

**openai_voice_name:** `typing.Optional[CopilotCompletionRequestOpenaiVoiceName]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_tts_model:** `typing.Optional[CopilotCompletionRequestOpenaiTtsModel]` 
    
</dd>
</dl>

<dl>
<dd>

**input_face:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
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

**sadtalker_settings:** `typing.Optional[CopilotCompletionRequestSadtalkerSettings]` 
    
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

