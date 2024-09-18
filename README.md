<h3 align="center">
  <img src="https://storage.googleapis.com/dara-c1b52.appspot.com/daras_ai/media/cdc58fe0-2da1-11ef-84df-02420a0001f4/githubbanner.png"
  />
</h3>
<p align="center">
  <a href="https://gooey.ai">🏠 Homepage</a> ·
  <a href="https://gooey.ai/explore">👾 Explore Workflows</a> ·
  <a href="https://gooey.ai/docs">📚 Docs</a> ·
  <a href="https://gooey.ai/api">🤖 API</a> ·
  <a href="https://gooey.ai/discord">🛟 Discord</a> ·
  <a href="https://gooey.ai/account">💃🏾 Start Building</a>
</p>

<div>
  <p align="center">
    <a
    href="https://x.com/GooeyAI">
        <img src="https://img.shields.io/badge/X/Twitter-000000?style=for-the-badge&logo=x&logoColor=white" />
    </a>
    <a href="https://in.linkedin.com/company/gooeyai">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>
    <a href="https://gooey.ai/discord">
        <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" />
    </a>
    <a href="https://www.youtube.com/@gooeyai">
        <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
    </a>
 </p>
</div>

[Gooey.AI](http://gooey.ai/) is the low-code orchestration platform with **discoverable workflows** & **unified billing to all of GenAI universe.** 

# Gooey Python Library

The Gooey Python library provides convenient access to the Gooey API from Python.

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)
[![pypi](https://img.shields.io/pypi/v/gooeyai)](https://pypi.python.org/pypi/gooeyai)

# 🤖🐍📦 What Gooey.AI SDK offers?

Gooey.AI simplifies building AI workflows by:
- Offering high and flexible interoperability
- Single API key to run several AI workflows
- Hosting private and open-source AI models - LLMs, ASR, Image and Animation

## 🧑‍💻 Who is this for and why would I want to use it?

- Any developer who wants to quickly prototype with GenAI apps
- Great for those who want to include GenAI in their existing product or app
- Gooey.AI SDKs are great for speedy GTMs as we are already built to scale! 
  
## Try it on Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EH8zh_zPZgyksR9uitGSO_iXn0JU-JmD?usp=sharing)

## Installation

```sh
pip install gooeyai
```

## Usage

Instantiate and use the client with the following:

```python
from gooey import AnimationPrompt, Gooey

client = Gooey(
    api_key="YOUR_API_KEY",
)
client.lipsync(
    input_face="./path/to/face.mp4",
    input_audio="./path/to/audio.mp3",
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from gooey import AnimationPrompt, AsyncGooey

client = AsyncGooey(
    api_key="YOUR_API_KEY",
)


async def main() -> None:
    await client.lipsync(
        input_face="./path/to/face.mp4",
        input_audio="./path/to/audio.mp3",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from gooey.core.api_error import ApiError

try:
    client.animate(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retriable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.animate(..., {
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from gooey import Gooey

client = Gooey(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.animate(..., {
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.
```python
import httpx
from gooey import Gooey

client = Gooey(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.

Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
