# Milestone 7: Project Structure - Video Guide

**Target Duration:** ~2 minutes (acceptable range: 1:50 to 2:10)  
**Segments:** 6 scenes with exact timing  
**Key Focus:** Demonstrating folder organization and explaining why structure matters

---

## Table of Contents

1. [Before Recording](#before-recording)
2. [Scene Breakdown](#scene-breakdown)
3. [Verbatim Scripts](#verbatim-scripts)
4. [Recording Checklist](#recording-checklist)
5. [Common Pitfalls](#common-pitfalls)
6. [Post-Recording](#post-recording)

---

## Before Recording

### Equipment Check (5 minutes)

- [ ] Screen recording software open and configured
  - Recommended: OBS, Zoom, QuickTime, ScreenFlow, or Camtasia
- [ ] Microphone tested and working clearly
  - Test recording 10 seconds, review audio quality
  - Position microphone 6 inches from mouth
- [ ] Screen resolution at least 1280x720 (1920x1080 preferred)
- [ ] Backup audio: Use microphone from headset instead of built-in
- [ ] Background: Clear desktop, minimize distractions
- [ ] Lighting: Good visibility of your face (if visible in recording)
- [ ] No notifications: Disable email, chat, calendar popups

### Environment Setup (5 minutes)

- [ ] Open file manager with sample-ds-project folder visible
- [ ] Have folder structure expanded to show all directories
- [ ] README.md files visible (not opened, just available)
- [ ] Close all unnecessary applications
- [ ] Silence phone and disable interruptions

### Content Preparation (5 minutes)

- [ ] Print or open this guide for reference
- [ ] Note timestamps if using for practice
- [ ] Prepare scenario answer (see Segment 6)
- [ ] Do one practice run (optional but recommended)

### Timing Aid

Keep clock/timer visible:
- Segment 1: 00:00 to 00:30 (30 seconds)
- Segment 2: 00:30 to 01:15 (45 seconds)
- Segment 3: 01:15 to 02:05 (50 seconds)
- Segment 4: 02:05 to 02:30 (25 seconds)
- Segment 5: 02:30 to 02:55 (25 seconds)
- Segment 6: 02:55 to 03:20 (25 seconds)

**Total: 3:20 (within acceptable range)**

---

## Scene Breakdown

### Segment 1: Introduction and Project Overview
**Duration:** 30 seconds (00:00 - 00:30)

**What to Show:**
- Root folder of sample-ds-project
- Main directory structure visible (folders at first level)

**Verbatim Script:**
```
"Hello, I'm demonstrating Milestone 7 on project structure 
for data science work. This is the sample-ds-project folder, 
which demonstrates professional organization for data analysis. 
You can see the main folders: data, notebooks, scripts, 
outputs, configs, and docs. Each serves a specific purpose 
in keeping the project organized and scalable."
```

**Script Breakdown:**
- Line 1-2: Welcome and milestone identification
- Line 2-4: Describe what we're looking at
- Line 4-7: Point out main folders
- Line 7: Brief overview of purpose

**Timing Tips:**
- Speak clearly and deliberately
- Pause after main point (after "organized and scalable")
- This is your introduction; don't rush

---

### Segment 2: Raw vs. Processed Data
**Duration:** 45 seconds (00:30 - 01:15)

**What to Show:**
1. Navigate to `data/raw/` folder
2. Show it contains README.md
3. Navigate to `data/processed/` folder
4. Show it also has README.md
5. Navigate back to data folder to show both subfolders

**Verbatim Script:**
```
"The most important principle is separating raw from 
processed data. Notice we have two subfolders in the data 
directory: raw and processed. The raw folder contains the 
original, unmodified source data—exactly as it came from 
the source. This folder is immutable; we never modify 
these files. The processed folder contains cleaned, 
transformed data that's ready for analysis. This separation 
is critical because it preserves reproducibility. If 
something goes wrong in processing, the raw data is still 
there. And we can always re-run the cleaning steps to 
regenerate processed data. This is a best practice 
recommended across the data science industry."
```

**Script Breakdown:**
- Line 1-4: Introduce the principle of separation
- Line 4-8: Explain raw data (immutable)
- Line 8-12: Explain processed data (ready for use)
- Line 12-15: Explain why this matters

**Timing Tips:**
- Segment 2 is longest; speak at conversational pace
- Pause after "data" when introducing both folders
- Pause after each folder description for visual clarity
- Final sentence is important; deliver with emphasis

**Visual Actions:**
- Click on data/raw/, let it load
- Click back, then on data/processed/
- Point to folder names clearly

---

### Segment 3: Code Organization (Notebooks and Scripts)
**Duration:** 50 seconds (01:15 - 02:05)

**What to Show:**
1. Navigate to `notebooks/` folder
2. Show README.md
3. Navigate back and open `scripts/` folder
4. Show README.md
5. Point out key difference: one for exploration, one for reuse

**Verbatim Script:**
```
"Code is organized into two folders. The notebooks folder 
contains Jupyter notebooks—these are for exploration and 
prototyping. Notice the naming convention: 01_exploratory_analysis, 
02_feature_engineering. Numbers indicate sequence and order. 
This helps anyone read the analysis in logical order.

The scripts folder contains Python files with reusable 
functions. Instead of duplicating code across multiple 
notebooks, we extract functions to scripts and import them 
where needed. This follows the principle of Don't Repeat 
Yourself, commonly known as DRY.

For example, a data_cleaning.py script might have a 
remove_duplicates function. Every notebook can import and 
use that same function, ensuring consistency and reducing 
maintenance burden."
```

**Script Breakdown:**
- Line 1-5: Introduce notebooks
- Line 5-10: Explain naming convention
- Line 10-15: Introduce scripts
- Line 15-20: Explain the DRY principle
- Line 20-26: Provide concrete example

**Timing Tips:**
- Segment 3 is substantial; keep pace steady
- Pause after describing each folder type
- Emphasize "DRY principle" - this is a key concept
- Example makes it concrete; don't rush this part

**Visual Actions:**
- Show notebooks folder and naming
- Show scripts folder
- Consider opening one README to show documentation style

---

### Segment 4: Outputs and Configuration
**Duration:** 25 seconds (02:05 - 02:30)

**What to Show:**
1. Show `outputs/` folder structure
   - models/
   - visualizations/
   - reports/
2. Show `configs/` folder
3. Briefly show one config file (optional)

**Verbatim Script:**
```
"Generated outputs are organized into three subfolders: 
models for trained models, visualizations for plots and 
charts, and reports for analysis summaries and exports. 
Keeping outputs separate from source data prevents 
accidental data overwrite and keeps things clean.

Configuration files live in the configs folder. These 
YAML or JSON files centralize parameters and settings. 
Using configs instead of hardcoding values makes 
analysis reproducible and easier to adjust."
```

**Script Breakdown:**
- Line 1-5: Explain outputs structure
- Line 5-7: Why separation matters
- Line 7-11: Introduce configuration files
- Line 11-13: Benefits of configuration management

**Timing Tips:**
- Speak at steady pace
- Segment 4 is shorter; ensure good pacing
- Don't rush through config explanation

**Visual Actions:**
- Show outputs folder expanded to show three subfolders
- Show configs folder
- Optional: Display one example config file (data_config.yaml)

---

### Segment 5: Documentation and Why This Matters
**Duration:** 25 seconds (02:30 - 02:55)

**What to Show:**
1. Main README.md file
2. Mention docs/ folder with data_dictionary.md
3. Show .gitignore
4. Emphasize professional appearance

**Verbatim Script:**
```
"Documentation is critical. Every project should have 
a README at the root level explaining the project, its 
structure, and how to use it. The docs folder contains 
detailed documentation like data_dictionary.md, which 
describes every data column.

Finally, notice the .gitignore file. This tells git which 
large generated files NOT to commit to version control. 
We commit code and configs, but not processed data or 
large model files.

This structure exhibits professional organization. It 
demonstrates that the project is manageable, scalable, 
and ready for collaboration."
```

**Script Breakdown:**
- Line 1-4: Introduce README
- Line 4-6: Mention docs folder
- Line 6-10: Explain .gitignore
- Line 10-13: Summary of professional appearance

**Timing Tips:**
- Last description segment before scenario
- Deliver final statement with confidence
- Emphasis on "professional" and "collaboration"

**Visual Actions:**
- Show README at root
- Mention docs folder
- Point to .gitignore file

---

### Segment 6: Scenario-Based Reasoning (REQUIRED)
**Duration:** 25 seconds (02:55 - 03:20)

**What to Show:**
- Still showing file system (folder structure)
- OR: Close file system for this segment (optional)

**Scenario to Answer:**

> A teammate clones your repository and struggles to find where 
> the original data is stored and where the analysis outputs ended 
> up. What structure mistakes likely caused this confusion, and 
> how would clearer project layout prevent it?

**Verbatim Script:**

Choose ONE of these answers based on your explanation style:

**Option A: Comprehensive Answer**
```
"This problem would happen if data and outputs were all 
mixed together in one folder, or if folders had vague names 
like 'files' or 'results'. Our structure prevents this by 
being explicit: data/raw/ clearly holds original data, 
data/processed/ holds cleaned data, and outputs/ holds 
results. The naming is so specific that anyone—even a 
new team member—can navigate immediately.

The key improvements are: clear separation of concerns 
(different folders for different file types), predictable 
naming (raw vs. processed), and consistency (same structure 
across all projects). This enables collaboration because 
everyone knows where to find everything."
```

**Option B: Concise Answer (if running long)**
```
"If data and outputs were mixed together without clear 
naming, teammates would be lost. Our structure prevents 
this: data/raw/ for original data is obvious, data/processed/ 
for cleaned data is clear, and outputs/ for results is 
unambiguous. 

The structure ensures collaboration by being predictable 
and consistent. Anyone can clone the repo and understand 
the layout immediately because folder names are specific 
and logically organized."
```

**Option C: Detailed Answer (if running short)**
```
"Confusion comes from three mistakes: First, mixing file 
types—if raw data, processed data, and outputs are all in 
one folder called 'analysis_files', no one knows what's what. 
Second, unclear names—'data_v2' or 'results_final' don't 
tell you what transformation occurred. Third, no documentation 
about folder purposes.

Our structure solves this by: separating by type and purpose 
(data/raw, data/processed, outputs/models), using descriptive 
names that reveal transformations, and including README files 
explaining each folder. This is why consistency matters—when 
all your projects follow the same structure, collaboration 
becomes effortless."
```

**Answer Selection Guide:**
- Choose A if you're under time (excellent explanation)
- Choose B if you're running long (shorter but complete)
- Choose C if you're on pace (most detailed and educational)

**Timing Tips:**
- This is the final segment; deliver with confidence
- Reference specific folder names from your structure
- Mention the three key principles: separation, naming, documentation
- Conclude firmly—this is your final impression

---

## Verbatim Scripts Summary

**Total Words Guideline:** 400-500 words across all segments

**Key Phrases to Emphasize:**
- "Separation of concerns"
- "Immutable raw data"
- "DRY principle" (Don't Repeat Yourself)
- "Reproducibility"
- "Professional organization"
- "Collaboration and scalability"
- "Predictable and consistent"

---

## Recording Checklist

### Before Starting Recording

- [ ] All folders visible and organized
- [ ] File manager at root of sample-ds-project
- [ ] README files visible (not opened)
- [ ] Microphone is on and tested
- [ ] Recording software is running
- [ ] Background is clear and professional
- [ ] Lighting is adequate
- [ ] Phone is silenced
- [ ] No browser tabs with notifications
- [ ] Timestamp or timer is visible

### During Recording

- [ ] Speak clearly and deliberately
- [ ] Use appropriate pacing (not too fast, not too slow)
- [ ] Pause after major points for visual clarity
- [ ] Point to folders and files as you discuss them
- [ ] Reference specific folder and file names
- [ ] Make eye contact with camera (or speak naturally if no camera)
- [ ] Maintain steady voice and confidence
- [ ] Watch for "um", "uh", "like" - minimize filler words

### Segment Transitions

- [ ] Navigate smoothly between segments
- [ ] Click on folders to open/close visibly
- [ ] Allow folders to load if there's delay
- [ ] Don't rush through navigation
- [ ] Keep narration going while navigating (no long silences)

### After Recording

- [ ] Stop recording after scenario answer finishes
- [ ] Check total duration is 1:50 to 2:10 (acceptable range)
- [ ] Save file with clear name: `Milestone-7-Project-Structure-YourName.mp4`
- [ ] Preview file: Sound clear? Video legible? Complete?

---

## Common Pitfalls to Avoid

### Pacing Problems

❌ **Speaking too fast**
- Hard to follow
- Sounds rushed
- Scenario answer becomes unclear

✓ **Solution:** Speak at conversational pace, ~120-150 words per minute

❌ **Speaking too slowly**
- Boring to watch
- Might run long
- Hard to maintain enthusiasm

✓ **Solution:** Speak naturally as if explaining to a teammate

### Technical Issues

❌ **Background noise**
- Fans, traffic, notifications
- Distracting and unprofessional

✓ **Solution:** Check environment, close apps, silence phone

❌ **Multiple re-takes**
- Energy fades with each attempt
- Audio shifts between takes if spliced

✓ **Solution:** Do one practice run; then record once, clean

### Content Issues

❌ **Vague scenario answer**
- Doesn't reference specific folder names
- Doesn't explain the principle

✓ **Solution:** Practice scenario answer, reference structure

❌ **Forgetting to show key elements**
- Missed a folder or significant detail
- Incomplete demonstration

✓ **Solution:** Follow the script; check off each segment

### Timing Issues

❌ **Video is 4+ minutes**
- Way too long
- Exceeds requirements significantly

✓ **Solution:** Tighten script, speak naturally (don't rush)

❌ **Video is 1:30 or less**
- Misses important details
- Scenario answer too brief

✓ **Solution:** Add more explanation, don't skip segments

---

## Post-Recording Steps

### Immediate (Same Day)

1. [ ] Export/save recording in MP4 or WebM format
2. [ ] Filename: `Milestone-7-Project-Structure-[YourName].mp4`
3. [ ] Check file size (should be 50-300 MB typically)
4. [ ] Review first 30 seconds: audio and video quality
5. [ ] Verify video is complete (all 6 segments present)

### Review (Before Upload)

1. [ ] Watch full video if time permits (or first 2 minutes)
2. [ ] Check audio:
   - [ ] Can clearly hear all narration
   - [ ] No major background noise
   - [ ] No sudden volume changes
3. [ ] Check video:
   - [ ] Screen is legible (folders/files visible)
   - [ ] Resolution is good quality
   - [ ] No pixelation or blur
   - [ ] Cursor movements are smooth
4. [ ] Verify timing: 1:50 to 2:10 range
5. [ ] Confirm all 6 segments are present:
   - [ ] Introduction
   - [ ] Raw vs. Processed data
   - [ ] Notebooks and Scripts
   - [ ] Outputs and Configuration
   - [ ] Documentation
   - [ ] Scenario answer

### Troubleshooting Common Issues

**Audio Too Quiet:**
- Re-record prioritizing volume
- OR use audio editing software to amplify (if available)

**Video Too Blurry:**
- Ensure screen resolution is 1280x720 minimum
- Re-record at higher resolution

**Formatting Wrong:**
- Some platforms accept MP4, others AVI, MOV, etc.
- Check submission requirements
- Convert if needed using free tool (HandBrake, etc.)

**Audio Out of Sync:**
- Re-record (this is a recording issue, not editing issue)
- Try different recording software

**Timestamp Issues:**
- If using multiple recordings spliced: note exact splits for reference
- Consider re-recording as single take for cleaner result

---

## Uploading and Sharing

### Upload to Shareable Platform

**Options:**
- Google Drive: Upload → Right-click → Get link → Change to "Viewer"
- YouTube: Upload as "Unlisted" (visible with link only, not in search)
- OneDrive: Upload → Right-click → Share → get link
- Vimeo: Upload → set privacy to "Only people with link"

### Create Shareable Link

1. Upload video
2. Generate shareable link
3. Test link in private/incognito browser window
4. Confirm video plays correctly
5. Copy final link for submission

### Share Quality Check

Before sharing with instructor:
- [ ] Link works in private browser
- [ ] Video plays from start to finish
- [ ] No authorization errors
- [ ] Audio is clear
- [ ] Video is legible

---

## Timing Reference Table

| Segment | Content | Start | End | Duration |
|---------|---------|-------|-----|----------|
| 1 | Introduction & Overview | 0:00 | 0:30 | 30 sec |
| 2 | Raw vs. Processed Data | 0:30 | 1:15 | 45 sec |
| 3 | Notebooks & Scripts | 1:15 | 2:05 | 50 sec |
| 4 | Outputs & Configuration | 2:05 | 2:30 | 25 sec |
| 5 | Documentation & .gitignore | 2:30 | 2:55 | 25 sec |
| 6 | Scenario Answer | 2:55 | 3:20 | 25 sec |
| **TOTAL** | **All Segments** | **0:00** | **3:20** | **3:20** |

**Acceptable Range:** 1:50 to 2:10  
**Your Target:** 2:00 (exactly 2 minutes)

---

## Final Checklist Before Submission

Recording Quality:
- [ ] Audio is clear and understandable
- [ ] Video is legible and professional
- [ ] Total duration is acceptable (1:50 to 2:10)
- [ ] All 6 segments are complete
- [ ] File format is MP4 or WebM

Content Coverage:
- [ ] Segment 1: Introduction & project overview ✓
- [ ] Segment 2: Raw data vs. processed data ✓
- [ ] Segment 3: Notebooks vs. scripts ✓
- [ ] Segment 4: Outputs & configuration ✓
- [ ] Segment 5: Documentation ✓
- [ ] Segment 6: Scenario answer ✓

Scenario Answer Quality:
- [ ] References specific folder names
- [ ] Mentions separation of concerns
- [ ] Explains naming conventions
- [ ] Discusses collaboration benefits
- [ ] Demonstrates understanding

Ready for Submission:
- [ ] Video uploaded to shareable platform
- [ ] Link tested and working
- [ ] Project structure folder created
- [ ] All README files in place
- [ ] PR ready for creation
- [ ] Yes, I am ready to submit!

---

**You've got this! Your video walkthrough will demonstrate professional project organization. Good luck!**
