# MILESTONE 8: VIDEO GUIDE - ORGANIZING RAW DATA, PROCESSED DATA, AND OUTPUT ARTIFACTS
Comprehensive Script and Recording Instructions

---

## QUICK REFERENCE

**Video Duration:** ~2 minutes (acceptable range: 1:50 - 2:10)

**Required Content:**
1. Overview and why organization matters (20s)
2. Raw data protection demonstration (30s)
3. Processed data organization explanation (30s)
4. Output artifacts organization (20s)
5. Scenario question answer (15s)
6. Closing / key takeaways (5s)

**Key Requirement:** Answer the scenario question in depth (critical for scoring)

**Total Time: ~2 minutes**

---

## PART 1: EQUIPMENT CHECKLIST

Before Recording:

### Hardware
- [ ] Recording device (computer, phone, or camera)
- [ ] Microphone (built-in or external)
- [ ] Screen capture software or camera set up
- [ ] Quiet, well-lit environment
- [ ] Cup of water nearby

### Software
- [ ] Screen recording software ready
  * Windows: OBS Studio, Camtasia, or QuickTime
  * Mac: QuickTime Player app ⌘+Shift+5
  * Linux: OBS Studio
- [ ] Backup backup of project files
- [ ] Files organized and visible

### Project Preparation
- [ ] Terminal/command prompt ready
- [ ] File explorer showing your project structure
- [ ] Text editor with your guide ready
- [ ] Sample files visible (at least 5-10)

### Network/Account
- [ ] GitHub repo accessible
- [ ] Project folder cloned/opened
- [ ] All terminal paths set correctly
- [ ] Internet stable

### Audio Quality
- [ ] Check audio levels (should be clear, not too quiet or loud)
- [ ] Eliminate background noise (close tabs, silence notifications)
- [ ] Test microphone level before recording: "Testing 1-2-3"

---

## PART 2: VIDEO SCRIPT - SEGMENT BY SEGMENT

### SEGMENT 1: INTRODUCTION (20 seconds)

**Objective:** Explain why data organization matters and what you're showing

**Script (read verbatim):**

---

[Camera shows: You at your screen, project folder visible in background]

"Hi, I'm demonstrating Milestone 8: Organizing Data Responsibly.

When working on a data science project, how you organize data can make or break 
the success of your analysis. In the next two minutes, I'll show you the three 
critical stages of data organization:

First, protecting your raw data so it can never be accidentally modified.

Second, maintaining clean processing pipelines that track every transformation.

And third, organizing output artifacts so they're easy to find and regenerate.

Let's start by looking at why this matters."

[Transition: Click to show project folder]

---

**Timing:** 20 seconds  
**Key Points to Emphasize:** Three stages, protection, tracking, organization

---

### SEGMENT 2: RAW DATA PROTECTION (30 seconds)

**Objective:** Show raw data folder and explain immutability principle

**Script:**

---

[Camera shows: File explorer with data/raw/ folder open]

"Here's my data/raw folder. This is where all original data lives - completely 
untouched from the source.

[Click: Open data/raw/README.md in text editor]

In my README, I explain the Sacred Rule: Never modify raw data.

[Read from screen while pointing:]

'Why is raw data immutable?
If raw data is corrupted, I have no way to reproduce my results. No audit trail. 
No backup. I lose everything.'

[Click: Show data/raw/DATA_SOURCES.md]

Here's my data sources documentation. It answers:
- Where each file came from (Shopify API, CRM database, etc.)
- When it was exported
- How many records
- How to re-export if needed

[Point to specific lines]

For example: 'sales_transactions_raw.csv - Source: Shopify API - Date received: 
2024-01-15 - Total records: 250,000'

This way, any teammate can understand the data immediately, and I have proof of 
the original state."

[Transition: Click to data/processed/ folder]

---

**Timing:** 30 seconds  
**Key Points:** Immutability, documentation, traceability, team understanding

---

### SEGMENT 3: PROCESSED DATA ORGANIZATION (30 seconds)

**Objective:** Show processing pipeline with naming conventions and metadata

**Script:**

---

