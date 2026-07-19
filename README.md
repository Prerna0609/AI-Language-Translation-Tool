# 🌐 AI Language Translation Tool

A beginner-friendly desktop application built with **Python** and **CustomTkinter** that translates text between multiple languages in real time, powered by the **deep-translator** library (Google Translate engine).

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-2CC985)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## ✨ Features

- Clean, modern dark-themed GUI (built with CustomTkinter)
- Translate between **English, Hindi, Marathi, Japanese, French, and German**
- Auto-detect source language option
- Swap source/target language with one click
- Copy translated text to clipboard
- Clear input/output with one click
- Friendly error messages (empty input, network/translation failures)
- Clean, heavily commented code — great for learning

---

## 🗂️ Project Structure

```
AI-Language-Translation-Tool/
│
├── translator_app.py     # Main application (GUI + logic)
├── requirements.txt      # Python dependencies
├── README.md              # Project documentation (this file)
└── .gitignore              # Files/folders Git should ignore
```

---

## ⚙️ Requirements

- Python **3.12+**
- Internet connection (required for live translation via Google Translate)

---

## 🛠️ Installation

1. **Clone or download** this repository:
   ```bash
  git clone https://github.com/Prerna0609/AI-Language-Translation-Tool.git
   ```

2. **(Recommended) Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** `tkinter` (which CustomTkinter is built on) ships with most standard Python installations. If you get a `ModuleNotFoundError: No module named 'tkinter'` on Linux, install it separately:
   > ```bash
   > sudo apt-get install python3-tk
   > ```

---

## ▶️ How to Run

From inside the project folder, run:

```bash
python translator_app.py
```

The application window will open. Then:

1. Select a **source language** (or leave it on "Auto Detect").
2. Select a **target language**.
3. Type or paste text into the **left text box**.
4. Click **Translate**.
5. View the result in the **right text box**.
6. Use **Copy Output** to copy the translation, or **Clear** to reset both boxes.

---

## 🧠 Code Overview (Plain-English Explanation)

The entire app lives in `translator_app.py` and is organized into clear sections:

1. **Imports** — Loads `customtkinter` for the GUI, `deep_translator` for the actual translation, and `messagebox` for pop-up alerts.
2. **App Configuration** — Sets the dark theme and defines the color palette (background, accent, text, error colors) used throughout the app.
3. **Supported Languages** — A simple Python dictionary mapping human-readable language names (e.g. "Hindi") to the language codes Google Translate expects (e.g. "hi").
4. **`TranslatorApp` class** — The whole application is one class that inherits from `ctk.CTk` (the main window). It's broken into small, well-named methods:
   - `_build_header()` — Adds the title and subtitle at the top.
   - `_build_language_selector_bar()` — Adds the "From" / "To" dropdowns and the swap button.
   - `_build_text_areas()` — Adds the input and output text boxes side by side.
   - `_build_action_buttons()` — Adds the Translate, Copy, and Clear buttons.
   - `_build_footer()` — Adds a small status label for feedback messages.
5. **Logic methods** (the "brains" of the app):
   - `swap_languages()` — Swaps the source and target language selections.
   - `translate_text()` — Reads the input text, validates it isn't empty, calls the `GoogleTranslator` from deep-translator, and displays the result. Wrapped in a `try/except` block so any error (e.g. no internet) shows a friendly pop-up instead of crashing.
   - `copy_output()` — Copies the translated text to your system clipboard.
   - `clear_text()` — Empties both text boxes and resets the status message.
6. **Program entry point** — The `if __name__ == "__main__":` block creates the app and starts it. This is the standard way Python scripts are launched.

---

## 🚧 Error Handling

The app handles the following cases gracefully:

- **Empty input** → Shows an error pop-up asking the user to type something before translating.
- **Translation failure** (e.g. no internet connection, service unavailable) → Catches the exception and shows a clear error message instead of crashing.
- **Swap with Auto Detect selected** → Informs the user they must pick a specific source language first.
- **Copying with no output** → Warns the user there's nothing to copy yet.

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| [customtkinter](https://github.com/TomSchimansky/CustomTkinter) | Modern-looking GUI widgets built on top of Tkinter |
| [deep-translator](https://github.com/nidhaloff/deep-translator) | Simple interface to Google Translate and other translation engines |

---

## 🚀 Possible Future Improvements

- Add more languages
- Add text-to-speech playback for translated text
- Add a "translation history" panel
- Add drag-and-drop file translation (.txt)

---

## 📄 License

This project is provided for educational purposes as part of an AI Internship project.

---

## 🙋 Author
Author: Prerna Zende
Built as part of an AI Internship project.

