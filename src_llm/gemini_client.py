"""Lightweight functional Gemini client for quick scripts/notebooks.

For production automation flows, use GeminiProvider in providers.py instead —
it has retry/backoff, Vertex/ADC auth fallback, and video mode.
"""

from __future__ import annotations

import os
import threading
from typing import Any

_client_instance: Any = None
_client_key: str | None = None
_client_lock = threading.Lock()


def api_key() -> str | None:
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if key:
        return key
    return os.environ.get("GOOGLE_GENERATIVE_AI_API_KEY", "").strip() or None


def model() -> str:
    return os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")


def client(api_key_override: str | None = None) -> Any:
    global _client_instance, _client_key

    try:
        from google import genai
    except ImportError as exc:
        raise RuntimeError(
            "Gemini support requires the google-genai package. "
            "Install dependencies from src_llm/requirements.txt"
        ) from exc

    resolved_key = api_key_override or api_key()
    if not resolved_key:
        raise RuntimeError(
            "GEMINI_API_KEY (or GOOGLE_GENERATIVE_AI_API_KEY) is required for Gemini."
        )

    with _client_lock:
        if _client_instance is None or _client_key != resolved_key:
            _client_instance = genai.Client(api_key=resolved_key)
            _client_key = resolved_key
        return _client_instance


def load_image(path: str) -> Any:
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("Gemini image support requires Pillow.") from exc

    return Image.open(path)


def ask(prompt: str, image_paths: list[str]) -> str:
    contents: list[Any] = [prompt]
    contents.extend(load_image(p) for p in image_paths)
    response = client().models.generate_content(
        model=model(),
        contents=contents,
    )
    return response.text.strip()