[Camera shows: File explorer with data/processed/ folder open]

"In my data/processed folder, I have the output of my cleaning pipeline.

[Show files: sales_cleaned.csv, customer_features.csv, train_set.csv, test_set.csv]

Notice the clear naming: Each file name tells you what was done to it.

sales_cleaned - Shows duplicates were removed and cleaned
customer_features - Shows features were engineered  
train_set and test_set - Show data was split for modeling

[Click: Open one _metadata.txt file]

For each processed file, I created a metadata file documenting:

[Read key sections aloud:]

'Processing Steps:
1. Loaded 250,000 raw records
2. Removed 2 duplicate rows  
3. Filled 18 null values with median
4. Result: 248,500 clean records'

[Point to changes section]

'Changes: 20 records affected (0.008% of total)'

[Point to reproducibility section]

'Reproducibility: Can regenerate by running python scripts/clean_sales_data.py'

This metadata is the audit trail. It answers: Where did this data come from? 
What was done to it? And can we reproduce it?

The answer is: Yes, we can regenerate this anytime."

[Transition: Click to outputs/ folder]

---

**Timing:** 30 seconds  
**Key Points:** Clear naming, metadata, traceability, reproducibility, audit trail

---

### SEGMENT 4: OUTPUT ORGANIZATION (20 seconds)

**Objective:** Show how outputs are organized by purpose

**Script:**

---

[Camera shows: File explorer with outputs/ folder open]

"Now let's look at outputs. This is where results live - models, visualizations, 
and reports.

[Click: outputs/models/]

Models folder contains trained ML models:
- customer_segmentation_kmeans.pkl
- purchase_prediction_xgboost.pkl

Each with metadata explaining when trained, accuracy, features used.

[Click: outputs/visualizations/]

Visualizations folder contains charts:
- sales_trend_2024.png
- customer_segments.png  
- feature_importance.png

High resolution (300 DPI) ready for presentations.

[Click: outputs/reports/]

Reports folder contains analysis summaries:
- sales_analysis_2024.html
- model_evaluation_summary.xlsx
- forecast_q1_2024.csv

Organized by purpose, not by date. Easy to find what you need.

The key: These outputs are disposable. I can regenerate them anytime 
by running my scripts again. They're not precious - they're transparent."

[Transition: Switch to terminal window]

---

**Timing:** 20 seconds  
**Key Points:** Organization by purpose, types of artifacts, reproducibility, transparency

---

### SEGMENT 5: SCENARIO QUESTION ANSWER (15 seconds)

**Objective:** Answer the assigned scenario deeply and connect back to concepts

**Scenario Reminder:**
> "A teammate cannot reproduce your results because the raw data appears to be altered
> and outputs are mixed with input files. What data organization mistakes likely caused this,
> and how would separating raw, processed, and output data prevent the issue?"

**Script:**

---

[Camera shows: You explaining, gestures to screen]

"Here's the scenario: A teammate cannot reproduce results because raw data looks 
altered and outputs are mixed with inputs. What went wrong?

[Pause for emphasis]

This project made three critical mistakes:

Mistake 1: Raw data was modified.
[Point to screen or write on whiteboard:]
If the raw CSV was edited in Excel and saved, the original is gone. There's no 
way to verify what the data actually was. That's why we keep raw data read-only 
and immutable.

Mistake 2: No separation of concerns.
Files were mixed together:
- Both input data and output models in the same folder
- No clear distinction between stages
- Teammate couldn't tell what was source vs. result

Mistake 3: No documentation.
Without metadata files, the teammate couldn't see:
- What transformations were applied
- What the audit trail was
- How to regenerate outputs

[Speak directly to solution:]

By separating: Raw → Processed → Outputs, each in its own folder:
- Raw data is protected and immutable
- Processing pipeline is transparent and documented
- Outputs are clearly organized and regenerable
- Teammate can reproduce everything

This structure takes 5 minutes to set up and saves hours of confusion later."

[Transition: Heading to closing]

---

**Timing:** 15 seconds  
**Key Points:** 
- Three mistakes (raw modified, mixed files, no documentation)
- How separation prevents issues
- Reproducibility and team trust
- ROI of good organization

