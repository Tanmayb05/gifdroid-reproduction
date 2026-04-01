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
    timeout_sec: int | None = 20,
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


def check_metal_acceleration(base_url: str, timeout_sec: int | None = 10) -> Dict[str, object]:
    """Query Ollama /api/ps to check whether the running model is using Metal (Apple Silicon GPU).

    Returns a dict with keys:
      - metal: bool — True if all processors are GPU (Metal), False if any CPU
      - processors: str — raw value from Ollama, e.g. "100% GPU" or "100% CPU"
      - model: str — name of the first running model found
      - raw: the full /api/ps response

    Raises LlamaPrereqError if the endpoint is unreachable or returns unexpected data.
    """
    normalized = str(base_url).strip().rstrip("/")
    # Strip /v1 or /v1/chat/completions suffix to get the Ollama root
    for suffix in ("/v1/chat/completions", "/v1"):
        if normalized.endswith(suffix):
            normalized = normalized[: -len(suffix)]
            break
    url = f"{normalized}/api/ps"

    req = url_request.Request(url=url, method="GET")
    try:
        with url_request.urlopen(req, timeout=timeout_sec) as response:
            raw = response.read().decode("utf-8")
    except url_error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        raise LlamaPrereqError(
            f"Metal check failed (HTTP {exc.code}): {err_body[:300]}"
        ) from exc
    except url_error.URLError as exc:
        raise LlamaPrereqError(f"Metal check failed (URL error): {exc}") from exc
    except TimeoutError as exc:
        raise LlamaPrereqError(f"Metal check failed (timeout after {timeout_sec}s).") from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise LlamaPrereqError("Metal check failed: /api/ps returned non-JSON.") from exc

    models = data.get("models")
    if not isinstance(models, list) or not models:
        raise LlamaPrereqError(
            "Metal check: no models currently loaded in Ollama. "
            "Run a model first (e.g. ollama run llama3.2-vision) then retry."
        )

    first = models[0]
    # /api/ps returns {"name": "llama3.2-vision:latest", "processors": "100% GPU", "size_vram": ..., ...}
    processors_field = str(first.get("processors", "")).strip()
    size_vram = first.get("size_vram", 0)

    if processors_field:
        metal = "gpu" in processors_field.lower() and "cpu" not in processors_field.lower()
        processors_display = processors_field
    elif size_vram:
        metal = int(size_vram) > 0
        vram_gb = int(size_vram) / (1024 ** 3)
        processors_display = f"GPU ({vram_gb:.1f} GB VRAM)"
    else:
        metal = False
        processors_display = "unknown (no processors or size_vram field)"

    model_name = str(first.get("name") or first.get("model") or "unknown")

    return {
        "metal": metal,
        "processors": processors_display,
        "model": model_name,
        "raw": data,
    }


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
    parser.add_argument(
        "--check-metal",
        action="store_true",
        help="Check whether Ollama is running on Apple Silicon GPU (Metal) instead of CPU.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        env = _load_env_values(args.env_file)
        base_url = args.base_url or str(env.get("LLAMA_BASE_URL", "")).strip()
        model = args.model or str(env.get("LLAMA_MODEL", "")).strip() or DEFAULT_LLAMA_MODEL
        api_key = str(env.get("LLAMA_API_KEY", "")).strip()
        timeout_raw = str(env.get("LLAMA_PREREQ_TIMEOUT_SEC", "")).strip()
        if timeout_raw:
            try:
                parsed = int(timeout_raw)
                timeout_sec: int | None = parsed if parsed > 0 else None
            except ValueError:
                timeout_sec = args.timeout_sec
        else:
            timeout_sec = None

        assert_llama_accessible(
            base_url=base_url,
            model=model,
            api_key=api_key,
            timeout_sec=timeout_sec,
        )
        print(f"[llama_prereq] OK | model={model} | base_url={base_url}")

        if args.check_metal:
            result = check_metal_acceleration(base_url=base_url, timeout_sec=timeout_sec)
            status = "METAL (Apple Silicon GPU)" if result["metal"] else "CPU (not using Metal)"
            print(
                f"[llama_prereq] acceleration={status} | "
                f"model={result['model']} | processors={result['processors']}"
            )
            if not result["metal"]:
                print(
                    "[llama_prereq] WARNING: Ollama is not using Metal acceleration. "
                    "Inference will be slow. Ensure Ollama is the macOS native build "
                    "(not Rosetta or Docker) and that the model fits in unified memory."
                )

        return 0
    except LlamaPrereqError as exc:
        print(f"[llama_prereq] ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
