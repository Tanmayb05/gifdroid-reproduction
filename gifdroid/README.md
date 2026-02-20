# GIFdroid: Automated Replay of Visual Bug Reports for Android Apps

## Watch the video (Click on image✨)
[![Watch the video](figures/youtube.png)](https://www.youtube.com/watch?v=5GIw1Hdr6CE)

## Approach
<p align="center">
<img src="figures/overview.png" width="90%"/> 
</p><p align="center">The overview of GIFdroid consists of three phases, Keyframe Location, GUI Mapping, Execution Trace generation.<p align="center">


GIFdroid is a light-weight image-processing approach to automatically replay the video (GIF) based bug reports for Android apps. GIFdroid consists of three phases, each of which play a crucial role in accomplishing this functionality. Given that GIFdroid was designed and built with extension in mind, each of these phases and each of the component elements of these phases can be extended or substituted to further the functionality of the pipeline as a whole. The intent of this design choice is to allow researchers and developers to customize GIFdroid for future projects or development use cases.

### Keyframe Location
<p align="center">
<img src="figures/timeframe.png" width="70%"/> 
</p><p align="center">Figure 1: An illustration of the Y-Diff similarity scores of consecutive frames in the visual recording.<p align="center">


Note that GUI rendering takes time, hence many frames in the visual recording are showing the partial rendering process. The goal of this phase is to locate keyframes i.e., states in which GUI are fully rendered in a given visual recording.

Inspired by signal processing, we leverage the image processing techniques to build a perceptual similarity score for consecutive frame comparison based on Y-Difference (or Y-Diff), see Figure 1.
Given the consective frame comparision, we identify the keyframe by locating the steady state, where the consecutive frames are similar for a relatively long duration.

### GUI Mapping
Given the sequence of keyframes in the recording, we map the keyframes extracted to states/GUIs within the GUI transitions graph (UTG), hence to infer the actions.
We design an advanced image similarity metric for GUI mapping that first detects the features within pixels and structures using SSIM and ORB, and then compute a combined similarity value.

### Execution Trace generation

<p align="center">
<img src="figures/lcs.png" width="70%"/> 
</p><p align="center">Figure 2: Illustration of the execution trace generation. Index sequence 2,3 indicate two types of defective sequences, i.e., missing {𝐷} and wrong mapping to {𝐵}, respectively.<p align="center">


After mapping keyframes to the GUIs in the UTG, we need to go one step further to connect these GUIs/states into a trace to replay the bug.
However, this process is challenging due to two reasons. First, the extracted keyframe and mapped GUIs may not be 100% accurate, resulting in a mismatch of the groundtruth trace. For example in Figure 2, {𝐷} is missed in the index sequence 2 and the second keyframe is wrongly mapping to {𝐵} in the index sequence 3. Second, different from the uploaded GIF which may start the recording anytime, the recovered trace in our case must begin from the launch of the app.


In this phase, we first generate all candidate sequences in UTG between the app launch to the last keyframe from GIF. By regarding the extracted keyframes as a sequence, our approach then further extracts the Longest Common Subsequence (LCS) between it and all candidate sequences.
The overflow of our approach can be seen in Algorithm 1 in our paper.


## Setup Instructions
### Prerequisites
* Python 3.6.9 installed
    * Other versions are not verified.
    * If none installed yet, can use Anaconda/Miniconda as mentioned below

### Installing Anaconda/Miniconda
* We will use conda to manage python package dependencies.
* We recommend you install Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html) or Anaconda from [here](https://www.anaconda.com/distribution/).
    * select "Add Anaconda to PATH" option during the install (more than one path variable is needed and this option takes care of them all).
* If freshly downloaded, you have python 3.7 or newer. As mentioned earlier, downgrade to python 3.6.9 using 'conda install python=3.6.9'.

### GIFdroid Installation
* Ensure that the environment you are running in is operating with Python 3.6.9.
* Current Option:
    * Clone the repository [here](https://github.com/gifdroid/gifdroid.git), navigate to gifdroid directory, and execute `pip install -r requirements.txt`. Please make sure you have installed all the requirements.

### Execution
* Input requirements:
    * video
    * utg: GUI transition graph in json format depicting the screenshots transitions
    * artifact: screenshots in UTG
* When you are ready to complete the installation, run `python main.py --video=<filename> --utg=<utg.json> --artifact=<folder> --out=<out_filename>`. If no out argument is specified, the default execution.json file is outputted✨.
* A demo of input and output is shown in `<example>` folder
<p align="center">
<img src="figures/response.png" width="100%"/> 
</p><p align="center">Figure: An example of our output, execution trace.<p align="center">
   

## Performance

<p align="center">
<img src="figures/table2.png" width="50%"/> 
</p>

* Accuracy of Keyframe Location
    * Table 2 shows the performance of all approaches. The performance of our method is much better than that of other baselines, i.e., 32%, 106%, 14% boost in recall, precision, and F1-score compared with the best baseline (ILS-SUMM, PySceneDetect). The issues with these baselines are that they are designed for general videos which contain more natural scenes like human, plants, animals etc. However, different from those videos, our visual bug recordings belong to artificial artifacts with different rendering processes. Therefore, considering the characteristics of visual bug recordings, our approach can work well in extracting keyframes.

<p align="center">
<img src="figures/table3.png" width="80%"/> 
</p>

* Accuracy of GUI Mapping
    * Table 3 shows the overall performance of all methods. In contrast with baselines, our method outperforms in all metrics, 85.4%, 90.0%, 91.3% for Precision@1, Precision@2, Precision@3 respectively. We observe that the methods based on structural features perform much better than pixel features due to the reason that the pixel similarity suffers from the scale-invariant as the resolutions for visual recordings varies. Our method that combines SSIM and ORB leads to a substantial improvement (i.e., 9.7% higher) over any single feature, indicating that they complement each other. In detail, ORB addresses the image distortion that causes false GUI mapping considering only SSIM.


<p align="center">
<img src="figures/table4.png" width="50%"/> 
</p>

<p align="center">
<img src="figures/table5.png" width="80%"/> 
</p>

* Performance of Trace Generation
    * Table 4 shows the performance comparison with the baselines. Our method achieves 89.59% sequence similarity which is much higher than that of baselines. Note that due to the strict requirement of input recordings, V2S does not work well in all our datasets, but performs well in our partial dataset with touch indicators. In addition, adding LCS can mitigate the errors introduced in the first two steps in our approach, resulting in a boost of performance from 82.63% to 89.59%. Although applying LCS takes a bit more runtime (i.e., 13.25 seconds on average), it does not influence its real-world usage as it can be automatically run offline.

    * Table 5 shows detailed results of the success rate for each visual recordings, where each app, execution trace (number of steps), and successfully replayed steps are displayed. GIFdroid fully reproduces 82% (50/61) of the visual recordings, signals a strong replay-ability.

<p align="center">
<img src="figures/table6.png" width="80%"/> 
</p>

* User Study 💬 
    * Table 6 shows the experiment result. the experiment group reproduces the visual bug recording much faster than that of the control group (with an average of 171.4 seconds versus 65.0 seconds). In fact, the average time of the control group is underestimated, because three bugs fail to be reproduced within 10 minutes, which means that participants may need more time. In contrast, all participants in the experiment group finish all the tasks within 2 minutes.
    * For more detail of this user study, please see the [website](https://sites.google.com/view/gifdroid).

## Creating a Conda Environment (macOS)

Here are the commands to create a conda environment with Python 3.6.9:

```bash
# Create the environment
conda create -n gifdroid python=3.6.9

# Activate it
conda activate gifdroid

# Install dependencies
pip install -r requirements.txt
```

## UTG File Structure Needed

The `utg.json` file describes the GUI Transition Graph of the app. It is a JSON object with a single `events` array.

### sourceScreenId and destinationScreenId

These are screen state IDs in the UI Transition Graph (UTG). They represent unique UI screens/states observed during app exploration:

- **`sourceScreenId`** — the screen the app was on **before** the action was performed
- **`destinationScreenId`** — the screen the app transitioned to **after** the action

Each event in `utg.json` describes a transition: `screen A --[action]--> screen B`.

```json
{
  "events": [
    {
      "sourceScreenId": "0",
      "destinationScreenId": "1",
      "launch": {
        "action": "android.intent.action.MAIN"
      }
    },
    {
      "sourceScreenId": "1",
      "destinationScreenId": "2",
      "target": {
        "type": "TAP",
        "targetDetails": {
          "className": "android.widget.Button",
          "resourceName": "com.example:id/my_button",
          "contentDescription": "Search"
        }
      }
    },
    {
      "sourceScreenId": "2",
      "destinationScreenId": "3",
      "target": {
        "type": "TYPE_TEXT",
        "enterTextString": "hello",
        "targetDetails": {
          "className": "android.widget.EditText",
          "resourceName": "com.example:id/input_field"
        }
      }
    }
  ]
}
```

### Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `events` | Yes | Top-level array of all GUI transition events |
| `events[].sourceScreenId` | Yes | ID of the source screen (string of an integer, e.g. `"0"`) |
| `events[].destinationScreenId` | Yes | ID of the destination screen (string of an integer, e.g. `"1"`) |
| `events[].launch` | First event only | Present on the app launch event (no `target` needed) |
| `events[].target` | All non-launch events | Describes the user interaction that triggered the transition |
| `events[].target.type` | Yes (if target) | Action type: `"TAP"`, `"TYPE_TEXT"`, etc. |
| `events[].target.targetDetails` | Yes (if target) | Dict of widget info — written as-is to the output trace |

### Notes
* Screen IDs must be strings of integers starting from `"0"` (the initial/launch state).
* The first event must use the `launch` key (no `target`), representing the app being opened.
* The artifact screenshots passed via `--artifact` must be named `artifacts_<N>.png` where `<N>` matches the screen IDs (e.g. `artifacts_1.png`, `artifacts_2.png`).
* Fields like `startTimeSeconds`, `endTimeSeconds`, `executionResult`, and `sequence` are not read by the code and can be omitted.

## Expected File Structure

For each app, organize your inputs as follows:

```
app_<app_name>/
├── app_<app_name>.mp4
├── utg.json
└── artifacts/
    ├── artifacts_1.png
    ├── artifacts_2.png
    └── artifacts_3.png
```

And run with:

```bash
python main.py --video=app_<app_name>/app_<app_name>.mp4 --utg=app_<app_name>/utg.json --artifact=app_<app_name>/artifacts/ --out=execution.json
```

## Artifact Filename Convention

Screenshots in the artifact folder passed via `--artifact` must follow this naming pattern:

```
artifacts_<N>.png
```

Where `<N>` is the integer screen ID matching `sourceScreenId`/`destinationScreenId` in `utg.json`.

### Examples
```
artifacts_1.png
artifacts_2.png
artifacts_3.png
```

### Key points
* Extension must be `.png` — only `*.png` files are loaded from the artifact folder
* Prefix must be exactly `artifacts_` — the code splits on that string to extract the screen ID
* The number must match a screen ID used in `utg.json`
* Screen `0` (the initial/launch state) does not need a screenshot

## Citations
Please consider citing this paper if you use the code:
```
@article{feng2021gifdroid,
  title={GIFdroid: Automated Replay of Visual Bug Reports for Android Apps},
  author={Feng, Sidong and Chen, Chunyang},
  journal={arXiv preprint arXiv:2112.04128},
  year={2021}
}
```

## References
1. [Comixify](https://github.com/maciej3031/comixify)
2. [ILS-SUMM](https://github.com/YairShemer/ILS-SUMM)
3. [Hecate](https://github.com/yahoo/hecate)
4. [PySceneDetect](https://github.com/Breakthrough/PySceneDetect)
5. [V2S](https://gitlab.com/SEMERU-Code-Public/Android/video2scenario/-/tree/master/python_v2s)








====
# Steps

python gifdroid/main.py --video=app_AdAway/app_AdAway.mp4 --utg=app_AdAway/utg.json --artifact=app_AdAway/artifacts/ --out=app_AdAway/execution.json

python gifdroid/main.py --video=app_AntennaPod/app_AntennaPod.mp4 --utg=app_AntennaPod/utg.json --artifact=app_AntennaPod/artifacts/ --out=app_AntennaPod/execution.json

python gifdroid/main.py --video=app_HomeMedkit/app_HomeMedkit.mp4 --utg=app_HomeMedkit/utg.json --artifact=app_HomeMedkit/artifacts/ --out=app_HomeMedkit/execution.json

python gifdroid/main.py --video=app_Jigsaw/app_Jigsaw.mp4 --utg=app_Jigsaw/utg.json --artifact=app_Jigsaw/artifacts/ --out=app_Jigsaw/execution.json

python gifdroid/main.py --video=app_LuxAlarm/app_LuxAlarm.mp4 --utg=app_LuxAlarm/utg.json --artifact=app_LuxAlarm/artifacts/ --out=app_LuxAlarm/execution.json

python gifdroid/main.py --video=app_PortAuthority/app_PortAuthority.mp4 --utg=app_PortAuthority/utg.json --artifact=app_PortAuthority/artifacts/ --out=app_PortAuthority/execution.json

python gifdroid/main.py --video=app_SimpleNotes/app_SimpleNotes.mp4 --utg=app_SimpleNotes/utg.json --artifact=app_SimpleNotes/artifacts/ --out=app_SimpleNotes/execution.json

python gifdroid/main.py --video=app_WifiAnalyzer/app_WifiAnalyzer.mp4 --utg=app_WifiAnalyzer/utg.json --artifact=app_WifiAnalyzer/artifacts/ --out=app_WifiAnalyzer/execution.json


====

# Changes made to gifdroid repo

- add logs in main.py
- change mapping.py to ignore pngs in artifact dir other than artifact_<number>.png format
- Event 207 is a terminal roboscriptFinished event with no screen IDs. The fix is in trace.py — read_graph needs to skip events that don't have both sourceScreenId and destinationScreenId. Same fix needed in main.py's read_graph_with_action
- knnMatch returns an empty list when ORB finds no keypoints in a frame (or a screenshot), so len(matches) is 0. The fix is to return 0.0 (no match) when there are no matches, and also handle the case where ORB finds no descriptors at all (des can be None) mapping.py
===
