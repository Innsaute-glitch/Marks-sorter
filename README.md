# 📊 Marks Sorter

A simple but powerful terminal-based marks management tool built in Python.  
Enter student marks in batches, and get them sorted with the highest and lowest instantly!

---

## ✨ Features

- 📥 **Batch Input** — Enter marks for multiple students at once, then add more batches as needed
- 🔃 **Auto Sorting** — Automatically sorts all marks in ascending order at the end
- 🏆 **Max & Min Detection** — Instantly shows the highest and lowest marks
- ⚠️ **Full Error Handling** — Handles invalid inputs (letters, symbols, decimals) gracefully
- ⌨️ **Keyboard Interrupt Support** — Press `Ctrl+C` anytime for a clean, graceful exit (no ugly crashes!)
- 🔁 **Multi-batch Support** — Add more students after the first batch without restarting

---

## 🚀 How to Use

**Requirements:** Python 3.x

**Run the script:**
```bash
python Marks_sorter.py
```

**Follow the prompts:**
1. Enter the number of students in your first batch
2. Enter each student's marks one by one
3. Choose whether to add more students (`y/n`)
4. View the final sorted list with max and min marks!

**To exit anytime:** Press `Ctrl+C` — the script handles it cleanly 👍

---

## 📸 Sample Output

```
How many students are there? 4
Please enter the marks: 78
Please enter the marks: 92
Please enter the marks: 45
Please enter the marks: 88
Max number of students reached

Add more? (y/N): n

Your final list is: [78, 92, 45, 88]
Sorting in ascending order...

[45, 78, 88, 92]
Maximum marks are: 92
Minimum marks are: 45

Thanks for using this :)
```

---

## 🧠 Concepts Used

- Lists and list methods (`append`, `sort`, `len`)
- `while` loops and nested loops
- `try` / `except` for error handling (`ValueError`, `KeyboardInterrupt`)
- f-strings
- State management with control variables
- `time.sleep()` for cleaner UX pacing

---

## 📅 About

Built on **Day 4** of learning Python — part of my coding journey before starting college.  
No AI assistance — pure logic and learned commands! 🧑‍💻
---

## 📬 Connect

If you have suggestions, improvements or just want to say hi — feel free to open an issue or drop a comment
