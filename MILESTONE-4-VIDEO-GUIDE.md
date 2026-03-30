# Milestone 4: Video Walkthrough Guide
## Understanding Notebook Cells: Code vs Markdown (~2 Minutes)

---

## RECORD THIS VIDEO (Total: ~2 minutes)

### Video Timeline & Script

**Segment 1: Open Notebook & Show Structure (35 seconds)**

1. **Launch Jupyter and Open Sample Notebook**
   - Say: "I'm launching Jupyter Notebook to show the sample notebook that demonstrates Code and Markdown cells."
   - Show: `jupyter notebook`
   - Navigate to: `notebooks/` folder
   - Click on: `04-cell-types-demonstration.ipynb`
   - Show: Notebook opens with full content

2. **Scroll Through Structure**
   - Scroll slowly through notebook
   - Point to: Markdown title at top
   - Say: "Notice the notebook starts with a Markdown title explaining what we're learning."
   - Continue scrolling
   - Say: "Throughout the notebook, you see alternating Markdown sections explaining what's next, followed by Code cells that execute, followed by Markdown interpreting the results."

3. **Show Organization**
   - Point to: A Markdown cell with text formatting
   - Say: "These are Markdown cells - they contain formatted text, not code."
   - Point to: A Code cell with Python code
   - Say: "These are Code cells - they contain Python that actually runs."

---

**Segment 2: Demo - Execute Code & Render Markdown (50 seconds)**

1. **Show & Execute a Code Cell**
   - Scroll to: Code cell with `print("Welcome to Jupyter Notebooks!")`
   - Click on the cell
   - Say: "Let me click on this Code cell and execute it."
   - Press: Shift+Enter
   - Show: Output appears below cell
   - Say: "Notice the output appears right below. This happened because it's a Code cell - Python ran and produced output."

2. **Show a Markdown Cell Rendering**
   - Scroll to: A Markdown cell with heading and bullets
   - Point to formatted text
   - Say: "This is what a rendered Markdown cell looks like. The heading is formatted, bullets are styled. This is text meant to be read, not code to be executed."

3. **Demonstrate Cell Type Switching**
   - Right-click on a Code cell
   - Select: "Cell Type" → "Markdown" (or use Cell menu)
   - Show: The cell content changes appearance (code now shown as text)
   - Say: "I just switched this Code cell to Markdown. Notice the Python code is now just text - it won't run anymore."
   - Switch back to Code
   - Say: "Switching back to Code, and the cell is ready to execute again."

---

**Segment 3: Explain When to Use Each (25 seconds)**

Say this verbally (you can read from notes):

*"Let me explain when to use Code cells versus Markdown cells.*

*Use **Code cells** when you want to execute Python - that's where you import libraries, load data, perform calculations, anything that needs to run and produce output.*

*Use **Markdown cells** to explain what your code does and why. Before each Code cell, I write a Markdown cell explaining 'what are we doing and why?' After the Code cell executes, another Markdown cell explains 'what do these results mean?'*

*This separation is critical. A Code cell shows WHAT you did. A Markdown cell explains WHY you did it and SO WHAT - what are the implications?*

*This structure makes notebooks readable for teammates, easier to review, and professional."*

---

**Segment 4: Point Out Professional Structure (10 seconds)**

1. **Highlight the Pattern**
   - Scroll to show a few sections
   - Say: "Every section follows the same pattern: Markdown explains the purpose, Code executes the logic, Markdown interprets the results."
   - Point to: Multiple sections showing this pattern
   - Say: "This is professional notebook structure - it separates explanation from execution, making the notebook a proper document, not just a code dump."

---

## WHAT TO SHOW IN VIDEO

### ✅ MUST INCLUDE:

- [ ] Sample notebook opened in Jupyter
- [ ] Scroll through notebook structure visible
- [ ] Markdown cells shown (with formatting - headings, bullets)
- [ ] Code cells shown (with Python code)
- [ ] At least one Code cell executed (Shift+Enter)
- [ ] Output from executed cell visible
- [ ] At least one Markdown cell clearly visible and formatted
- [ ] Cell type switched (Code ↔ Markdown)
- [ ] Explained when to use Code cells (execution/logic)
- [ ] Explained when to use Markdown cells (explanation/narrative)
- [ ] Showed why separation matters (readability, professionalism)
- [ ] Showed the pattern: Markdown-Code-Markdown structure

