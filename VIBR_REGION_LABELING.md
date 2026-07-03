# ViBR Region Labeling Process

## Overview
ViBR labels UI regions (interactive elements) on emulator screenshots by parsing Android XML dumps and drawing visual indicators. The labeled images are saved as `*_labeled.png` artifacts and used for LLM-based region analysis.

## Architecture

```
Device Screenshot + XML Dump
         ↓
   Parse XML → Identify Elements
         ↓
   Filter & Deduplicate
         ↓
   Draw Labels on Screenshot
         ↓
   Save as *_labeled.png
```

## Step-by-Step Process

### 1. **Get Device XML Dump** (`segment_replay.py:453`)
```python
xml_str = device.get_ui_xml()
```
- Uses ADB to pull the current UI hierarchy from the Android device
- Returns XML with element attributes: `bounds`, `clickable`, `text`, `resource-id`, etc.
- Example bounds format: `[x1,y1][x2,y2]` e.g., `[100,200][300,400]`

### 2. **Parse XML & Extract Elements** (`input_formatter.py:75-126`)
```python
elements = parse_xml_string(xml_str, bound_margin=10, min_cent_dist=20, clickable_only=True)
```

**Filtering logic:**
- **Start**: Parse all elements from XML with valid bounds
- **Skip invalid**: Remove elements with zero bounds or parse errors
- **Deduplicate**: Skip overlapping elements (overlap detection with margin/distance checks)
- **Filter by interaction**:
  - If `clickable_only=True`: Keep only elements where `clickable="true"`
  - If `clickable_only=False`: Keep elements with either text content OR resource-id (non-empty)

**Result**: Ordered list of `AndroidElement` objects, each with:
- `path`: XPath-like hierarchy (e.g., `android.widget.LinearLayout[0].android.widget.Button[2]`)
- `bounds`: `(x1, y1, x2, y2)` - top-left and bottom-right corners
- `text`: Display text or label from the element
- `center`: Computed center `((x1+x2)//2, (y1+y2)//2)`

### 3. **Handle Low Element Count** (`segment_replay.py:454-456`)
```python
if len(elements) <= 5:
    elements = parse_xml_string(xml_str, bound_margin=10, min_cent_dist=20)
```
If only 5 or fewer clickable elements found, parse again without the `clickable_only` filter to get more context elements.

### 4. **Draw & Label Screenshot** (`input_formatter.py:129-184`)
```python
label_screenshot(screenshot_path=live_path, elements=elements, name="step_0_labeled")
```

**Visual rendering process:**

1. **Load screenshot** as OpenCV image (BGR format)
2. **Draw rectangles for each element**:
   - Size is proportional but at least `MIN_ELEMENT_DIM=50` pixels
   - Size = `max(50, element_dimension / 5)` 
   - Color: **Purple** `(160, 32, 240)`
   - Thickness: 4 pixels
3. **Blend overlay** with original (80% overlay, 20% original) for transparency
4. **Draw index labels** (0, 1, 2, ...) in purple text
   - Text placed above rectangle (or below if too close to top)
   - Font: Duplex, scale 1.0, thickness 2
5. **Save** as PNG to artifacts directory

### 5. **Region Index Mapping** (`segment_replay.py:470-478`)
```python
for idx, e in enumerate(elements):
    region = {
        "index": idx,  # This is the number drawn on the label
        "center": e.center,
        "box": list(e.bounds),
        "phrase": e.text if e.text else "unknown element",
    }
```

The region **index matches the label number** drawn on the screenshot. This allows the LLM to reference regions by their visible numeric labels.

## Visual Example

**Screenshot before labeling:**
```
┌─────────────────────────┐
│ Baker's Percentage Calc │
│                         │
│  ┌─────────────────┐    │
│  │ + Add Recipe    │    │  ← Element at index 0 (clickable)
│  └─────────────────┘    │
│                         │
│  ┌──────────────────────┐│
│  │ Recipe List Item 1   ││  ← Element at index 1
│  └──────────────────────┘│
└─────────────────────────┘
```

**Screenshot after labeling (with boxes, labels, and blend):**
```
┌─────────────────────────┐
│ Baker's Percentage Calc │
│ 0                       │
│  ┌────[0]──────────┐    │  Purple box with "0" label
│  │ + Add Recipe    │    │
│  └─────────────────┘    │
│                         │
│ 1                       │
│  ┌────[1]──────────────┐│  Purple box with "1" label
│  │ Recipe List Item 1   ││
│  └──────────────────────┘│
└─────────────────────────┘
```

## How LLM Uses Labels

1. **View labeled screenshot**: LLM sees the image with visible numeric labels
2. **Region selection**: LLM returns `"region": 0` (or any index it sees)
3. **Position resolution**: Code maps `region 0` → `elements[0].center` → `(x, y)` coordinates
4. **Action execution**: ADB executes tap at `(x, y)`

## Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `bound_margin` | 10 | Overlap detection margin (pixels) |
| `min_cent_dist` | 20 | Minimum center-to-center distance for overlap |
| `MIN_ELEMENT_DIM` | 50 | Minimum label box size (pixels) |
| `RESIZE_FACTOR` | 5 | Scale factor for element box (element_size / 5) |
| `CV2_ALPHA` | 0.8 | Overlay transparency (80% colored) |

## Artifacts Generated

- **`step_N_labeled.png`**: Screenshot with all parsed elements labeled with numeric indices
- **`step_N_dino.png`**: DINO grounding output (separate from XML-based labeling)
- **`step_N_relevant_regions.png`**: Subset of elements filtered by LLM as relevant

## Related Files

- [`input_formatter.py`](src_ViBR/approach/input_formatter.py): Core labeling logic
- [`segment_replay.py:452-463`](src_ViBR/approach/segment_replay.py#L452-L463): Integration point
- [`adb_device_controller.py`](src_ViBR/approach/adb_device_controller.py): XML dump method
