# MILESTONE 8: COMPLETION GUIDE
## Organizing Raw Data, Processed Data, and Output Artifacts

**Status:** All artifacts created and ready for submission  
**What This Milestone Covers:** Understanding and implementing proper data lifecycle management  
**Video Duration:** ~2 minutes  
**Estimated Total Time:** 2-3 hours (30 min. study + 1.5 hr. implementation + 30 min. video)  

---

## TABLE OF CONTENTS

1. [What's Been Completed](#whats-been-completed)
2. [The Five Artifacts](#the-five-artifacts)
3. [Your Task: Record the Video](#your-task-record-the-video)
4. [Submission Process](#submission-process)
5. [Common Issues & Solutions](#common-issues--solutions)
6. [Key Learning Outcomes](#key-learning-outcomes)
7. [From Milestone 8 to 9](#from-milestone-8-to-9)
8. [Final Verification Checklist](#final-verification-checklist)

---

## WHAT'S BEEN COMPLETED

Your learning materials for Milestone 8 include:

### ✓ DATA_ORGANIZATION_GUIDE.md
- **Length:** 2,000+ words
- **Content:** Comprehensive reference on data lifecycle management
- **Topics Covered:**
  - Why data organization matters (real cost/benefit scenarios)
  - The three stages: raw ← processed ← outputs
  - Raw data protection and immutability
  - Processed data traceability and documentation
  - Output artifacts organization
  - Naming conventions for every stage
  - Data versioning strategies
  - Metadata and documentation standards
  - Reproducibility and auditability principles
  - Real-world example workflows (e-commerce, time series)
  - Common mistakes and how to fix them
  - Data governance best practices
  
- **How to Use:** Reference while building your own project structure

### ✓ sample-data-organization-project/
- **Structure:** Complete e-commerce sales analysis example
- **Contains:**
  - data/raw/ with 3 raw files documented
  - data/processed/ with 4 cleaned datasets
  - outputs/ (models/, visualizations/, reports/)
  - scripts/ with processing pipeline
  - docs/ with documentation
  - Complete README hierarchy explaining each folder
  - DATA_SOURCES.md documenting all sources
  - Example metadata files

- **How to Use:** Reference for your own organization; shows best practices in action

### ✓ DATA_ORGANIZATION_CHECKLIST.txt
- **Length:** 600+ lines
- **Structure:** 14 comprehensive sections (A-N)
- **Contents:**
  - Raw data protection verification
  - Processed data quality checks
  - Separation of concerns verification
  - Data quality documentation
  - Output organization validation
  - Naming convention assessment
  - Version control integration
  - Reproducibility testing
  - Common mistakes identification
  - Collaboration readiness
  - Video preparation
  - Self-assessment
  - Final sign-off
  - Scoring rubric

- **How to Use:** Work through each section to verify your understanding and preparation

### ✓ MILESTONE-8-VIDEO-GUIDE.md
- **Length:** 600+ lines with complete scripts
- **Segments:** 6 scripted segments with exact timing
- **Includes:**
  - Equipment checklist
  - Complete verbatim scripts for each segment
  - Detailed recording instructions
  - Common pitfalls & solutions
  - Post-recording checklist
  - Scoring rubric
  - Alternative recording formats
  - Quick reference guide

- **How to Use:** Follow while recording your video

### ✓ MILESTONE-8-COMPLETION-GUIDE.md
- **This File**
- **Purpose:** Guide you from learning → implementation → submission

---

## THE FIVE ARTIFACTS

This Milestone contains **Five Required Artifacts**:

### Artifact 1: DATA_ORGANIZATION_GUIDE.md
- **Status:** ✓ Created and complete
- **Review:** Read through to understand all concepts
- **Study Time:** 30-45 minutes
- **Key Action:** Reference while building own structure

### Artifact 2: sample-data-organization-project/
- **Status:** ✓ Created with full folder structure
- **Review:** Explore folder structure, read all README files
- **Study Time:** 20-30 minutes
- **Key Action:** Use as template for your own project organization

### Artifact 3: DATA_ORGANIZATION_CHECKLIST.txt
- **Status:** ✓ Created with 14 sections
- **Review:** Work through each part thoroughly
- **Study Time:** 40-60 minutes
- **Key Action:** Use to assess your own project readiness

### Artifact 4: MILESTONE-8-VIDEO-GUIDE.md
- **Status:** ✓ Created with complete scripts
- **Review:** Review 2-3 times before recording
- **Study Time:** 10-15 minutes (per review)
- **Key Action:** Follow while recording video

### Artifact 5: MILESTONE-8-COMPLETION-GUIDE.md
- **Status:** ✓ You're reading it now
- **Review:** Bookmark for reference during submission
- **Study Time:** 15-20 minutes
- **Key Action:** Use as step-by-step guide through completion

---

## YOUR TASK: RECORD THE VIDEO

**Estimated Time:** 30-60 minutes (including retakes)

### Overview

Create a ~2-minute video demonstrating your understanding of data organization:

1. **Show** your actual project structure (raw/processed/outputs)
2. **Explain** why each stage is organized the way it is
3. **Answer** the scenario question about data organization mistakes
4. **Demonstrate** that you understand reproducibility principles

### The Scenario You Must Answer

> "A teammate cannot reproduce your results because the raw data appears to be 
> altered and outputs are mixed with input files. What data organization mistakes 
> likely caused this, and how would separating raw, processed, and output data 
> prevent the issue?"

**This is the most important part of your video.** Spend 15+ seconds answering it thoroughly.

### Before Recording: Preparation Checklist

#### Content Preparation
- [ ] Review DATA_ORGANIZATION_GUIDE.md (especially common mistakes section)
- [ ] Study sample-data-organization-project folder structure
- [ ] Review MILESTONE-8-VIDEO-GUIDE.md at least twice
- [ ] Practice your scenario answer (out loud) 3-5 times
- [ ] Test understanding: Explain to a friend or family member

#### Project Preparation
- [ ] Your project folder structure set up:
  - [ ] data/raw/ with sample raw files
  - [ ] data/processed/ with example processed files
  - [ ] outputs/ folder with subfolders
- [ ] README files created in key folders
- [ ] At least one metadata file created
- [ ] Project files saved, committed to git
- [ ] Confidence level: 70%+ before recording

#### Technical Preparation
- [ ] Recording software tested and ready
- [ ] Microphone tested (record 10-second test)
- [ ] Screen capture/camera set up and working
- [ ] Terminal ready to show file structure
- [ ] Text editor ready with guide files open
- [ ] Quiet environment prepared
- [ ] Do a 20-second test recording and replay to verify quality

#### Mental Preparation
- [ ] Have read the guide 2+ times
- [ ] Feel comfortable explaining each section
- [ ] Practiced scenario answer
- [ ] Know what you'll show on screen
- [ ] Understand the key concepts
- [ ] Ready to record (not perfect, just ready!)

### Recording Steps

**Step 1: Set Up Your Screen (5 minutes)**

```bash
# Open Terminal/PowerShell
ls -la data/
tree data/ (if available)

# Open File Explorer
Navigate to: project/data/raw/
Navigate to: project/data/processed/
Navigate to: project/outputs/

# Open Text Editor
Open: DATA_ORGANIZATION_GUIDE.md
```

**Step 2: Start Recording (1-3 minutes)**

Start your screen recording software:
- OBS Studio: Click "Start Recording"
- Mac: ⌘ + Shift + 5 → Click "Record"
- Windows Camtasia: Click "Rec"

**Step 3: Open with Introduction (First 20 seconds)**

[Camera shows you]

Read from MILESTONE-8-VIDEO-GUIDE.md, Segment 1

Focus on:
- What you're demonstrating
- Why it matters
- What to expect in video

**Step 4: Show Raw Data (20-30 seconds)**

[Camera shows: data/raw/ folder open]

- Navigate to data/raw/ folder
- Show the files
- Open README.md and point to key lines
- Show DATA_SOURCES.md
- Explain immutability principle

**Step 5: Show Processed Data (20-30 seconds)**

[Camera shows: data/processed/ folder open]

- Navigate to data/processed/ folder
- Show the files (notice naming convention)
- Open one _metadata.txt file
- Point to processing steps documented
- Explain traceability and reproducibility

**Step 6: Show Outputs (15-20 seconds)**

[Camera shows: outputs/ folder open]

- Show outputs/models/, outputs/visualizations/, outputs/reports/
- Explain purpose of each
- Show 2-3 example files
- Explain why separated by purpose

**Step 7: Answer Scenario (15 seconds) - CRITICAL**

[Camera shows: You looking at camera]

Answer the provided scenario question:

"A teammate cannot reproduce your results because..."

Your answer MUST include:
- What mistakes were made (raw data modified, files mixed, no docs)
- Why these are problems (why bother?)
- How separation fixes it (from raw/processed/outputs)
- Why this enables reproducibility and trust

**Step 8: Closing (5 seconds)**

[Camera shows: You]

Wrap up with key takeaway:
- Three simple folders
- Clear naming
- Complete documentation
- Enables reproducibility and trust

**Step 9: Stop Recording**

When done:
- Stop recording
- Find the recorded file
- Save to: videos/milestone-8-video.mp4
- Backup to cloud

### Post-Recording: Verification

After recording, review:

- [ ] Audio is clear and audible
- [ ] Video shows all required components
- [ ] Scenario question answered thoroughly
- [ ] Timing is approximately 2 minutes
- [ ] Video is shareable (.mp4 or .mov format)
- [ ] File size reasonable (< 500 MB ideally)

### If Re-recording Needed

If you're not satisfied, common issues and fixes:

| Issue | Fix |
|-------|-----|
| Audio too quiet | Increase microphone volume, re-record |
| Audio muffled | Move microphone closer, eliminate background noise |
| Font/files too small to read | Zoom 150-200%, re-record |
| Speaking too fast | Deliberately slow down, re-record |
| Video too long (>2:15) | Cut unnecessary words, re-record |
| Scenario not answered | Re-record just Segment 5 (or whole video) |

**It's okay to re-record.** Quality > Getting it perfect first time.

---

## SUBMISSION PROCESS

**Timeline:** After you've completed everything, submit:

### Step 1: Finalize Your Project Structure

Verify your project includes:

```
your-project/
├── data/
│   ├── raw/                           ← Raw data (immutable)
│   │   ├── README.md                  ← Explains immutability
│   │   ├── DATA_SOURCES.md            ← Documents sources
│   │   └── [sample files]
│   └── processed/                     ← Cleaned data
│       ├── README.md                  ← Explains pipeline
│       ├── [cleaned files]
│       └── [*_metadata.txt files]
├── outputs/                           ← Generated artifacts
│   ├── models/
│   ├── visualizations/
│   ├── reports/
│   └── README.md                      ← Explains organization
├── scripts/                           ← Processing code
│   └── README.md                      ← Explains pipeline
└── README.md                          ← Project overview
```

- [ ] All folders present
- [ ] README files in key folders
- [ ] Sample files to demonstrate
- [ ] Metadata documented
- [ ] Committed to git

### Step 2: Prepare Submission Branch

```bash
# Create feature branch
git checkout -b feature/milestone-8-data-organization

# Stage all Milestone 8 artifacts
git add DATA_ORGANIZATION_GUIDE.md
git add DATA_ORGANIZATION_CHECKLIST.txt
git add MILESTONE-8-VIDEO-GUIDE.md
git add MILESTONE-8-COMPLETION-GUIDE.md
git add sample-data-organization-project/

# Make commit
git commit -m "Milestone 8: Organizing Raw Data, Processed Data, and Output Artifacts
- Complete guide on data lifecycle management
- Sample project demonstrating best practices
- Comprehensive checklist for verification
- Video recording guide with scripts"

# Verify commit
git log --oneline -1
```

### Step 3: Record Your Video

(See "Your Task: Record the Video" section above)

Completion status:
- [ ] Video recorded and saved
- [ ] Audio quality verified
- [ ] Content complete (all 6 segments)
- [ ] Scenario answered thoroughly
- [ ] Saved to: videos/milestone-8-video.mp4

### Step 4: Add Video to Submission

```bash
# Create videos folder if needed
mkdir -p videos

# Save your video
cp [your-recording] videos/milestone-8-video.mp4

# Stage video
git add videos/milestone-8-video.mp4

# Commit with video
git commit --amend  # Add to previous commit

# Or make separate commit
git commit -m "Add Milestone 8 video recording"
```

### Step 5: Push to Remote

```bash
# Push feature branch
git push -u origin feature/milestone-8-data-organization

# Verify push successful
# GitHub will show: "Create a pull request for 'feature/milestone-8-data-organization'"
```

### Step 6: Create Pull Request

**On GitHub:**

1. Go to your repository: github.com/kalviumcommunity/DS_sprint4
2. You'll see banner: "Compare & pull request" for feature/milestone-8-data-organization
3. Click "Create Pull Request"
4. Fill in PR template:

```markdown
## Milestone 8: Data Organization Submission

### Artifacts Included
- [x] DATA_ORGANIZATION_GUIDE.md
- [x] sample-data-organization-project/
- [x] DATA_ORGANIZATION_CHECKLIST.txt
- [x] MILESTONE-8-VIDEO-GUIDE.md
- [x] MILESTONE-8-COMPLETION-GUIDE.md
- [x] Video recording: videos/milestone-8-video.mp4

### Video Duration
~2 minutes

### Key Demonstrations
- Raw data protection and immutability
- Processed data organization and metadata
- Output artifacts separated by purpose
- Scenario question: Data organization mistakes

### Related PR
Builds on Milestone 7: Project Structure

### Additional Notes
[Any notes about your implementation]
```

5. Click "Create Pull Request"

### Step 7: Verification

After PR is created:

```bash
# Verify files in PR
# Check: All artifacts visible
# Check: Video attached
# Check: README files readable
# Check: Project structure clear

# Verify branch tracking
git status
# Should show: Your branch is up to date with 'origin/feature/milestone-8-data-organization'
```

---

## COMMON ISSUES & SOLUTIONS

### Issue 1: "I don't understand the difference between raw and processed data"

**Solution:**

**Raw Data:**
- Definition: Exact copy from source (never modified)
- Example: sales.csv downloaded from Shopify
- State: Immutable, preserved, documented

**Processed Data:**
- Definition: Result of transformations applied to raw
- Example: sales_cleaned.csv (after removing duplicates)
- State: Traceable, metadata documented, reproducible

**Key Test:** Ask "Did this come directly from source unchanged?" 
- YES → Raw data
- NO → Processed data

### Issue 2: "How do I know if my organization is good?"

**Solution:**

Ask yourself these questions:

1. **Can a teammate understand the structure immediately?**
   - If they don't ask questions in first 2 minutes → Good organization

2. **Can I reproduce all outputs from raw data?**
   - If YES → Good organization
   - If NO → Missing something (documentation, scripts, etc.)

3. **Is the audit trail clear?**
   - Can I trace: Raw → Processed → Output?
   - If YES → Good organization

4. **Would I understand this 6 months from now?**
   - If YES → Good organization
   - If NO → Add more documentation

### Issue 3: "My video keeps running too long (> 2:15)"

**Solution:**

Trim the fat:

- [ ] Remove "umm" and "uh" (edit out or re-record)
- [ ] Cut repeated explanations
- [ ] Skip less important details
- [ ] Focus on: Raw, Processed, Outputs, Scenario

**Acceptable cuts (in order of removability):**
1. Detailed intro (reduce from 20s to 15s)
2. Folder organization details (reduce from 20s to 15s)
3. Examples section (can skip if running over)

### Issue 4: "I can't demonstrate the scenario - what do I do?"

**Solution:**

The scenario is mandatory. Include in your video:

1. **Restate the scenario** (don't assume viewer knows it):
   "Let me read this scenario: A teammate cannot reproduce..."

2. **Identify the mistakes:**
   - Raw data was modified
   - Outputs mixed with data files
   - No documentation

3. **Explain why each is a problem:**
   - Modified raw data = no proof of original
   - Mixed files = confusing, hard to find things
   - No documentation = can't understand what was done

4. **Describe the solution:**
   - Keep raw data immutable in data/raw/
   - Separate processed in data/processed/
   - Keep outputs in outputs/ organized by type
   - Document everything with metadata

This should take 15-20 seconds. Essential.

### Issue 5: "I don't know what files to show in my video"

**Solution:**

At minimum, show:

**Raw Folder:**
- 2-3 example raw files
- README.md explaining immutability
- DATA_SOURCES.md if available

**Processed Folder:**
- 2-3 cleaned files (showing naming convention)
- One metadata file (showing what documentation included)

**Outputs Folder:**
- Show 3 subfolders (models/, visualizations/, reports/)
- Show 1-2 example files in each type

**Total:** 8-10 files shown = sufficient

### Issue 6: "My technology won't cooperate with recording"

**Solution:**

Alternatives to screen recording:

**Option A: Slideshow + Voiceover**
- Create slides in PowerPoint/Google Slides
- Show code/folders on slides
- Record audio separately
- Combine using free online tool

**Option B: Phone Photos + Audio**
- Take photos of your screen/documents
- Create slideshow in images
- Record voiceover to explain each image
- Compile using iMovie, Windows Photos, etc.

**Option C: Talk-Through with Screen Capture**
- Use built-in screenshot tool
- Record yourself (not screen) explaining
- Show static images as reference
- Point to screen sometimes

Any format that demonstrates your understanding is acceptable.

### Issue 7: "I'm nervous about being on camera"

**Solution:**

You don't have to show your face! Options:

- [ ] Screen recording only (show just your screen/files/terminal)
- [ ] Show hands pointing (hands only, no face)
- [ ] Voiceover while showing screen (professional format)
- [ ] Animated slides with your voice (no appearance at all)

The goal is demonstrating *understanding*, not showcasing you. Comfortable format = better content.

### Issue 8: "I can't figure out the folder structure"

**Solution:**

Use sample-data-organization-project as exact template:

```bash
# Copy sample structure
cp -r sample-data-organization-project/ my-project

# Customize sample files
cd my-project
# Edit README files to your project
# Add your own raw data examples
# Show your processing pipeline

# Commit
git add my-project/
git commit -m "My data organization project"
```

This is not cheating - it's using a template correctly!

---

## KEY LEARNING OUTCOMES

After completing Milestone 8, you should understand:

### Knowledge Goals ✓

By the end of this milestone, you can:

#### Concept 1: Raw Data Immutability
- [ ] Explain why raw data should never be modified
- [ ] Understand consequences when raw data changes
- [ ] Describe how to protect raw data (read-only, backups)
- [ ] Document data sources completely

#### Concept 2: Data Processing Pipeline
- [ ] Understand the flow: Raw → Processed → Outputs
- [ ] Create metadata documenting transformations
- [ ] Name files clearly showing what was done
- [ ] Maintain traceability from inputs to outputs

#### Concept 3: Output Organization
- [ ] Separate outputs by purpose (models/viz/reports)
- [ ] Name files descriptively showing content
- [ ] Understand why outputs are "disposable"
- [ ] Know how to regenerate outputs

#### Concept 4: Reproducibility
- [ ] Understand why reproducibility matters
- [ ] Recreate results from documentation
- [ ] Enable teammates to understand your work
- [ ] Build trust through transparency

#### Concept 5: Data Governance
- [ ] Document data sources (sources, dates, contact)
- [ ] Create audit trails (what changed, when, why)
- [ ] Communicate about data clearly
- [ ] Collaborate on data science projects

### Skills Goals ✓

By the end of this milestone, you can:

- [ ] Create proper folder structure (raw/processed/outputs)
- [ ] Protect raw data from accidental modification
- [ ] Write README files explaining each folder
- [ ] Create metadata documenting transformations
- [ ] Name files following clear conventions
- [ ] Organize outputs logically
- [ ] Trace data lineage through your project
- [ ] Regenerate outputs from processing scripts
- [ ] Explain data organization to teammates
- [ ] Set up reproducible workflows

### Scenarios You Can Now Handle

After Milestone 8, you can:

✓ **Scenario 1:** "How do I organize my data?"
→ Answer: Raw/Processed/Outputs with documentation

✓ **Scenario 2:** "A teammate can't find the data"
→ Answer: Create clear folder structure and README files

✓ **Scenario 3:** "Raw data was accidentally modified, now what?"
→ Answer: Explain why this is critical problem, show how to prevent

✓ **Scenario 4:** "How do I regenerate old analysis?"
→ Answer: Restore scripts and raw data, re-run pipeline, outputs regenerate

✓ **Scenario 5:** "This processed data has errors"
→ Answer: Trace back to raw data, find error in processing script, regenerate

---

## FROM MILESTONE 8 TO 9

After completing Milestone 8, you're ready for the next milestone:

### Milestone 9: Jupyter Notebooks for Data Exploration

**What You'll Learn:**
- How to use Jupyter notebooks for interactive analysis
- Best practices for notebook documentation
- How notebooks fit into the data science workflow
- Sharing and reproducing notebook-based analysis

**How Milestone 8 Prepares You:**
- You understand data organization (notebooks use organized data)
- You know how to document work (notebooks need documentation)
- You understand reproducibility (notebooks should be reproducible)
- You can manage raw/processed data (notebooks analyze processed data)

**Bridge Between Milestones:**
```
Milestone 7: Folder structure (where things go)
Milestone 8: Data organization (what goes in folders) ← YOU ARE HERE
Milestone 9: Jupyter notebooks (how to analyze) ← NEXT
Milestone 10: Exploratory data analysis (what to find)
```

---

## FINAL VERIFICATION CHECKLIST

Before submission, verify:

### Artifacts Present ✓

- [ ] DATA_ORGANIZATION_GUIDE.md (2000+ words)
- [ ] sample-data-organization-project/ (with 10+ files)
- [ ] DATA_ORGANIZATION_CHECKLIST.txt (600+ lines)
- [ ] MILESTONE-8-VIDEO-GUIDE.md (600+ lines)
- [ ] MILESTONE-8-COMPLETION-GUIDE.md (this file)

### Your Project Structure

- [ ] data/raw/ folder created
- [ ] data/processed/ folder created
- [ ] outputs/ folder with subfolders (models/viz/reports)
- [ ] README.md in key folders
- [ ] Metadata files alongside datasets
- [ ] Sample files to demonstrate

### Video Content

- [ ] Video ~2 minutes long (1:50-2:10)
- [ ] Audio clear and audible
- [ ] All 5 content areas covered
- [ ] Scenario question answered (15+ seconds)
- [ ] File structure shown on screen
- [ ] Key concepts explained

### Git Submission

- [ ] Feature branch created: feature/milestone-8-data-organization
- [ ] All artifacts staged: git add [files]
- [ ] Committed with descriptive message
- [ ] Pushed to remote: git push -u origin
- [ ] PR created on GitHub
- [ ] PR description filled in

### Understanding Verification

- [ ] Can explain raw data immutability
- [ ] Can describe processing pipeline
- [ ] Can answer the scenario question
- [ ] Can explain why structure matters
- [ ] Can discuss team collaboration benefits

### Self-Assessment

Rate your confidence (1-5):

**Understanding Concepts:** ____/5
- Raw data protection
- Data processing
- Output organization
- Reproducibility

**Implementing Structure:** ____/5
- Folder organization
- File naming
- Documentation
- Metadata creation

**Communication:** ____/5
- Explaining to teammates
- Answering the scenario
- Video clarity
- Overall presentation

**Overall Confidence:** ____/5

**Target: 4/5 average before submission**

---

## SUCCESS CRITERIA

Your Milestone 8 submission is **successful** when:

✅ **Knowledge**
- Can explain why raw data is immutable
- Can describe data processing pipeline
- Can answer the provided scenario question
- Can identify common classification mistakes

✅ **Application**
- Project structure shows raw/processed/outputs separation
- Files are named clearly showing transformations
- Documentation explains every stage
- Metadata accompanies processed datasets

✅ **Communication**
- Video clearly demonstrates concepts
- Scenario answer is thorough and specific
- Project structure is easy to understand
- README files guide users through folders

✅ **Submission**
- All 5 artifacts included
- PR created with full description
- Video attached and functional
- Everything committed and pushed

---

## A NOTE ON PERFECTION

**Your data organization doesn't have to be perfect.**

It has to be:
✓ Clear (teammates understand it)
✓ Consistent (same pattern throughout)
✓ Documented (explains what/why)
✓ Reproducible (can regenerate outputs)

That's it.

Real projects grow and evolve. Your structure may change. **That's okay.**

What matters is the *principles*:
- Protect raw data
- Track transformations
- Organize outputs
- Document everything

Apply these principles, and you're golden.

---

## FINAL WORDS

This milestone teaches one of the most valuable skills in data science:

**Clear organization and documentation.**

It's not the sexiest skill. Doesn't get you on TechCrunch. But it's the difference between:

❌ Analysis that only you can understand (and you forget after 3 months)  
✅ Analysis that your team can trust, reproduce, and build on

This skill will:
- Make you a better collaborator
- Help you get hired
- Enable your team's success
- Save countless hours of debugging

Invest in this. You won't regret it.

---

## NEED HELP?

**If you're stuck:**

1. **Re-read** the relevant section of DATA_ORGANIZATION_GUIDE.md
2. **Study** the sample-data-organization-project/ example
3. **Review** the section in DATA_ORGANIZATION_CHECKLIST.txt
4. **Answer** the corresponding video script question

**If you're still stuck:**

- Ask a teammate
- Post in the learning channel
- Review the guide again (second read often clarifies)
- Take a short break and return

---

**You've got this. Go build something organized and reproducible.**

---

**Submit to:** github.com/kalviumcommunity/DS_sprint4  
**Branch:** feature/milestone-8-data-organization  
**Video Guide:** MILESTONE-8-VIDEO-GUIDE.md  

Good luck! 🚀
