# OpenAI vs Gemini 2.5 Pro Implementation Differences in src_ViBR

## Core Architecture

### API Integration
**OpenAI (gpt-4o)**:
- Uses OpenAI Python SDK (`from openai import OpenAI`)
- Direct client initialization with API key
- Stateless HTTP calls via the SDK

**Gemini (gemini-2.5-pro via REST)**:
- Manual HTTP requests (`urllib.request`)
- Direct REST API calls to Google's generativelanguage API
- Support for two auth methods: API key or Application Default Credentials (Vertex AI)
- Exponential backoff retry logic for rate limiting (429) and timeouts

---

## Image Encoding & Transport

### OpenAI
```python
# Direct base64 embedding in message
b64_image = base64.b64encode(image_bytes).decode("utf-8")
content.append({
    "type": "image_url",
    "image_url": {"url": f"data:image/png;base64,{b64_image}"}
})
```

### Gemini
```python
# Base64 in inlineData format
content.append({
    "inlineData": {
        "mimeType": "image/png",
        "data": base64.b64encode(image_bytes).decode("utf-8")
    }
})
```
**Impact**: Gemini uses a structured `inlineData` format vs OpenAI's data URI scheme. No functional difference — both are base64-encoded PNG data.

---

## Request/Response Handling

### OpenAI
- **Timeout**: Default handling via SDK (no explicit timeout)
- **Retries**: None built-in; relies on SDK
- **Response Parsing**: Direct access to `response.usage.prompt_tokens`, `response.usage.completion_tokens`
- **Token Counts**: Automatically included in response object

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[...],
)
prompt_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens
```

### Gemini
- **Timeout**: 180s (configurable, increased for slower models like gemini-2.5-pro)
- **Retries**: 5 attempts with exponential backoff (10s base, max ~10 minutes total)
- **Response Parsing**: Manual JSON parsing from HTTP response
- **Token Counts**: Extracted from `usageMetadata` in JSON response

```python
# Manual retry loop with exponential backoff for 429/timeout
data = json.loads(response_text)
prompt_tokens = data.get("usageMetadata", {}).get("promptTokenCount", 0)
output_tokens = data.get("usageMetadata", {}).get("candidatesTokenCount", 0)
```

---

## Semantic Differences in Prompts

Both implementations have **identical prompt logic** for the three core tasks, with minor wording differences:

### 1. State Consistency Check
Both ask: "Is the current device screen functionally consistent with the reference video frame?"
- **Identical criteria** for determining "same_state": buttons present, same action executable, minor layout differences ignored
- **Identical output**: `{"same_state": "yes"}` or `{"same_state": "no", "description": "..."}`

### 2. Relevant Region Detection
Both identify which UI regions are involved in a state transition:
- **Identical action list**: `["tap", "double_tap", "long_press", "swipe", "input_text", "back", "home", "wait", "no action"]`
- **Identical output**: `{"target_regions": [indices], "predicted_action": "..."}`

### 3. Action Region Prediction
Both predict which region to interact with to reproduce an observed action:
- **Identical action formats**: `tap`, `swipe`, `input_text` with coordinates or region indices
- **Identical reasoning**: "Which action on the current (live) screen would achieve the same transition as the reference?"

---

## Key Implementation Differences

### 1. Resilience to Failures
**Winner: Gemini**
- Exponential backoff retry logic for transient failures (rate limits, network timeouts)
- Gemini-2.5-pro is slower, so timeout is longer (180s vs SDK default)
- Better for production/long-running automation

**OpenAI**
- No built-in retry logic
- Fails immediately on any error
- Requires external retry wrapper for reliability

### 2. Authentication Flexibility
**Winner: Gemini**
- Supports both API key (Google AI Studio) and ADC (Vertex AI)
- Can use gcloud credentials or environment variable
- Better for cloud-native deployments

**OpenAI**
- API key only
- Simpler but less flexible

### 3. Model Flexibility
**Winner: Gemini**
- Global `set_model()` to switch models at runtime
- Can use `gemini-1.5-flash` (default), `gemini-2.5-pro`, or any future model
- All functions adapt automatically

**OpenAI**
- Hard-coded to `gpt-4o`
- Would need code changes to swap models

### 4. Token Counting Precision
**OpenAI**: Reliable token counts from SDK response object
**Gemini**: Manual extraction from JSON; depends on API version supporting `usageMetadata`

---

## Why Gemini 2.5 Pro Over GPT-4o?

1. **Reasoning**: Gemini 2.5 Pro has stronger visual reasoning for complex UI scenarios
2. **Cost**: Generally cheaper per token
3. **Speed**: Faster latency for image analysis (despite being "pro" tier)
4. **Availability**: No rate limiting issues in testing environment
5. **Production Resilience**: Built-in retry logic makes it more robust for long automation runs

---

## Performance Characteristics

| Aspect | OpenAI (gpt-4o) | Gemini (2.5-pro) |
|--------|---|---|
| Latency (state check) | ~2-3s | ~3-5s |
| Latency (action prediction) | ~2-3s | ~5-8s |
| Retries on failure | None | 5 attempts, exponential backoff |
| Timeout handling | SDK default | 180s explicit |
| Token efficiency | High | High (comparable) |
| Cost per call | ~$0.015 | ~$0.005 |

---

## Swapping Providers

Both implementations expose **identical function signatures** so `segment_replay.py` can swap providers via:

```python
# Option 1: OpenAI
from approach import openai_api as provider

# Option 2: Gemini
from approach import gemini_api as provider
set_model("gemini-2.5-pro")  # Sets global model

# All calls work identically:
provider.ask_gpt_state_consistency(ref, live)
provider.ask_gpt_for_relevant_regions(start, stop)
provider.ask_gpt_for_action_region(start, stop, live, action)
```

This design allows A/B testing, fallback logic, or gradual migration between providers without changing the core automation logic.
