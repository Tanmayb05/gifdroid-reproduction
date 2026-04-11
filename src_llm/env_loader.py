from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from dotenv import dotenv_values, load_dotenv


class EnvError(ValueError):
    """Raised when required environment variables are missing."""


REQUIRED_ENV_BY_LLM: Dict[str, List[str]] = {
    "gemini": [],
    "sonnet": ["ANTHROPIC_API_KEY"],
    "claude": ["ANTHROPIC_API_KEY"],
    # Local Ollama providers — all share LLAMA_BASE_URL (http://localhost:11434/v1).
    # LLAMA_API_KEY is optional (not needed for local Ollama).
    "llama": ["LLAMA_BASE_URL"],
    "llava": ["LLAMA_BASE_URL"],
    "minicpm": ["LLAMA_BASE_URL"],
    "gemma": ["LLAMA_BASE_URL"],
    # QWEN_BASE_URL is required; QWEN_API_KEY is optional (not needed for local Ollama).
    # Model is set via llm_model in config.yml, so QWEN_MODEL is not required here.
    "qwen": ["QWEN_BASE_URL"],
}


def load_and_validate_env(env_file: Path, llm: str) -> Dict[str, str]:
    """Load .env values and validate provider-specific requirements."""
    if not env_file.exists():
        raise EnvError(f"Environment file not found: {env_file}")

    load_dotenv(dotenv_path=env_file, override=False)
    values = {k: v for k, v in dotenv_values(env_file).items() if v is not None}

    llm_name = llm.lower()
    if llm_name not in REQUIRED_ENV_BY_LLM:
        supported = ", ".join(sorted(REQUIRED_ENV_BY_LLM.keys()))
        raise EnvError(f"Unsupported llm '{llm}'. Supported values: {supported}")

    if llm_name == "gemini":
        if str(values.get("GEMINI_SERVICE_ACCOUNT_FILE", "")).strip():
            raise EnvError(
                "GEMINI_SERVICE_ACCOUNT_FILE is no longer supported. "
                "Use GOOGLE_GENERATIVE_AI_API_KEY or ADC via google.auth.default()."
            )

        return values

    missing = [
        key
        for key in REQUIRED_ENV_BY_LLM[llm_name]
        if key not in values or not str(values[key]).strip()
    ]
    if missing:
        raise EnvError(
            f"Missing required env vars for llm='{llm_name}': {', '.join(missing)}"
        )

    return values