---

### SEGMENT 6: CLOSING & KEY TAKEAWAYS (5 seconds)

**Objective:** Summarize key learning and wrap up

**Script:**

---

[Camera shows: You looking at camera directly]

"Data organization is not about rules for their own sake.

It's about building trust: 
- Trust that the data is authentic
- Trust that we can reproduce results  
- Trust that teammates understand the work

Three simple folders - raw, processed, outputs - combined with clear naming 
and complete documentation, unlock that trust.

That's Milestone 8. Thanks for watching."

[Transition: End]

---

**Timing:** 5 seconds  
**Key Points:** Trust, reproducibility, simplicity

---

## PART 3: COMPLETE TIMING BREAKDOWN

| Segment | Duration | Cumulative | Notes |
|---------|----------|-----------|-------|
| 1. Introduction | 20s | 20s | Overview and context |
| 2. Raw Data | 30s | 50s | Protection and documentation |
| 3. Processed Data | 30s | 1:20 | Pipeline and metadata |
| 4. Outputs | 20s | 1:40 | Organization by purpose |
| 5. Scenario Answer | 15s | 1:55 | Connecting mistakes to solutions |
| 6. Closing | 5s | 2:00 | Wrap-up and key takeaways |

**TOTAL: 2 minutes exactly** (acceptable range: 1:50 - 2:10)

---

## PART 4: RECORDING INSTRUCTIONS

### Step 1: Prepare Your Environment

```bash
# Before recording, open these:

# Terminal 1: Show file structure
ls -la data/
ls -la data/raw/
ls -la data/processed/
ls -la outputs/

# Terminal 2: Have git ready
git log --oneline -1  (to show you've committed)

# Text Editor: Have guides ready
open DATA_ORGANIZATION_GUIDE.md
```

### Step 2: Start Recording

**Trigger:** When everything is ready:

```bash
# Start screenshare/recording application
# OBS Studio: Click "Start Recording"
# Mac: ⌘ + Shift + 5 → Click "Record"
# Windows Camtasia: Click "Rec"
```

**Recording notes:**
- Don't worry about mistakes - can re-record
- Speak clearly and slowly
- Pause briefly between major sections
- Point to screen to highlight key areas

### Step 3: Record Each Segment

**For each segment:**

1. **Preparation**: Navigate to the file/folder you need
2. **Verification**: Confirm it's visible on screen
3. **Record**: Read the script verbatim
4. **Pause**: Natural pause between segments
5. **Transition**: Move to next location (can edit)

**Do not re-record entire video**: Record segments separately and edit together, or do one continuous take.

### Step 4: Stop Recording

When finished:
- Let recording finish to completion
- Export in default format (usually .mp4)
- Save to: `videos/milestone-8-recording.mp4`

### Step 5: Save and Backup

```bash
# Save video file
videos/milestone-8-recording.mp4

# Backup to cloud
# (Upload to Google Drive, OneDrive, or Dropbox)

# Verify file exists and is playable
# Test: Open and watch first 10 seconds
```

---

## PART 5: COMMON PITFALLS & HOW TO AVOID

### Pitfall 1: Speaking Too Fast

**Problem:** Difficult to follow, sounds nervous

**Solution:**
- Deliberately slow down (30% slower feels right)
- Pause between sentences
- Emphasize key points with tone

### Pitfall 2: Unclear Audio

**Problem:** Recording hard to hear or audio is muffled

**Solution:**
- Test audio BEFORE recording (record 10s test)
- Microphone aimed at mouth (4-6 inches away)
- Eliminate background noise (close tabs, silence phone)
- Speak clearly, not mumbled

### Pitfall 3: Terminal/Editor Text Too Small

**Problem:** Viewers cannot read file names or code

**Solution:**
- Increase font size before recording
- In terminal: `Command + +` (Mac) or `Ctrl + +` (Windows)
- In editor: similar shortcuts
- Zoom to 150-200% for clarity
- Test: Can you read it 3 feet from screen?

### Pitfall 4: Not Showing File Structure Clearly

**Problem:** Listener doesn't understand organization

