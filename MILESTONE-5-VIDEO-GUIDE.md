# Milestone 5 Video Walkthrough Guide

**Target Duration:** ~2 minutes (±10 seconds)  
**Format:** Screen recording with verbal explanation  
**Equipment:** Computer + screen + headset/microphone  
**Platform:** Screen capture tool (OBS, Zoom, QuickTime, Windows 10 Screen Recorder, etc.)

---

## Before You Record

**Preparation Checklist:**
- [ ] Notebook is open and ready: `notebooks/05-kernel-management-demo.ipynb`
- [ ] Kernel is fresh (not run any cells yet)
- [ ] VS Code or Jupyter Notebook is visible
- [ ] Microphone is working and clear
- [ ] Screen resolution is at least 1280x720
- [ ] No distracting background applications open
- [ ] You have this script visible while recording (print or second monitor)

**Technical Setup:**
- [ ] Recording software open (OBS Studio, Zoom, QuickTime, etc.)
- [ ] Audio input set to your microphone
- [ ] Video set to "full screen" or "active window"
- [ ] Recording quality set to at least 720p
- [ ] Start recording in a test format first (do a practice run if needed)

**Timing Aid:**
- Print this page or have it on a second screen
- Watch the clock while recording
- If under/over time, adjust pacing or detail level next time

---

## SEGMENT 1: Normal Execution
**⏱ Duration: 35 seconds**  
**Cumulative Time: 0:35**

### What to Show
1. Notebook is open
2. Multiple cells visible (explain structure)
3. Run Cell 1 → Cell 2 → Cell 3 in sequence
4. Show output progression

### Exact Script to Read (verbatim)

**[At 0:00-0:05] - Start recording and introduction**

"Hi! This is Milestone 5: Kernel Control. Today I'm demonstrating how to run, interrupt, and restart a Jupyter kernel. Let me open my notebook."

*Action: Focus on the notebook. Point out cell structure.*

**[At 0:05-0:15] - Tour the notebook structure**

"This notebook has multiple code cells and markdown cells explaining concepts. The kernel is a Python interpreter running in the background. Each time I run a cell, the kernel executes the code and keeps variables in memory."

*Action: Scroll to show 4-5 cells, then go back to top.*

**[At 0:15-0:25] - Run cells in order**

"Let me run the first three cells in order. I'll press Ctrl+Enter to run each cell."

*Action: Click Cell 1, press Ctrl+Enter. Wait for output (should see "✓ Cell 1 Complete"). Repeat for Cells 2 and 3.*

**[At 0:25-0:35] - Explain what happened**

"Notice that Cell 2 used variables from Cell 1, and Cell 3 used variables from both. This is kernel state: variables defined in earlier cells are available in later cells. The kernel maintains this memory."

*Action: Show outputs of Cells 1-3. Point to key outputs.*

---

## SEGMENT 2: Interrupt Demonstration
**⏱ Duration: 50 seconds**  
**Cumulative Time: 1:25**

### What to Show
1. Find the long-running cell (with time.sleep)
2. Start execution
3. Interrupt it after a few iterations
4. Show kernel is still responsive
5. Run next cell to verify variables preserved

### Exact Script to Read (verbatim)

**[At 0:35-0:40] - Find the interrupt-able cell**

"Now I'm looking for the cell that runs long enough to interrupt. Here it is—Cell 5. This cell loops 100 times with a short pause in each iteration, so it'll run for a while."

*Action: Scroll to Cell 5. Show it has "for i in range(100)" and "time.sleep(0.5)".*

**[At 0:40-0:50] - Start execution and interrupt**

"I'm going to run this cell. Once it starts, I'll press Ctrl+C to interrupt it after a few iterations."

*Action: Click Cell 5 and press Ctrl+Enter. Let it output "Processing iteration 1...", "Processing iteration 2...", "Processing iteration 3...". Then press Ctrl+C.*

**[At 0:50-0:60] - Show the interrupt worked**

"Good—I pressed Ctrl+C and the cell stopped. It didn't complete all 100 iterations, but the kernel is still responsive. The important thing: the kernel didn't crash. Variables I defined in earlier cells are still in memory."

*Action: Point to 'interrupt_count' in the output. Show it's a partial number (like 3 or 4), not 100.*

**[At 1:00-1:10] - Run next cell to verify state**

"Let me run the next cell to show that kernel state is preserved."

*Action: Click Cell 6, press Ctrl+Enter. Shows: "interrupt_count = [partial number]" and "PROJECT_NAME = Kernel Demo", confirming state preserved.*

**[At 1:10-1:25] - Explain the concept**

