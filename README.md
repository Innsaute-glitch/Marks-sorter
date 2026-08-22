# 📊 Marks Sorter

A simple but powerful terminal-based marks management tool built in Python.
Enter student marks in batches, and get them sorted with the highest and lowest instantly!

---

## ✨ Features

- 📥 **Batch Input** — Enter marks for multiple students at once, then add more batches as needed
- 🔢 **Type Choice Per Batch** — Choose integer marks or decimal marks for each new batch (`Y/N` prompt)
- 🔃 **Auto Sorting** — Automatically sorts all marks in ascending order at the end
- 🏆 **Max & Min Detection** — Instantly shows the highest and lowest marks
- ⚠️ **Input Validation** — Re-prompts on invalid numbers and invalid yes/no choices
- ⌨️ **Graceful Exit Support** — Handles both `Ctrl+C` (`KeyboardInterrupt`) and `Ctrl+Z` + Enter (`EOFError`) cleanly
- 🔁 **Multi-batch Support** — Add more students after the first batch without restarting

---

## 🚀 How to Use

**Requirements:** Python 3.x

**Run the script:**
```bash
python Marks_sorter.py
```

**Follow the prompts:**
1. Enter the number of students in your batch (must be greater than `0`)
2. Choose mark type: decimal marks (`Y`) or integer marks (`N`)
3. Enter each student's marks one by one
4. Choose whether to add more students (`y/n`)
5. View the final sorted list with max and min marks

**To exit anytime:** Press `Ctrl+C` — the script handles it cleanly 👍

---

## 📸 Sample Output

```
How many students are there? 4
Are the marks containing decimal points? (Y/N): N
Please enter the marks: 78
Please enter the marks: 92
Please enter the marks: 45
Please enter the marks: 88
Max number of students reached

Do you want to add more? (y/n): n
Getting the final data sorted...

Your final list is: [78, 92, 45, 88]
Sorting in ascending order...

[45, 78, 88, 92]
Maximum marks are: 92
Minimum marks are: 45

Thank You for using this script :)

And it's done! Thanks for using this script
```

---

## 🧠 Concepts Used

- Lists and list methods (`append`, `sort`)
- `while` loops and nested loops
- `try` / `except` for error handling (`ValueError`, `KeyboardInterrupt`, `EOFError`)
- f-strings
- State management with control variables
- `time.sleep()` for cleaner UX pacing

---

## 📬 Connect

If you have suggestions, improvements or just want to say hi — feel free to open an issue or drop a comment