**Solution:**
- Open file explorer deliberately
- Show: data/ → raw/ → specific files
- Use `tree` command if available: `tree data/`
- Point with mouse cursor while explaining

### Pitfall 5: Forgetting the Scenario Question

**Problem:** Video doesn't address the required scenario

**Solution:**
- Write scenario on whiteboard or index card
- Keep in view while recording
- Allocate full 15 seconds to scenario answer
- Practice scenario answer 5 times before recording

### Pitfall 6: Video Too Long

**Problem:** Video running 3-4 minutes instead of 2

**Solution:**
- Use timer on phone: visible while recording
- Practiced read-through (verify timing fits)
- Cut unnecessary words (use script as guide, not gospel)
- If over: Delete Segment 6 (closing) - less critical

### Pitfall 7: Not Demonstrating, Just Explaining

**Problem:** Just reading script without showing files/folders

**Solution:**
- Show file structure first
- Then explain while pointing
- Mix narration (your voice) with visual (mouse pointing)
- Vary between close-ups (files) and wide shots (full screen)

### Pitfall 8: Poor Lighting

**Problem:** Video is dark or screen hard to see

**Solution:**
- Ensure good desk lighting
- Avoid glare on monitor (angle away from light)
- Reduce screen brightness if needed
- Test: Looks good full screen on phone? Yes → Go

---

## PART 6: POST-RECORDING CHECKLIST

### Immediate (within 1 hour)

- [ ] Video file saved and backed up
- [ ] Audio quality acceptable (spot-check 30s sections)
- [ ] Content covers all 5 segments
- [ ] Scenario question answered adequately
- [ ] Timing approximately 2 minutes
- [ ] No major errors or incomprehensibilities

### If Re-recording Needed

Issues:
- [ ] Audio was muffled → Re-record with better microphone
- [ ] Video too long (> 2:15) → Re-record, cut unnecessary words
- [ ] Scenario not answered → Segment 5 only
- [ ] Font too small → Re-record after increasing font size

### Submission Preparation

When satisfied with video:

```bash
# Move video to submission folder
mv milestone-8-recording.mp4 submissions/

# Create submission note
echo "Milestone 8 video: Data Organization
Date recorded: $(date)
Duration: 2:00
Content: Raw/Processed/Outputs organization + scenario answer
" > submission_notes.txt

# Stage for git
git add submissions/milestone-8-recording.mp4
git add submission_notes.txt
```

---

## PART 7: ALTERNATIVE FORMATS (if live is stressful)

If live recording is too stressful, alternatives:

### Option A: Multiple Takes (Edit Together)
```
Recording session:
- Segment 1: Take it 3 times, choose best
- Segment 2: Take it 3 times, choose best
- ...
- Segment 5: Take it 3 times, choose best

Then edit clips together
```

### Option B: Slideshow + Voiceover
```
1. Build PowerPoint/Google Slides with:
   - Slide 1: Title (20s)
   - Slides 2-3: Raw data (30s)
   - Slides 4-5: Processed data (30s)
   - Slides 6: Outputs (20s)
   - Slides 7-8: Scenario (15s)
   - Slide 9: Closing (5s)

2. Record voiceover for each slide
3. Combine into final video
```

### Option C: Screencast + Script (No Live Audio)
```
1. Screen record you walking through folders
2. Record audio separately
3. Combine in video editor
```

**Recommendation:** Live recording is ideal and shows confidence, but any format that meets content requirements is acceptable.

---

## PART 8: WHAT TO SHOW ON SCREEN

### Must Be Visible:
- [ ] Your data/raw/ folder (with files)
- [ ] Your data/processed/ folder (with files)
- [ ] Your outputs/ folder (with subfolders)
- [ ] At least one README.md file
- [ ] At least one _metadata.txt file
- [ ] Terminal/folder showing project structure

### Nice to Have:
- [ ] Your GitHub repo (commit history)
- [ ] A few example files (opened in editor)
- [ ] A processing script (show code briefly)
- [ ] Git log showing commits