"This demonstrates that interrupting a cell with Ctrl+C stops execution but doesn't clear kernel memory. All variables are still available. I can use this technique when a cell is running too slow or when I made a mistake in the code."

*Action: Point to the output showing preserved state.*

---

## SEGMENT 3: Restart Demonstration
**⏱ Duration: 25 seconds**  
**Cumulative Time: 1:50**

### What to Show
1. Restart kernel using menu
2. Run the "verify after restart" cell
3. Show NameErrors for undefined variables
4. Briefly show "Run All Cells" to restore state

### Exact Script to Read (verbatim)

**[At 1:25-1:35] - Restart the kernel**

"Now I'm going to restart the kernel. This clears everything from memory. I'll use the Kernel menu."

*Action: Click "Kernel" menu. Click "Restart Kernel". Confirm restart in dialog.*

**[At 1:35-1:45] - Verify state is cleared**

"Let me run a cell that checks if variables still exist. I'll run Cell 7."

*Action: Click Cell 7, press Ctrl+Enter. Output shows NameError for PROJECT_NAME, total_records, dataset.*

**[At 1:45-1:50] - Show variables are gone**

"See—all the variables are gone. The kernel memory is empty. To get them back, I need to run all cells from the beginning."

*Action: Point to the "not defined" messages in output.*

---

## SEGMENT 4: Scenario-Based Reasoning (MANDATORY)
**⏱ Duration: 10 seconds**  
**Cumulative Time: 2:00**

### The Scenario
Read this verbatim:

**"A notebook works on your machine, but when someone else opens it and runs all cells, it fails with undefined variable errors. What kernel-related mistake likely caused this, and how would restarting and rerunning cells help prevent it?"**

### Expected Answer

Choose one of these styles (all are acceptable):

**Style A: Direct and concise (recommended for shorter timing)**

"The mistake was that I ran cells out of order when testing locally. Cell 5 might depend on Cell 2, but I ran them backwards. On my machine, Cell 2 was already run earlier, so Cell 5 worked. But when my colleague ran all cells from the top, the dependencies weren't met and Cell 5 failed. The fix: I should test by restarting the kernel and running all cells—if that works, then anyone can run my notebook successfully."

**Style B: More detailed (if you have time)**

"The issue is likely hidden kernel state from running cells out of order. I probably ran Cell 5 before Cell 2 running some cells manually, Cell 5 worked because Cell 2 was already in my kernel memory. But in a fresh kernel, Cell 2 hasn't run yet. To prevent this, I should always test my notebooks with 'Restart & Run All Cells'—this ensures dependencies are correct and the notebook works from scratch."

**Style C: Reference to the demo**

"This is exactly what I just demonstrated. In my notebook, Cell 4 depends on Cell 1, 2, and 3. If someone skipped Cell 1, Cell 4 would fail with a NameError. The best practice: before sharing any notebook, always restart the kernel and then run all cells. If it works from scratch, it'll work for anyone."

### Exact Script to Record

**[At 1:50-2:00] - Scenario answer (read one of the above styles)**

"The scenario is: a notebook works on your machine but fails for someone else with undefined variable errors. The mistake is likely running cells out of order locally. On my machine, variables were already in kernel memory from earlier executions, but my colleague ran a fresh kernel from top to bottom and hit undefined variables. The fix is to always test by restarting and running all cells before sharing. That's what I showed in the demo."

*Action: Look at camera while speaking. Speak clearly.*

---

## Recording Checklist

**Before You Record:**
- [ ] Microphone is on and unmuted
- [ ] Screen is focused on notebook
- [ ] Recording software is set to 720p or higher
- [ ] Timer or clock is visible (or use a phone to track time)
- [ ] You can see this script (print or second monitor)

