from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict
from urllib import error as url_error
from urllib import request as url_request

from dotenv import dotenv_values


DEFAULT_LLAMA_MODEL = "llama3.2-vision:latest"


class LlamaPrereqError(RuntimeError):
    """Raised when Llama endpoint/model prerequisite checks fail."""


def _resolve_chat_completions_url(base_url: str) -> str:
    normalized_base = str(base_url).strip().rstrip("/")
    if not normalized_base:
        raise LlamaPrereqError("Missing LLAMA_BASE_URL.")
    if normalized_base.endswith("/v1/chat/completions"):
        return normalized_base
    if normalized_base.endswith("/v1"):
        return f"{normalized_base}/chat/completions"
    return f"{normalized_base}/v1/chat/completions"


def assert_llama_accessible(
    *,
    base_url: str,
    model: str,
    api_key: str = "",
    timeout_sec: int = 20,
) -> None:
    if not str(model).strip():
        raise LlamaPrereqError("Missing llama model id.")

    url = _resolve_chat_completions_url(base_url)
    headers = {"Content-Type": "application/json"}
    if str(api_key).strip():
        headers["Authorization"] = f"Bearer {api_key.strip()}"

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Reply with exactly: OK"}],
        "temperature": 0.0,
        "max_tokens": 8,
    }
    req = url_request.Request(
        url=url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with url_request.urlopen(req, timeout=timeout_sec) as response:
            raw = response.read().decode("utf-8")
    except url_error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        raise LlamaPrereqError(
            f"Llama prerequisite failed (HTTP {exc.code}): {err_body[:300]}"
        ) from exc
    except url_error.URLError as exc:
        raise LlamaPrereqError(f"Llama prerequisite failed (URL error): {exc}") from exc
    except TimeoutError as exc:
        raise LlamaPrereqError(
            f"Llama prerequisite failed (timeout after {timeout_sec}s)."
        ) from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise LlamaPrereqError(
            "Llama prerequisite failed: endpoint returned non-JSON response."
        ) from exc

    if not isinstance(data.get("choices"), list) or not data["choices"]:
        raise LlamaPrereqError(
            "Llama prerequisite failed: response missing 'choices'."
        )


def _load_env_values(env_file: Path) -> Dict[str, str]:
    if not env_file.exists():
        raise LlamaPrereqError(f"Environment file not found: {env_file}")
    return {k: v for k, v in dotenv_values(env_file).items() if isinstance(v, str)}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check if a Llama endpoint/model is accessible."
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=Path(".env.local"),
        help="Path to .env file containing LLAMA_BASE_URL and optional LLAMA_API_KEY.",
    )
    parser.add_argument(
        "--base-url",
        type=str,
        default=None,
        help="Override LLAMA_BASE_URL from env.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help=f"Model id to check (default: {DEFAULT_LLAMA_MODEL}).",
    )
    parser.add_argument(
        "--timeout-sec",
        type=int,
        default=20,
        help="HTTP timeout in seconds.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        env = _load_env_values(args.env_file)
        base_url = args.base_url or str(env.get("LLAMA_BASE_URL", "")).strip()
        model = args.model or str(env.get("LLAMA_MODEL", "")).strip() or DEFAULT_LLAMA_MODEL
        api_key = str(env.get("LLAMA_API_KEY", "")).strip()

        assert_llama_accessible(
            base_url=base_url,
            model=model,
            api_key=api_key,
            timeout_sec=args.timeout_sec,
        )
        print(f"[llama_prereq] OK | model={model} | base_url={base_url}")
        return 0
    except LlamaPrereqError as exc:
        print(f"[llama_prereq] ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
