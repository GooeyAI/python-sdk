# GooeyAI Python SDK

## Usage

[Lipsync+TTS](https://gooey.ai/LipsyncTTS) with a local image.

??? note "API Key"
    You need a Gooey API key to use this SDK. You can obtain it
    from your [Gooey.AI account page](https://gooey.ai/account/api-keys)
    and set it to the environment variable `GOOEY_API_KEY`.

    ```shell
    export GOOEY_API_KEY=sk-...
    ```

```python
from gooey import Gooey

client = Gooey()
result = client.lipsync_tts(
    input_face="./image.jpg",
    text_prompt="Gooey.AI is awesome!",
)
print(result.output_video)
```
