"""
Environment variable loader and validator for ViBR.

Supports Gemini authentication via:
  1. GOOGLE_GENERATIVE_AI_API_KEY (Google AI Studio)
  2. Application Default Credentials (ADC) with google-auth (Vertex AI)
     Optional: GEMINI_VERTEX_PROJECT_ID, GEMINI_VERTEX_LOCATION
"""

from pathlib import Path
from typing import Dict, List

from dotenv import dotenv_values, load_dotenv


class EnvError(ValueError):
    """Raised when required environment variables are missing."""


REQUIRED_ENV_BY_LLM: Dict[str, List[str]] = {
    "gemini": [],  # Gemini uses google-auth or API key (both optional, one required at runtime)
    "openai": ["OPENAI_API_KEY"],
}


def load_and_validate_env(env_file: Path, llm: str) -> Dict[str, str]:
    """Load .env values and validate provider-specific requirements.

    Args:
        env_file: Path to .env.local file
        llm: LLM provider name ("gemini" or "openai")

    Returns:
        Dictionary of environment variables

    Raises:
        EnvError: If validation fails
    """
    if not env_file.exists():
        raise EnvError(f"Environment file not found: {env_file}")

    load_dotenv(dotenv_path=env_file, override=False)
    values = {k: v for k, v in dotenv_values(env_file).items() if v is not None}

    llm_name = llm.lower()
    if llm_name not in REQUIRED_ENV_BY_LLM:
        supported = ", ".join(sorted(REQUIRED_ENV_BY_LLM.keys()))
        raise EnvError(f"Unsupported llm '{llm}'. Supported values: {supported}")

    # For Gemini, no env vars are strictly required here — auth is handled at runtime
    # (GOOGLE_GENERATIVE_AI_API_KEY or ADC)
    if llm_name == "gemini":
        return values

    # For OpenAI, OPENAI_API_KEY is required
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
