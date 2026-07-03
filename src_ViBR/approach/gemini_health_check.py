"""
Gemini API health check tool.
Tests basic API connectivity and model responsiveness before starting inference.
"""

import json
import logging
import sys
import time
from pathlib import Path
from urllib import error as url_error, request as url_request

logger = logging.getLogger(__name__)


def test_gemini_api(model: str = "gemini-2.5-flash", timeout: int = 60) -> bool:
    """
    Test Gemini API connectivity with a simple text request.

    Args:
        model: Model name to test
        timeout: Timeout in seconds for the request

    Returns:
        True if API is working, False otherwise
    """
    from gemini_api import _build_url_and_headers

    logger.info("=" * 70)
    logger.info("🔍 Testing Gemini API Health...")
    logger.info("=" * 70)
    logger.info(f"Model: {model}")
    logger.info(f"Timeout: {timeout}s")

    try:
        url, headers = _build_url_and_headers(model)
        logger.info(f"✅ Built URL and headers")

        payload = {
            "contents": [{
                "role": "user",
                "parts": [{"text": "Say 'API is working' in 5 words or less."}]
            }],
            "generationConfig": {"temperature": 0.1},
        }
        payload_bytes = json.dumps(payload).encode("utf-8")

        req = url_request.Request(
            url=url,
            data=payload_bytes,
            headers=headers,
            method="POST"
        )

        logger.info(f"📤 Sending test request to Gemini API...")
        start_time = time.time()

        with url_request.urlopen(req, timeout=timeout) as resp:
            response_text = resp.read().decode("utf-8")
            elapsed = time.time() - start_time

        data = json.loads(response_text)
        candidates = data.get("candidates", [])

        if not candidates:
            logger.error("❌ No candidates in response")
            return False

        text_response = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        usage = data.get("usageMetadata", {})
        prompt_tokens = usage.get("promptTokenCount", 0)
        output_tokens = usage.get("candidatesTokenCount", 0)

        logger.info(f"✅ API Response received in {elapsed:.2f}s")
        logger.info(f"   Response: {text_response[:100]}")
        logger.info(f"   Tokens: {prompt_tokens} input, {output_tokens} output")
        logger.info("=" * 70)
        logger.info("✅ Gemini API is HEALTHY")
        logger.info("=" * 70)

        return True

    except url_error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        logger.error(f"❌ HTTP Error {exc.code}: {body[:300]}")
        logger.error("=" * 70)
        return False

    except url_error.URLError as exc:
        logger.error(f"❌ URL Error: {exc}")
        logger.error("=" * 70)
        return False

    except TimeoutError as exc:
        logger.error(f"❌ Timeout Error: {exc}")
        logger.error("=" * 70)
        return False

    except Exception as exc:
        logger.error(f"❌ Unexpected error: {type(exc).__name__}: {exc}")
        logger.error("=" * 70)
        return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    model = sys.argv[1] if len(sys.argv) > 1 else "gemini-2.5-flash"
    timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 60

    success = test_gemini_api(model, timeout)
    sys.exit(0 if success else 1)
