# Milestone 2: Video Walkthrough Guide
## ~2 Minute Screen Recording Guide

---

## RECORD THIS VIDEO (Total: ~2 minutes)

### Script Timeline

**Segment 1: Terminal Verification (45 seconds)**

1. Open PowerShell and position it prominently on screen
2. Say: "First, let's verify that Python is installed and working."
3. Type and execute: `python --version`
4. Say: "Here we can see Python [version number] is installed and accessible."
5. Say: "Next, we'll verify Conda for environment management."
6. Type and execute: `conda --version`
7. Say: "Conda version [number] is installed. Now let's activate the base environment."
8. Type and execute: `conda activate base`
9. Show the prompt changes (you should see "(base)" indicator)
10. Say: "Notice the prompt now shows (base) - this confirms our Conda environment is active."

---

**Segment 2: Jupyter Verification (50 seconds)**

1. Say: "Now let's verify Jupyter is working correctly."
2. Type: `jupyter notebook` (or `jupyter lab`)
3. Wait for browser to launch (show it opening)
4. Say: "Jupyter Notebook has launched successfully in the browser."
5. Show the Jupyter interface with file browser
6. Click "New" → "Python 3" to create new notebook
7. In first cell, type: `print("Jupyter is working!")`
8. Click Run button (or press Shift+Enter)
9. Show the output appears below the cell
10. Say: "The Python cell executed successfully - Jupyter is fully operational."
11. Close the browser tab (don't need to save)

---

**Segment 3: PR Walkthrough (20 seconds)**

1. Open browser to: https://github.com/kalviumcommunity/DS_sprint4/pull/new/feature/milestone-2-environment-verification
2. Show the branch name "feature/milestone-2-environment-verification"
3. Say: "This PR contains verification documentation and a sample Jupyter notebook that proves our environment is working. It includes Python version check, Conda environment test, and Jupyter execution test."
4. Show the files in the diff (ENVIRONMENT_VERIFICATION.md, jupyter-test-execution.ipynb, VERIFICATION_COMMANDS.txt)

---

## WHAT TO SHOW IN VIDEO

### ✅ Must Include:

- [ ] Python version command output
- [ ] Conda version command output
- [ ] Activated Conda environment (show prompt with "(base)")
- [ ] Jupyter Notebook/Lab launching in browser
- [ ] Python code cell executing successfully
- [ ] Output from executed cell visible
- [ ] Brief PR view explaining verification proof
- [ ] All within ~2 minutes

### Optional (If Time Allows):

- Show conda environment list with `conda env list`
- Show jupyter `--version` output
- Show multiple cells running in notebook

---

## VIDEO RECORDING TIPS

1. **Clear Audio**: Speak clearly, pause between sections
2. **Slow Pacing**: Move mouse slowly, give viewer time to see output
3. **Zoom**: Use browser zoom if terminal text is too small
4. **Cursor**: Make sure cursor movements are visible
5. **Success**: Celebrate briefly when things work ("Great, that's working!")

---

## EXACT COMMANDS TO RUN

Copy-paste these in order for your video:

```powershell
python --version
conda --version
conda activate base
jupyter notebook
```

In Jupyter cell:
```python
print("Jupyter is working!")
```

---

## EXAMPLE SCRIPT TO READ

Here's what to say verbally (adapt as needed):

---

**"Hi, welcome to my environment verification walkthrough. I'm going to demonstrate that Python, Conda, and Jupyter are all installed and working properly on my local machine.**

**First, let's check Python. I'll run python --version... [pause for command] Great, I have Python [version] installed.**

**Next, I'll verify Conda is installed. Running conda --version... [pause] Perfect, Conda is operational.**

**Now I'm going to activate my base Conda environment... [pause] Notice the prompt has changed to show (base) - this confirms the environment is active.**

**Let me launch Jupyter Notebook now... [wait for browser] Excellent, Jupyter has opened in the browser automatically.**

**Now I'll create a quick test. Clicking New → Python 3... I'll type a simple print statement... [type code] and run it... [execute cell] Perfect! The code executed successfully and the output appears below.**

**This PR documents our verification process with detailed checklists and a sample notebook. All three components - Python, Conda, and Jupyter - are working correctly and ready for data science work.**

**Total verification time: less than 2 minutes. The environment is production-ready."**

---

## AFTER RECORDING

- Save video file (MP4, WebM, or MOV format)
- Keep file size reasonable (< 100MB)
- Upload to: [Instructor's submission platform]
- Include: PR link in description or comment

---

## VIDEO SUBMISSION CHECKLIST

- [ ] Video recorded (~2 minutes)
- [ ] All three tools verified: Python, Conda, Jupyter
- [ ] Code executed successfully in Jupyter shown on screen
- [ ] PR overview briefly explained
- [ ] Audio is clear and understandable
- [ ] Terminal output clearly visible
- [ ] Jupyter interface clearly visible
- [ ] Ready to submit with PR link

---

**Status**: Script ready, command reference ready ✅  
**Next Step**: Record video walkthrough and submit both PR + video
