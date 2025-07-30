HTML File - A Step-by-Step Guide

This guide will help you make text changes to the HTML file without any coding knowledge. You'll only be changing text content, not the code that makes the charts and data work.

### Step 1: Download the HTML File from GitHub

1. **Access the GitHub Repository**
   - Open your web browser and go to the project's GitHub page
   - Find the v7 dashboard HTML file

2. **Download the File**
   - Click on the HTML filename (`nepal_dashboard_v7.html`)
   - The page will show the code content
   - Click the **"Raw"** button in the top right corner
   - Right-click on the page and select **"Save as"**
   - Save it to an easy-to-find location on your computer (like your Desktop)
   - Make sure the file extension is `.html`

### Step 2: Choose the Right Editor

For an 8,000-line HTML file, I recommend using one of these editors:

1. **Visual Studio Code (Recommended)**
   - Free download: https://code.visualstudio.com/
   - After installing, right-click the HTML file and select "Open with Code"
   - Benefits: Search function, color highlighting, auto-save

2. **Notepad++ (For Windows Users)**
   - Free download: https://notepad-plus-plus.org/
   - Lightweight and simple

3. **Sublime Text**
   - Download: https://www.sublimetext.com/
   - Clean interface with powerful search

### Step 3: Use Search to Quickly Find Text

#### Searching in Visual Studio Code:
1. Press **Ctrl + F** (Mac: Cmd + F) to open the search box
2. Type the specific text Paul mentioned
3. Press Enter to jump to that location
4. Change the text content (be careful to only change the text, not the HTML tags)

#### Search Tips:
- Search for unique phrases or specific headings
- If there are multiple matches, press F3 or Enter to go to the next one
- Use **Ctrl + H** (Mac: Cmd + H) for find and replace

### Step 4: What You Can and Cannot Change

#### ✅ SAFE to Change:
```html
<!-- Original -->
<h1>Community Wellbeing Dashboard</h1>
<!-- Changed to -->
<h1>Nepal Community Wellbeing Survey Results</h1>

<!-- Original -->
<p>Total Responses: 587</p>
<!-- Changed to -->
<p>Total Responses: 560</p>
```

#### ❌ DO NOT Change:
- HTML tags (like `<h1>`, `<p>`, `<div>`)
- Attributes (like `class="header"`, `id="chart"`)
- JavaScript code (usually inside `<script>` tags)
- CSS styles (usually inside `<style>` tags)

### Step 5: Using AI Tools to Help

1. **Use Claude or ChatGPT for Assistance**
   - Copy the original text Paul wants changed
   - Ask: "I need to change [original text] to [new text] in an HTML file. What should I search for?"

2. **Verify Your Changes**
   - After making changes, copy the code snippet
   - Ask AI: "I changed this code from [original] to [modified]. Is this correct?"

3. **Bulk Changes**
   - If you need to change the same text in multiple places
   - Ask AI: "I need to change all instances of 'Survey 2024' to 'Survey 2025'. How should I do this?"

### Step 6: Save and Test

1. **Save the File**
   - Press **Ctrl + S** (Mac: Cmd + S) to save
   - Keep the original filename

2. **Test in Browser**
   - Double-click the HTML file to open it in your browser
   - Check that your text changes appear correctly
   - Ensure charts and other features still work

### Step 7: Troubleshooting Common Issues

#### If You Can't Find the Text:
1. The text might be in JavaScript code
2. Try searching without punctuation
3. Search for key words only, not full sentences

#### If the Page Looks Broken After Changes:
1. Press **Ctrl + Z** to undo
2. Check if you accidentally deleted quotes or tags
3. Compare your changed code with the original

### Practical Search Examples

For common changes Paul might request:

1. **Changing Titles**
   - Search for: `<h1>` or the specific title text
   
2. **Changing Statistics**
   - Search for: `Total Responses` or `587`
   
3. **Changing Dates**
   - Search for: `2024` or `Survey Period`

4. **Changing Descriptions**
   - Search for unique phrase fragments

### Create a Change Log

I recommend creating an Excel spreadsheet to track all changes:

| Original Text | New Text | Search Keywords | Status |
|--------------|----------|-----------------|---------|
| Total Responses: 587 | Total Responses: 560 | Search "587" | ✓ |
| Survey 2024 | Survey 2025 | Search "Survey 2024" | ✓ |
| Community Dashboard | Community Wellbeing Dashboard | Search "<h1>" | ✓ |

### Final Tips

1. **Back Up First**: Make a copy of the original file before making any changes
2. **Change One Thing at a Time**: Make one change, test it, then continue
3. **Document Everything**: Keep all of Paul's change requests in one place
4. **Save Frequently**: Save after every few changes

If you encounter any problems:
- Take a screenshot of any error messages
- Save before/after code snippets for comparison
- Ask for help with specific examples

### Quick Reference Card

**Opening Files:**
- Right-click → Open with → VS Code

**Searching:**
- Find: Ctrl + F (Cmd + F on Mac)
- Find & Replace: Ctrl + H (Cmd + H on Mac)
- Next result: F3 or Enter

**Saving:**
- Save: Ctrl + S (Cmd + S on Mac)
- Undo: Ctrl + Z (Cmd + Z on Mac)

**Remember:**
- Only change text between `>` and `<` symbols
- Never delete HTML tags
- When in doubt, make a backup first

With this guide, you can confidently make all the text changes Paul needs without worrying about breaking the code!
