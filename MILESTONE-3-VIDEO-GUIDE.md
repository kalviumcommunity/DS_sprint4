# Milestone 3: Video Walkthrough Guide
## Launching Jupyter & Understanding Home Interface (~2 Minutes)

---

## RECORD THIS VIDEO (Total: ~2 minutes)

### Video Timeline & Script

**Segment 1: Launching Jupyter Correctly (40 seconds)**

1. **Show Terminal/PowerShell Window**
   - Say: "I'm going to launch Jupyter Notebook from the correct project directory."
   - Show: `cd c:\sprint-4-ds-lifecycle`
   - Execute command
   - Say: "I've navigated to my project folder."

2. **Verify Location**
   - Show: `pwd`
   - Output: `C:\sprint-4-ds-lifecycle`
   - Say: "I can confirm I'm in the right directory with the pwd command."

3. **List Files to Show Structure**
   - Show: `dir`
   - Point to: notebooks/, data/, scripts/ folders
   - Say: "Here's my project structure - notebooks folder for Jupyter files, data folder for datasets, scripts for Python code."

4. **Launch Jupyter**
   - Show: `jupyter notebook`
   - Wait for browser to open (5 seconds)
   - Say: "Launching Jupyter Notebook now... and the browser opens automatically showing the Jupyter Home interface."

---

**Segment 2: Home Interface Walkthrough (45 seconds)**

1. **Show Breadcrumb**
   - Point to: `/c:/sprint-4-ds-lifecycle` (or Windows equivalent)
   - Say: "The breadcrumb at the top shows I'm in the sprint-4-ds-lifecycle folder. This is my working directory - where Jupyter looks for files."

2. **Show File Browser**
   - Point to: 📁 `notebooks/`
   - Point to: 📁 `data/`
   - Point to: 📁 `scripts/`
   - Point to: 📄 `JUPYTER_HOME_INTERFACE_GUIDE.md`
   - Say: "I can see all my project folders and files right here. Folders are clickable - let me navigate into the notebooks folder."

3. **Click into Notebooks Folder**
   - Click: `📁 notebooks/`
   - Breadcrumb updates to: `/c:.../notebooks`
   - Say: "Notice the breadcrumb changed - I'm now inside the notebooks folder. The New button will create files here, not in the project root."

4. **Show Navigation Buttons**
   - Point to: **New** button
   - Say: "This New button creates new notebooks HERE, in the notebooks folder. If I go back to the main folder, new notebooks would be created there instead. That's why launch directory and folder organization matter."

5. **Go Back to Root**
   - Click breadcrumb or back button: `sprint-4-ds-lifecycle`
   - Say: "I'm back in the project root. This is where I launched Jupyter from."

---

**Segment 3: Notebook Creation & Execution (20 seconds)**

1. **Create New Notebook**
   - Navigate to: `notebooks/` folder
   - Click: **New** → **Python 3**
   - Say: "Creating a new notebook in the notebooks folder."

2. **Show Notebook Opens**
   - New tab opens with blank notebook
   - Say: "The notebook editor opens in a new tab."

3. **Write and Execute Code**
   - In first cell, type:
     ```python
     import os
     print(f"Working directory: {os.getcwd()}")
     print(f"Files here: {os.listdir('.')[:3]}")
     ```
   - Execute: Shift+Enter
   - Show output appears below
   - Say: "I've executed Python code. The output shows my working directory is c:\sprint-4-ds-lifecycle and lists files in that folder."

4. **Show File Saved**
   - Go back to file browser tab (Jupyter home)
   - Show new notebook appears in `notebooks/` folder with name like `Untitled.ipynb`
   - Say: "The notebook was automatically saved in the notebooks folder. This proves the file is in the right place."

---

**Segment 4: Scenario-Based Reasoning (15 seconds)**

**Read this script verbally in the video:**

*"Let me answer the scenario question: 'You open a notebook and realize it cannot find a dataset file that exists on your machine. How would you diagnose and fix this using understanding of Jupyter's file structure?'*

*First, I'd understand that Jupyter loads files relative to its working directory - where I launched Jupyter from. In my case, that's the project root. If a file exists but my notebook can't find it, I'd use `os.getcwd()` in a notebook cell to see what Jupyter thinks is the current directory.*

*Second, I'd check the actual file path. If my file is in the data/ folder but I wrote just 'data.csv' without the folder path, Jupyter won't find it. I'd need to use 'data/data.csv' or better yet, `os.path.join('data', 'data.csv')`.*

*Third, I'd verify my file actually exists at that path with `os.listdir('data/')` to see what files are available.*

*This is why workspace awareness matters: understanding the launch directory, navigating folders intentionally, and using relative paths from the working directory prevents file-not-found errors and makes code work for any team member."*