**During Recording:**
- [ ] Speak clearly and at a moderate pace
- [ ] Don't rush through Segment 1 (viewers need to see cell structure)
- [ ] Pause briefly while cells are executing (don't talk over loading)
- [ ] Point/click to highlight what you're explaining
- [ ] Look at the camera (or imagine speaking to a friend)
- [ ] Stay within the timing for each segment (35s, 50s, 25s, 10s)

**Common Timing Pitfalls to Avoid:**
- Don't spend too long on Cell 1 execution (should be fast)
- Don't explain interruption too briefly—show 3+ iterations before interrupting
- Don't skip explaining why restart is important
- Do clearly read the scenario question before answering

**If You Go Over/Under Time:**
- Over time: Speed up your speaking slightly, skip less-important details
- Under time: Add more explanation to scenarios or show one more cell briefly
- Target is ~2 minutes; ±10 seconds is acceptable

---

## Post-Recording Checklist

**After You Finish Recording:**

- [ ] Review the video
  - [ ] Audio is clear (no background noise)
  - [ ] Video is visible (not too dark or blurry)
  - [ ] Timing is approximately 2 minutes
  - [ ] You covered all 4 segments (execute, interrupt, restart, scenario)
  - [ ] Screen is focused and readable (no accidental clicks visible)

- [ ] If satisfied:
  - [ ] Save video file with name: `MILESTONE-5-KERNEL-VIDEO.[mp4/mov/webm]`
  - [ ] Export final version (check recording software's export settings)
  - [ ] Upload to your hosting platform (Google Drive, YouTube, GitHub, etc.)
  - [ ] Get shareable link with view permissions
  - [ ] Test the link (open incognito/private window to verify)

- [ ] If not satisfied:
  - [ ] Identify what to redo (audio issues, timing too fast, etc.)
  - [ ] Re-record that segment or the entire video
  - [ ] Repeat until satisfied

---

## Segment Timing Reference

Use this table to track timing while recording:

| Segment | Duration | Cumulative | Content |
|---------|----------|------------|---------|
| Intro & Tour | 0:20 | 0:20 | "Hi! This is Milestone 5..." + cell structure tour |
| Run Cells 1-3 | 0:15 | 0:35 | Execute Cells 1, 2, 3 in order |
| Interrupt Intro | 0:05 | 0:40 | "This cell runs long..." |
| Run & Interrupt | 0:20 | 1:00 | Execute Cell 5, then Ctrl+C after 3 iterations |
| Verify State After Interrupt | 0:10 | 1:10 | Show preserved variables |
| Interrupt Concept | 0:15 | 1:25 | Explain why interrupt matters |
| Restart & Show Clearing | 0:10 | 1:35 | Kernel → Restart, verify state cleared |
| Scenario Answer | 0:25 | 2:00 | Answer the "undefined variable" scenario |

---

## Scenario Answer Tips

**Do:**
- ✓ Reference "running cells out of order" as the mistake
- ✓ Mention "kernel state" or "hidden state" affecting your code
- ✓ Reference testing with "Run All Cells" from a fresh restart
- ✓ Speak conversationally (this is recorded, not live)
- ✓ Make eye contact with camera (or imagine explaining to a friend)

**Don't:**
- ✗ Give a generic answer unrelated to kernel state
- ✗ Speak too fast or too slow
- ✗ Sound uncertain or apologetic
- ✗ Click around nervously—be calm and deliberate
- ✗ Skip the scenario question—it's a core requirement

**Example Scenario Answers to Avoid:**
- ❌ "I don't know, maybe the code was wrong?"
- ❌ "The other person's computer is different"
- ❌ "I forgot to save the file"

**Example Scenario Answers That Work:**
- ✅ "The mistake was that I ran cells out of order when testing locally. Cell 5 depended on variables from Cell 2, but I had already run Cell 2 in my kernel at some point, so Cell 5 worked for me. When my colleague ran all cells fresh, they hit the dependency error. The fix: test with 'Run All Cells' after restarting the kernel."
- ✅ "Hidden kernel state caused it. My colleague ran from a fresh start, but I had run cells randomly while working, so variables were already defined. To prevent this, always restart and run all cells before sharing to ensure the notebook is reproducible."

---

## Final Quality Checklist

Before submitting video:

- [ ] Video duration is 1:50–2:10 (approximately 2 minutes)
- [ ] Audio is clear and understandable
- [ ] Screen is readable (not too small, not blurry)
- [ ] Segment 1: Normal execution is demonstrated (35s)
- [ ] Segment 2: Interrupt is demonstrated (50s)
- [ ] Segment 3: Restart and state clearing is demonstrated (25s)
- [ ] Segment 4: Scenario question is answered (10s)
- [ ] Scenario answer references kernel state and execution order
- [ ] Video is exported in common format (MP4, MOV, WebM, etc.)
- [ ] Upload link is working and shareable

---

## Upload and Submission

**Video Hosting Options:**
- Google Drive (shareable link with "Viewer" permissions)
- YouTube (unlisted video, shareable link)
- GitHub (commit video file to branch—keep under 100MB)
- OneDrive or Dropbox (shareable link)
- Any platform that provides a view-only link

**Submission Instructions:**
1. Upload video to your chosen platform
2. Get the shareable link (test it works)
3. Create PR on GitHub for this milestone
4. Post video link in PR comments or assignment submission
5. Include PR link in your final submission

---

**Good luck with your recording! Remember: you're demonstrating kernel control and reproducibility discipline, not complex code. Keep it simple and clear.**
