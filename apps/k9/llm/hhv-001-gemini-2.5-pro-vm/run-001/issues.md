# Issues: k9 hhv-001 run-001

## Video vs memory.md gaps

Video (9.46s, frames checked at 0.5s intervals): Unified Inbox → tap search icon (~1s, keyboard appears) → type "Hi" (~2s) → tap keyboard search/submit (~4s) → search results screen "Hello World" from ezioaltair1524@gmail.com (~7-9s) → back to inbox implied by end of clip.

memory.md's 4-step narrative matches this closely: tap search icon (1s), type "Hi" (2s), tap keyboard search button (4s), back (7s). No hallucination or fabrication found — **Stage 1 memory generation is accurate for this run**, unlike the k9 hhv-002 case. Video is short (9.46s) and the task is a single linear flow, which likely helped: less opportunity for the model to fill gaps with a templated narrative, and the single search-icon tap and text field are visually unambiguous even at 1fps sampling.

One soft note: the actual keyboard "search submit" affordance is not a clearly separate visible icon in the extracted frames (f_008, ~4s) — the keyboard shown is a plain QWERTY without an obviously distinct magnifying-glass key in view. Memory.md's phrase "tapped the magnifying glass icon on the keyboard" is a reasonable interpretation but slightly overspecifies what's actually visible; this ambiguity becomes the root cause of the Stage 2 gap below.

## memory.md vs device-automation gap

Automation executed **9 steps**, more than double memory.md's claimed 4 (`apps/k9/llm/hhv-001-gemini-2.5-pro-vm/run-001/device-automation/steps/`, confirmed via automate.log: `Run complete: app=k9 ... steps=9 status=done`).

**Root cause:** at step 3, the on-device screenshot (`step_002_post.png`) after typing "Hi" shows the search field with text entered but **no keyboard visible at all** — a blank white area below the search bar. This differs from what the video showed at the equivalent moment (keyboard present). The LLM's own reasoning at step 3 states this explicitly:

> "The video summary specifies this was done by tapping the search button on the keyboard. However, the keyboard is not visible in the current screenshot, and there is no corresponding UI element to interact with." (confidence 0.6, action=wait)

This is a genuine **environment divergence between Stage 1 (recorded video) and Stage 2 (live automation)** — not a model hallucination. The real device's IME (keyboard) auto-dismissed or never rendered at the point the automation screenshot was taken, likely due to timing differences between the human-recorded video (keyboard visible mid-typing) and the automation's screenshot-after-action capture (keyboard already gone/dismissed by the time the screenshot was taken). With no matching UI element for memory.md's step 3, the LLM improvised:
- Step 3: wait (guessing search might auto-execute)
- Step 4: press_back (screen still blank, assumes flow is stuck/complete)
- Step 5-6: re-tap search icon + re-type "Hi" (effectively restarting the whole flow from step 1)
- Step 7: wait again
- Step 8: press_back again
- Step 9: done (landed back on Unified Inbox, judged task complete)

Net effect: the search-icon-tap + type-text sequence was executed twice, and steps 3-4/7-8 of the automation are pure recovery/guessing behavior substituting for a UI element (keyboard search button) that Stage 2's screenshot never captured. No pipeline bug — this is an IME-timing/screenshot-timing mismatch between the two capture methods (human video vs. automated `capture_screenshot()` in [device.py](../../../../../src_llm/device.py)).

**Suggested fix:** add a short delay or explicit "wait for keyboard idle" check after `type_text` actions before capturing the next screenshot, so the automation's view of the screen matches what a human would see mid-interaction (keyboard still up, search button visible) rather than a post-dismiss state.
