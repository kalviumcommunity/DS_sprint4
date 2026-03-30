# Milestone 5 Completion Guide

**Milestone:** Running, Restarting, and Interrupting Jupyter Kernels  
**Branch:** `feature/milestone-5-kernel-management`  
**Status:** Ready for Video Recording and Submission  

---

## Table of Contents

1. [Milestone Overview](#milestone-overview)
2. [What You've Completed](#what-youve-completed)
3. [Next Steps: Before Recording Video](#next-steps-before-recording-video)
4. [Recording Your Video](#recording-your-video)
5. [Submission Instructions](#submission-instructions)
6. [Common Issues & Fixes](#common-issues--fixes)
7. [Key Learning Outcomes](#key-learning-outcomes)

---

## Milestone Overview

### What This Milestone Teaches
This milestone focuses on **execution discipline** and **kernel state management**, not data analysis. By completing this milestone, you'll demonstrate:

1. **Intentional Execution**: Running cells in deliberate order
2. **State Awareness**: Understanding how the kernel retains variables
3. **Interrupt Safety**: Stopping slow cells without crashing
4. **Restart Discipline**: Clearing state and ensuring reproducibility
5. **Debugging Prevention**: Understanding why notebooks fail when shared

### Why It Matters
- **Professional Practice**: All data scientists must ensure notebooks work for anyone, not just on their machine
- **Debugging**: Understanding kernel state solves 80% of "undefined variable" errors
- **Collaboration**: Sharing reproducible notebooks is a core skill
- **Production Readiness**: Self-discipline prevents embarrassing failures in real projects

### Real-World Scenario
You've built a great analysis notebook. Everything works perfectly on your machine. You upload it to GitHub and a colleague tries to run it. After 5 minutes, they report: "NameError on line X—your code is broken!"

But it works fine for you!

**Root Cause:** You ran cells out of order when testing. Cell X depended on Cell Y, but Y hadn't run yet. The kernel had the right state because you ran Y earlier in a different order. Your colleague ran cells top-to-bottom and hit the dependency: Cell X failed.

**Prevention:** Use "Restart & Run All Cells" before sharing. If that passes, your notebook is reproducible.

---

## What You've Completed

### Artifact 1: KERNEL_MANAGEMENT_GUIDE.md
**Purpose:** Comprehensive reference document  
**Contents:**
- Explanation of what a kernel is
- Kernel state and memory persistence
- How to run cells intentionally
- How to interrupt execution safely
- How to restart the kernel
- Best practices (7+)
- Common mistakes with fixes (5+)
- Scenario analysis for the real-world "undefined variable" problem
- Troubleshooting guide

**Usage:** Read before video recording for context; reference while explaining in video

### Artifact 2: notebooks/05-kernel-management-demo.ipynb
**Purpose:** Interactive demonstration notebook  
**Contents:**
- Part 1: Setup with 3 cells building on each other
- Part 2: Kernel state verification
- Part 3: Interrupt demonstration (long-running cell)
- Part 4: Restart demonstration (verifying state cleared)
- Part 5: Recovery and reproducibility check

**What It Demonstrates:**
- ✓ Cells executed in order produce expected output
- ✓ Variables from Cell 1 are accessible in Cell 5
- ✓ Interrupting Cell 5 doesn't clear variables from earlier cells
- ✓ Restarting kernel clears all variables
- ✓ Running all cells again restores variables with same outputs

**Testing:** Open this notebook, run through all parts, ensure outputs match expectations

### Artifact 3: KERNEL_MANAGEMENT_CHECKLIST.txt
**Purpose:** Comprehensive verification and self-assessment  
**Contents:**
- Knowledge assessment questions
- Setup verification
- Execution tests (normal, interrupt, restart, reproducibility)
- Documentation quality review
- Video requirements checklist
- Submission readiness verification
- Common issues and fixes
- Self-assessment section

**Usage:** Use as your testing roadmap before video recording

### Artifact 4: MILESTONE-5-VIDEO-GUIDE.md
**Purpose:** Exact script and timing for video recording  
**Contents:**
- Before-recording preparation checklist
- 4 segments with exact timing:
  - Segment 1: Normal execution (35 seconds)
  - Segment 2: Interrupt demonstration (50 seconds)
  - Segment 3: Restart demonstration (25 seconds)
  - Segment 4: Scenario-based reasoning (10 seconds)
- Verbatim scripts for each segment
- Expected actions (what to click/show)
- Scenario question and acceptable answers
- Timing reference table
- Post-recording quality checklist
- Upload and submission instructions

**Usage:** Print this or have on second screen while recording

---

## Next Steps: Before Recording Video

### Step 1: Review the Concepts (15 minutes)

Read through **KERNEL_MANAGEMENT_GUIDE.md** sections:
- "Kernel State and Memory" (essential)
- "Running Cells Intentionally" (essential)
- "Interrupting Execution" (you'll demo this)
- "Restarting the Kernel" (you'll demo this)

Focus on understanding:
- [ ] What a kernel is and why it matters
- [ ] Why deleted cells' effects persist in memory
- [ ] When to interrupt vs restart
- [ ] The importance of "Run All Cells" testing

### Step 2: Test the Notebook (20 minutes)

Open **notebooks/05-kernel-management-demo.ipynb** and follow the built-in instructions:

**Quick Test (10 minutes):**
- [ ] Open notebook in VS Code Jupyter or Jupyter Notebook
- [ ] Run Cells 1-3 in order
- [ ] Verify each produces output showing completion
- [ ] Run Cell 4 to verify state persistence

**Interrupt Test (5 minutes):**
- [ ] Find Cell 5 (long-running iteration)
- [ ] Run Cell 5
- [ ] After 2-3 iterations, press Ctrl+C to interrupt
- [ ] Run Cell 6 to verify state preserved

**Restart Test (5 minutes):**
- [ ] Kernel → Restart Kernel (confirm)
- [ ] Run Cell 7 to verify variables are cleared
- [ ] Scroll near Cell 8 to see the "REPRODUCIBILITY CHECK" section
- [ ] Run Cell 8 (should show all checks passing)

### Step 3: Run Through the Video Script (10 minutes)

Read **MILESTONE-5-VIDEO-GUIDE.md** completely:
- [ ] Read all 4 segment scripts verbatim
- [ ] Identify what you'll click/show for each action
- [ ] Practice saying the scenario answer out loud
- [ ] Check your timing (use a stopwatch for each segment)

### Step 4: Set Up Recording Equipment (5 minutes)

- [ ] Screen resolution is at least 1280×720
- [ ] Microphone is plugged in and working
- [ ] Recording software is installed (OBS, Zoom, QuickTime, etc.)
- [ ] Notebook is open and ready
- [ ] You have the script visible (print or second monitor)

### Estimated Total Preparation Time: 45 minutes

---

## Recording Your Video

### Quick Reference
| Segment | Duration | What to Show |
|---------|----------|--------------|
| 1. Intro & Cell Tour | :35 | Open notebook, show structure, run Cells 1-3 |
| 2. Interrupt Demo | :50 | Run Cell 5, interrupt after 3 iterations, verify state |
| 3. Restart Demo | :25 | Restart kernel, show variables cleared, explain importance |
| 4. Scenario Answer | :10 | Answer the "undefined variable" scenario question |
| **Total** | **~2:00** | All segments combined |

### Recording Process

1. **Start Recording** (in your screen capture software)
2. **Segment 1** (0:00–0:35): Run Cells 1-3 normally
3. **Segment 2** (0:35–1:25): Interrupt Cell 5, show state preserved
4. **Segment 3** (1:25–1:50): Restart kernel, show variables cleared
5. **Segment 4** (1:50–2:00): Answer the scenario question
6. **Stop Recording**

### Pacing Tips
- **Speak at normal, conversational pace** (not too fast, not too slow)
- **Pause briefly while cells are executing** (don't talk over output loading)
- **Point to key details** on screen while explaining
- **Look at camera/imagine speaking to a friend** (not at the code)

### Exact Script Reminders

**Segment 1 Opening:**
"Hi! This is Milestone 5: Kernel Control. Today I'm demonstrating how to run, interrupt, and restart a Jupyter kernel..."

**Segment 2 Opening:**
"Now I'm looking for the cell that runs long enough to interrupt. Here it is—Cell 5. This cell loops 100 times..."

**Segment 3 Opening:**
"Now I'm going to restart the kernel. This clears everything from memory..."

**Segment 4 Opening:**
"The scenario is: A notebook works on your machine but fails for someone else with undefined variable errors..."

---

## Submission Instructions

### Before Submission: Final Checklist

- [ ] Video is approximately 2 minutes (±10 seconds)
- [ ] Audio is clear (no background noise)
- [ ] Video is in standard format (MP4, MOV, WebM, etc.)
- [ ] You demonstrated all 4 segments
- [ ] You answered the scenario question with kernel state context
- [ ] Notebook passes all tests (execute, interrupt, restart)
- [ ] All 5 files committed to branch

### Submission Steps

#### Step 1: Create the GitHub Pull Request

1. Navigate to: https://github.com/kalviumcommunity/DS_sprint4
2. Click **Pull Requests** tab
3. Click **New Pull Request**
4. Set:
   - **Base branch:** `main` (or `add-ds-lifecycle-doc` if specified)
   - **Compare branch:** `feature/milestone-5-kernel-management`
5. Click **Create Pull Request**
6. Fill in the PR details:
   - **Title:** `Milestone 5: Kernel Control and Reproducibility`
   - **Description:**
     ```
     Demonstrates kernel management including:
     - Running cells intentionally in order
     - Interrupting long-running cells
     - Restarting the kernel and clearing state
     - Ensuring notebook reproducibility

     Files included:
     - KERNEL_MANAGEMENT_GUIDE.md: Comprehensive reference
     - notebooks/05-kernel-management-demo.ipynb: Interactive demo
     - KERNEL_MANAGEMENT_CHECKLIST.txt: Testing checklist
     - MILESTONE-5-VIDEO-GUIDE.md: Video script and timing

     Video: [link will be added in comments]
     ```
7. Click **Create Pull Request**

#### Step 2: Upload Your Video

1. Upload video to one of these platforms:
   - Google Drive (share with view permission)
   - YouTube (unlisted video)
   - GitHub (in the PR or as a release)
   - Dropbox or OneDrive (share link)
2. Get the shareable link
3. Test the link (open in private/incognito window)

#### Step 3: Share the Video Link

1. Return to your PR on GitHub
2. Click **Add a comment**
3. Paste the video link and write:
   ```
   Video walkthrough: [link]
   
   This video demonstrates:
   - Normal cell execution (Segment 1)
   - Interrupting a long-running cell (Segment 2)
   - Restarting the kernel and clearing state (Segment 3)
   - Scenario answer for undefined variable errors (Segment 4)
   ```
4. Click **Comment**

#### Step 4: Submit to Instructor

Submit via your course's assignment submission platform:
1. PR Link: `https://github.com/kalviumcommunity/DS_sprint4/pull/[PR_NUMBER]`
2. Video Link: `[Your video shareable link]`

### PR Link Format
After creating the PR, your link will be:
`https://github.com/kalviumcommunity/DS_sprint4/pull/[NUMBER]`

Share this link in the assignment submission.

---

## Common Issues & Fixes

### Issue 1: "Interrupt doesn't work—cell keeps running"
**Solution:**
- Verify Cell 5 has `time.sleep` and a loop
- Try pressing Ctrl+C instead of clicking the Stop button
- If neither works, click the Stop button in the notebook toolbar
- Last resort: Restart kernel and re-record

### Issue 2: "Video is too long/too short"
**Solution:**
- Target is ~2 minutes ±10 seconds (acceptable range: 1:50–2:10)
- If too long: Reduce explanation detail, speak faster slightly
- If too short: Add more context to scenario answer, slow down slightly

### Issue 3: "My video recording has bad audio"
**Solution:**
- Move microphone closer to mouth (~6 inches)
- Reduce background noise (fan, traffic)
- Test microphone in recording software first
- Use headset microphone instead of computer's built-in mic

### Issue 4: "Scenario answer doesn't make sense"
**Solution:**
- Refer to MILESTONE-5-VIDEO-GUIDE.md for example answers
- Your answer must mention: kernel state, execution order, or "Run All Cells"
- Practice the answer out loud before recording
- If unsure, explain the demo you just did as your answer

### Issue 5: "Notebook cell fails when I run it"
**Solution:**
- Ensure cells run in order (Cell 1 → Cell 2 → ...)
- Try "Kernel → Restart Kernel" then "Kernel → Run All Cells"
- Check for typos in cell names (PROJECT_NAME, dataset, processed_data)
- If error persists, refer to KERNEL_MANAGEMENT_CHECKLIST.txt troubleshooting section

### Issue 6: "I don't have time to record—deadline is soon"
**Solution:**
- Record a shorter version (1:45) instead of perfect 2:00
- Use the script verbatim (don't improvise)
- Record in one take (don't edit)
- Submit what you have rather than nothing

---

## Key Learning Outcomes

### By completing this milestone, you should be able to:

**Conceptual Understanding:**
- [ ] Explain what a kernel is in 2-3 sentences
- [ ] Describe kernel state and why it matters
- [ ] Explain why "Run All Cells" is the reproducibility test
- [ ] Understand when to interrupt vs restart

**Practical Skills:**
- [ ] Run a Jupyter cell intentionally (Ctrl+Enter)
- [ ] Interrupt a cell without restarting (Ctrl+C)
- [ ] Restart the kernel (Kernel → Restart)
- [ ] Test reproducibility with "Run All Cells"

**Debugging Capability:**
- [ ] Identify hidden kernel state causing "undefined variable" errors
- [ ] Know how to test if a notebook is reproducible
- [ ] Understand execution order dependencies
- [ ] Fix notebooks that fail when shared

**Professional Practice:**
- [ ] Always run "Run All Cells" before sharing
- [ ] Avoid relying on manual cell execution order
- [ ] Write notebooks that work for anyone
- [ ] Document dependencies between cells

---

## Summary

### The Complete Workflow

1. ✓ **Understand the concepts** (read KERNEL_MANAGEMENT_GUIDE.md)
2. ✓ **Test the notebook** (follow KERNEL_MANAGEMENT_CHECKLIST.txt)
3. ✓ **Prepare recording** (print MILESTONE-5-VIDEO-GUIDE.md script)
4. **Record your video** (~2 minutes, 4 segments)
5. **Upload video** to shareable platform
6. **Create PR** on GitHub
7. **Submit links** to instructor

### Files Submitted to PR
- ✓ KERNEL_MANAGEMENT_GUIDE.md (comprehensive reference)
- ✓ notebooks/05-kernel-management-demo.ipynb (interactive demo)
- ✓ KERNEL_MANAGEMENT_CHECKLIST.txt (testing guide)
- ✓ MILESTONE-5-VIDEO-GUIDE.md (recording script)
- ✓ MILESTONE-5-COMPLETION-GUIDE.md (this file)

### Video Segments (2 minutes total)
| Segment | Duration | Focus |
|---------|----------|-------|
| Normal Execution | :35 | Cells 1-3 in order, state persistence |
| Interrupt Demo | :50 | Cell 5 interrupted, state preserved |
| Restart Demo | :25 | Kernel restarted, state cleared |
| Scenario Answer | :10 | "Undefined variable" problem explained |

---

## Final Preparation

**The Night Before Recording:**
- [ ] Review MILESTONE-5-VIDEO-GUIDE.md script (read once through)
- [ ] Test notebook execution once (quick 10-minute run)
- [ ] Check recording software is installed and working
- [ ] Make sure microphone is available

**Day of Recording:**
- [ ] Clear desk/background of distracting items
- [ ] Pre-stage notebook (open, ready to use)
- [ ] Print or open script on second device
- [ ] Do a 30-second test recording to check audio/video
- [ ] Take a deep breath—you've got this!

**After Recording:**
- [ ] Review video (watch it back)
- [ ] Upload to hosting platform
- [ ] Test the shareable link
- [ ] Continue to submission steps

---

**Congratulations on reaching Milestone 5!**

You're demonstrating core execution discipline and debugging awareness that professional data scientists use daily. Master kernel management, and you'll never waste hours debugging "it works on my machine" problems.

Good luck with your video—you've prepared thoroughly. Now go record and show what you know!

For questions, refer to:
- KERNEL_MANAGEMENT_GUIDE.md (concepts)
- KERNEL_MANAGEMENT_CHECKLIST.txt (testing)
- MILESTONE-5-VIDEO-GUIDE.md (recording)

**Let's go! 🚀**