### OPTIONAL (If Time Allows):

- Show running multiple cells in sequence
- Show creating a new Markdown cell
- Show creating a new Code cell
- Demonstrate bullet formatting in Markdown
- Show commenting vs Markdown explanation difference

---

## EXACT SEQUENCE FOR VIDEO

Follow this order:

```
1. Launch Jupyter
   Command: jupyter notebook

2. Navigate to notebooks/
   Click: 📁 notebooks/

3. Open notebook
   Click: 04-cell-types-demonstration.ipynb

4. Scroll slowly through notebook (show structure)
   
5. Find a Code cell with print statement
   Click on it
   Press Shift+Enter
   Show output

6. Find a Markdown cell
   Point to formatted text

7. Right-click on a Code cell
   Select Cell Type → Markdown
   Show text instead of code

8. Change back to Code
   Right-click → Cell Type → Code
   Show it's ready to run again

9. Explain verbally when to use each

10. Point out the pattern in the notebook
```

---

## VIDEO SCRIPT (Read This)

Here's what to say verbally:

---

**"Hi, this is my Milestone 4 walkthrough - Understanding Notebook Cells: Code vs Markdown.**

**I'm going to demonstrate the sample notebook I created that shows the best practices for using both cell types.**

**[Launch Jupyter] First, I'll open Jupyter and navigate to my notebooks folder...**

**[Show notebook] Here's the notebook with clear examples of Code and Markdown cells. Let me scroll through to show the structure...**

**Notice as I scroll, the notebook alternates between Markdown sections that explain what we're doing, and Code sections that execute Python. This is professional notebook structure.**

**Let me execute one of the Code cells to show how it works. [Click on cell, Shift+Enter] See the output appears below - that's because it's a Code cell running Python.**

**Now look at this Markdown cell. [Point] It's formatted with a heading and bullet points. This text is meant to be read by humans, not executed as code.**

**Let me demonstrate switching cell types. [Right-click cell] I'll change this Code cell to Markdown... [select Markdown] Notice the Python code is now just text sitting there. It won't run anymore. [Switch back to Code] Changing back to Code, and it's executable again.**

**Now, why does this matter? Code cells show WHAT you did - the execution. Markdown cells explain WHY and SO WHAT - the reasoning and implications.**

**A beginner mistake is writing everything as code comments. A professional approach uses Markdown to explain the narrative and Code to execute logic. You see this pattern throughout: Markdown introduces a section, Code implements it, Markdown interprets the results.**

**This separation makes notebooks readable, reviewable, and maintainable. That's Milestone 4 - understanding cell types and structure!"**

---

## TIMING FOR VIDEO

| Segment | Duration | Content |
|---------|----------|---------|
| 1. Open & Structure | 35s | Launch Jupyter, show structure |
| 2. Demo Execution | 50s | Run Code, show Markdown, switch type |
| 3. Explanation | 25s | Explain when to use each |
| 4. Summary | 10s | Show professional pattern |
| **TOTAL** | **~2 min** | **Complete walkthrough** |

---

## RECORDING TIPS

1. **Speak Clearly**: Enunciate, pause between thoughts
2. **Move Slowly**: Let viewers see cell transitions
3. **Zoom if Needed**: Make text visible (Ctrl + in browser)
4. **Point to Elements**: Use cursor to highlight what you're discussing
5. **Pause Before Executing**: Say "let me execute this" then press Shift+Enter
6. **Let Output Show**: Wait a second for output to appear before continuing

---

## AFTER RECORDING

- Save video file (MP4, WebM, or MOV)
- Keep file size reasonable (< 100MB)
- Check audio is clear
- Verify timing is ~2 minutes

---

## VIDEO SUBMISSION CHECKLIST

- [ ] Notebook opened successfully
- [ ] Structure clearly visible (scrolling shown)
- [ ] Code cell executed with output shown
- [ ] Markdown cell clearly visible and formatted
- [ ] Cell type switched (at least once)
- [ ] Explained Code cell purpose verbally
- [ ] Explained Markdown cell purpose verbally
- [ ] Explained why separation matters verbally
- [ ] Pointed out professional pattern
- [ ] Total time: ~2 minutes
- [ ] Audio clear and understandable
- [ ] Ready to submit with PR link

---

**Status**: Script ready, timing confirmed ✅  
**Next Step**: Record video walkthrough and submit both PR + video
