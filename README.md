# Gooey Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)
[![pypi](https://img.shields.io/pypi/v/gooey)](https://pypi.python.org/pypi/gooey)

The Gooey Python library provides convenient access to the Gooey API from Python.

## Installation

```sh
pip install gooey
```

## Usage

Instantiate and use the client with the following:

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

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from gooey import AsyncGooey

client = AsyncGooey(
    authorization="YOUR_AUTHORIZATION",
    api_key="YOUR_API_KEY",
)


async def main() -> None:
    await client.copilot_integrations.video_bots_stream_create(
        integration_id="integration_id",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from .api_error import ApiError

try:
    client.copilot_integrations.video_bots_stream_create(...)
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
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.copilot_integrations.video_bots_stream_create(...,{
    max_retries=1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from gooey import Gooey

client = Gooey(..., { timeout=20.0 }, )


# Override timeout for a specific method
client.copilot_integrations.video_bots_stream_create(...,{
    timeout_in_seconds=1
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
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!