### Avoid:
- [ ] Terminal errors or failed commands
- [ ] Sensitive data (passwords, API keys)
- [ ] Cluttered desktop with unrelated files
- [ ] Distracting browser tabs open

---

## PART 9: RUBRIC/SCORING CRITERIA

Instructors/Peer Reviewers Will Assess:

### Video Quality (20 points)
- [ ] Audio is clear and understandable (5 pts)
- [ ] Screen captures are visible (font large enough) (5 pts)
- [ ] Video length approximately 2 minutes (5 pts)
- [ ] Professional presentation (5 pts)

### Content Coverage (50 points)
- [ ] Raw data protection explained (10 pts)
- [ ] Processed data organization shown (10 pts)
- [ ] Output folders organized by purpose (10 pts)
- [ ] Scenario question answered thoroughly (15 pts)
- [ ] Key concepts reinforced (5 pts)

### Demonstration (30 points)
- [ ] Actual files/folders shown (not just described) (10 pts)
- [ ] Documentation files referenced (README, metadata) (10 pts)
- [ ] Clear navigation through project structure (10 pts)

**Total: 100 points**

---

## FINAL CHECKLIST BEFORE SUBMISSION

- [ ] Video recorded and saved
- [ ] Audio quality acceptable
- [ ] All 5 content areas covered
- [ ] Scenario question answered (15+ seconds)
- [ ] Timing approximately 2 minutes
- [ ] Video uploaded/backed up
- [ ] Submission notes created
- [ ] Git commit ready: `git add milestone-8-video.mp4`
- [ ] Ready for PR submission

---

## EXAMPLE VIDEO OUTLINE (Quick Reference)

```
[0:00-0:20] INTRO
"Today showing data organization: raw → processed → outputs"

[0:20-0:50] RAW DATA
Show data/raw/ folder
Explain immutability (why, benefits)
Point to README and DATA_SOURCES.md

[0:50-1:20] PROCESSED DATA
Show data/processed/ folder
Explain naming convention
Show metadata file
Emphasize reproducibility

[1:20-1:40] OUTPUTS
Show outputs/ with models/visualizations/reports
Explain each type and why separated
Show regenerate capability

[1:40-1:55] SCENARIO ANSWER
Read scenario
Explain 3 mistakes (modified raw, mixed files, no docs)
Describe how separation prevents issues

[1:55-2:00] CLOSING
Reinforce trust, reproducibility, simplicity
"Three folders + documentation = success"

[TOTAL: ~2 minutes]
```

---

## QUESTIONS TO ASK YOURSELF WHILE RECORDING

"Am I demonstrating or just talking?"
→ If just talking, show files on screen while you speak

"Could my teammate understand this?"
→ Include folder structure clearly

"Did I answer the scenario?"
→ Check: 15 seconds spent on Segment 5

"Is the audio clear?"
→ Test first 10 seconds of recording

"Does the video match the goal?"
→ Raw/Processed/Outputs organization demonstrated

---

**You've got this! Clear communication + working example = great submission.**

---

# Appendix: QUICK SCRIPT FOR REFERENCE (Condensed)

**20s - Intro:**
"Hi, Milestone 8: Organizing Data Responsibly. Three stages: raw, processed, 
outputs. Why it matters: reproducibility, team trust, transparent workflows."

**30s - Raw:**
"Raw data folder. Sacred rule: never modify. Immutable. If corrupted, no backup, 
no reproducibility. See DATA_SOURCES.md - documents sources, dates, re-export 
procedures. Proof of original state."

**30s - Processed:**
"Processed data folder. Clear naming tells story. Metadata accompanies each file. 
Documents transformations, impact, reproducibility. Audit trail. Can regenerate 
anytime."

**20s - Outputs:**
"Outputs organized by purpose: models, visualizations, reports. Disposable - can 
regenerate by running scripts. Transparent results."

**15s - Scenario:**
"Scenario: can't reproduce, raw modified, outputs mixed. Mistakes: edited raw 
data, no file separation, no documentation. Solution: separate folders + metadata 
= reproducibility."

**5s - Closing:**
"Three simple folders + clear naming + documentation = trust, reproducibility, 
team success."

---

**End of Video Guide**