---

## WHAT TO SHOW IN VIDEO

### ✅ MUST INCLUDE:

- [ ] Terminal showing: `cd c:\sprint-4-ds-lifecycle`
- [ ] Terminal showing: `pwd` (confirms correct directory)
- [ ] Terminal showing: `dir` (shows project structure)
- [ ] Terminal showing: `jupyter notebook`
- [ ] Browser opening with Jupyter Home interface
- [ ] Breadcrumb in Jupyter showing: `/c:/sprint-4-ds-lifecycle`
- [ ] Jupyter file browser showing: notebooks/, data/, scripts/ folders
- [ ] Navigation: Click into notebooks/ folder (breadcrumb updates)
- [ ] Creation: New → Python 3 notebook
- [ ] Execution: Code cell runs successfully
- [ ] Output visible: Working directory and file list
- [ ] File appears: New notebook saved in notebooks/ folder
- [ ] Scenario answer: Verbal explanation (15 seconds)

### OPTIONAL (If Time Allows):

- Show renaming notebook to descriptive name
- Show how to use os.path.join() in code
- Click on other files to show they're viewable
- Show what happens if you navigate outside valid areas

---

## EXACT COMMANDS FOR VIDEO

Copy-paste these in order:

```powershell
# Terminal commands
cd c:\sprint-4-ds-lifecycle
pwd
dir
jupyter notebook
```

**In Jupyter code cell:**
```python
import os
print(f"Working directory: {os.getcwd()}")
print(f"Files here: {os.listdir('.')[:5]}")
```

---

## VIDEO TIMING BREAKDOWN

| Segment | Duration | Content |
|---------|----------|---------|
| 1. Launch | 40s | Terminal → Jupyter opens |
| 2. Home Interface | 45s | File browser walkthrough |
| 3. Notebook Creation | 20s | Create + execute Python |
| 4. Scenario Answer | 15s | Explain diagnosis approach |
| **TOTAL** | **~2 min** | **Complete walkthrough** |

---

## EXAMPLE SCRIPT TO READ

Here's what to say verbally (adapt as needed):

---

**"Hi, this is my Milestone 3 walkthrough - Launching Jupyter Notebook and Understanding the Home Interface.**

**[Show terminal] First, I'm going to demonstrate the correct way to launch Jupyter. I'll navigate to my project directory using cd c:\sprint-4-ds-lifecycle. Let me verify I'm in the right place with pwd... yes, I'm in the sprint-4-ds-lifecycle folder.**

**Next, let me show the project structure with dir. I can see notebooks, data, and scripts folders - this is the correct organization for a data science project.**

**Now I'll launch Jupyter with jupyter notebook... [wait for browser] and here's the Jupyter Home interface.**

**Notice the breadcrumb at the top shows /c:/sprint-4-ds-lifecycle - this is my working directory, where Jupyter will look for and save files. I can see my project folders in the file browser. Let me click into the notebooks folder... the breadcrumb updates to show I'm now inside notebooks. This is important because the New button will create files HERE, not scattered randomly across the disk.**

**Now I'll create a new Python notebook... [click New → Python 3] The notebook editor opens. Let me write a quick test to verify the working directory...**

**[Write code] I've imported os and printed the working directory. Let me execute this...**

**[Run cell] Perfect! The output confirms I'm in the project root and shows the files available. The notebook automatically saved in the notebooks folder - I can see it in the file browser.**

**Now for the scenario question about file-not-found errors. The key insight is that Jupyter looks for files relative to its launch directory. If a dataset file isn't found, I'd use os.getcwd() to verify the working directory, then os.listdir() to check what files actually exist at that path. Using properly organized folders and relative paths like 'data/dataset.csv' instead of hardcoded paths ensures the code works for everyone. This is why workspace awareness and intentional file organization are critical in collaborative data science projects.**

**That's Milestone 3 - workspace awareness complete!"**

---

## AFTER RECORDING

- Save video file (MP4, WebM, or MOV format)
- Keep file size reasonable (< 100MB)
- Check audio is clear
- Timing is ~2 minutes (not more)

---

## VIDEO SUBMISSION CHECKLIST

- [ ] Terminal commands visible
- [ ] Directory navigation clear
- [ ] Jupyter opens in browser
- [ ] Home interface walkthrough complete
- [ ] Notebook created in correct folder
- [ ] Python code executed successfully
- [ ] Output shows correct working directory
- [ ] Scenario answered verbally (15 seconds)
- [ ] Total time: ~2 minutes
- [ ] Audio clear and understandable
- [ ] Ready to submit with PR link

---

**Status**: Script ready, timing confirmed ✅  
**Next Step**: Record video walkthrough and submit both PR + video
