"""
AI Language Translation Tool
-----------------------------
A beginner-friendly desktop app that translates text between multiple
languages using the free Google Translate engine (via the deep-translator
library) and a modern GUI built with CustomTkinter.

Author: (Your Name)
"""

# ---------------------------------------------------------------------------
# 1. IMPORTS
# ---------------------------------------------------------------------------
# customtkinter -> gives us modern-looking buttons, boxes, dropdowns, etc.
# deep_translator -> the library that actually talks to Google Translate.
# tkinter.messagebox -> used to show pop-up error/success messages.
# ---------------------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
from deep_translator import GoogleTranslator


# ---------------------------------------------------------------------------
# 2. APP CONFIGURATION (colors, appearance, fonts)
# ---------------------------------------------------------------------------
# CustomTkinter lets us set a "theme" for the whole app.
# "dark" mode + a "blue" color theme gives a clean, professional look.
# ---------------------------------------------------------------------------
ctk.set_appearance_mode("dark")          # "dark", "light", or "system"
ctk.set_default_color_theme("blue")      # built-in professional blue theme

# A small custom color palette we reuse throughout the app.
BG_COLOR = "#1e1e2e"          # main window background
CARD_COLOR = "#282a3a"        # panels / frames background
ACCENT_COLOR = "#4A9DFF"      # buttons / highlights
ACCENT_HOVER = "#357ae8"      # button hover color
TEXT_COLOR = "#e6e6e6"        # normal text
ERROR_COLOR = "#ff5c5c"       # error message color

# ---------------------------------------------------------------------------
# 3. SUPPORTED LANGUAGES
# ---------------------------------------------------------------------------
# This dictionary maps a friendly display name (shown in the dropdown)
# to the language code that Google Translate understands.
# You can add more languages here later if you want.
# ---------------------------------------------------------------------------
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Japanese": "ja",
    "French": "fr",
    "German": "de",
}

# deep-translator uses the special code "auto" to mean
# "detect the source language automatically".
SOURCE_LANGUAGES = {"Auto Detect": "auto", **LANGUAGES}


# ---------------------------------------------------------------------------
# 4. MAIN APPLICATION CLASS
# ---------------------------------------------------------------------------
# We put everything inside a class so the code stays organized.
# Think of this class as "the whole app" - it builds the window,
# places all the widgets (boxes, buttons, dropdowns) and defines
# what happens when the user clicks something.
# ---------------------------------------------------------------------------
class TranslatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()  # sets up the base CTk window

        # ---------------- Window basics ----------------
        self.title("AI Language Translation Tool")
        self.geometry("900x600")
        self.minsize(760, 520)
        self.configure(fg_color=BG_COLOR)

        # Build the interface (split into small helper methods below).
        self._build_header()
        self._build_language_selector_bar()
        self._build_text_areas()
        self._build_action_buttons()
        self._build_footer()

    # -----------------------------------------------------------------
    # HEADER: Just a title label at the top of the app.
    # -----------------------------------------------------------------
    def _build_header(self):
        header = ctk.CTkLabel(
            self,
            text="🌐 AI Language Translation Tool",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color=TEXT_COLOR,
        )
        header.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Translate text instantly between multiple languages",
            font=ctk.CTkFont(size=13),
            text_color="#9a9ab0",
        )
        subtitle.pack(pady=(0, 15))

    # -----------------------------------------------------------------
    # LANGUAGE SELECTOR BAR: source dropdown, swap icon, target dropdown
    # -----------------------------------------------------------------
    def _build_language_selector_bar(self):
        bar = ctk.CTkFrame(self, fg_color=CARD_COLOR, corner_radius=12)
        bar.pack(fill="x", padx=20, pady=(0, 15))

        # --- Source language dropdown ---
        ctk.CTkLabel(bar, text="From:", text_color=TEXT_COLOR).grid(
            row=0, column=0, padx=(15, 5), pady=15, sticky="w"
        )
        self.source_lang_var = ctk.StringVar(value="Auto Detect")
        self.source_dropdown = ctk.CTkOptionMenu(
            bar,
            values=list(SOURCE_LANGUAGES.keys()),
            variable=self.source_lang_var,
            fg_color=ACCENT_COLOR,
            button_color=ACCENT_COLOR,
            button_hover_color=ACCENT_HOVER,
        )
        self.source_dropdown.grid(row=0, column=1, padx=5, pady=15, sticky="w")

        # --- Swap button (swaps source & target languages) ---
        swap_btn = ctk.CTkButton(
            bar,
            text="⇄",
            width=40,
            fg_color="transparent",
            border_width=1,
            border_color=ACCENT_COLOR,
            hover_color=CARD_COLOR,
            command=self.swap_languages,
        )
        swap_btn.grid(row=0, column=2, padx=10, pady=15)

        # --- Target language dropdown ---
        ctk.CTkLabel(bar, text="To:", text_color=TEXT_COLOR).grid(
            row=0, column=3, padx=(5, 5), pady=15, sticky="w"
        )
        self.target_lang_var = ctk.StringVar(value="Hindi")
        self.target_dropdown = ctk.CTkOptionMenu(
            bar,
            values=list(LANGUAGES.keys()),
            variable=self.target_lang_var,
            fg_color=ACCENT_COLOR,
            button_color=ACCENT_COLOR,
            button_hover_color=ACCENT_HOVER,
        )
        self.target_dropdown.grid(row=0, column=4, padx=5, pady=15, sticky="w")

    # -----------------------------------------------------------------
    # TEXT AREAS: input box (left) and output box (right)
    # -----------------------------------------------------------------
    def _build_text_areas(self):
        text_frame = ctk.CTkFrame(self, fg_color="transparent")
        text_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Make both columns share space equally.
        text_frame.grid_columnconfigure(0, weight=1)
        text_frame.grid_columnconfigure(1, weight=1)
        text_frame.grid_rowconfigure(1, weight=1)

        # --- Input box (left side) ---
        ctk.CTkLabel(
            text_frame, text="Enter text", text_color=TEXT_COLOR,
            font=ctk.CTkFont(size=14, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.input_textbox = ctk.CTkTextbox(
            text_frame,
            fg_color=CARD_COLOR,
            text_color=TEXT_COLOR,
            corner_radius=10,
            wrap="word",
            font=ctk.CTkFont(size=14),
        )
        self.input_textbox.grid(row=1, column=0, sticky="nsew", padx=(0, 10))

        # --- Output box (right side) ---
        ctk.CTkLabel(
            text_frame, text="Translation", text_color=TEXT_COLOR,
            font=ctk.CTkFont(size=14, weight="bold")
        ).grid(row=0, column=1, sticky="w", pady=(0, 5))

        self.output_textbox = ctk.CTkTextbox(
            text_frame,
            fg_color=CARD_COLOR,
            text_color=TEXT_COLOR,
            corner_radius=10,
            wrap="word",
            font=ctk.CTkFont(size=14),
        )
        self.output_textbox.grid(row=1, column=1, sticky="nsew", padx=(10, 0))
        # Output box should not be typed in directly by the user.
        self.output_textbox.configure(state="disabled")

    # -----------------------------------------------------------------
    # ACTION BUTTONS: Translate, Copy, Clear
    # -----------------------------------------------------------------
    def _build_action_buttons(self):
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=(0, 10))

        self.translate_btn = ctk.CTkButton(
            button_frame,
            text="Translate",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=ACCENT_COLOR,
            hover_color=ACCENT_HOVER,
            command=self.translate_text,
            height=40,
            width=150,
        )
        self.translate_btn.pack(side="left", padx=(0, 10))

        self.copy_btn = ctk.CTkButton(
            button_frame,
            text="Copy Output",
            font=ctk.CTkFont(size=14),
            fg_color="#3a3d52",
            hover_color="#4a4d66",
            command=self.copy_output,
            height=40,
            width=150,
        )
        self.copy_btn.pack(side="left", padx=(0, 10))

        self.clear_btn = ctk.CTkButton(
            button_frame,
            text="Clear",
            font=ctk.CTkFont(size=14),
            fg_color="#3a3d52",
            hover_color="#4a4d66",
            command=self.clear_text,
            height=40,
            width=150,
        )
        self.clear_btn.pack(side="left")

    # -----------------------------------------------------------------
    # FOOTER: small status label to show messages (e.g. "Translating...")
    # -----------------------------------------------------------------
    def _build_footer(self):
        self.status_label = ctk.CTkLabel(
            self, text="", text_color="#9a9ab0", font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(pady=(0, 10))

    # ===================================================================
    # 5. LOGIC / EVENT HANDLER METHODS
    # ===================================================================

    def swap_languages(self):
        """Swap the selected source and target languages."""
        current_source = self.source_lang_var.get()
        current_target = self.target_lang_var.get()

        # "Auto Detect" cannot become a target language, so we skip the
        # swap in that case and just let the user know.
        if current_source == "Auto Detect":
            messagebox.showinfo(
                "Cannot Swap",
                "Please choose a specific source language (not Auto Detect) to swap.",
            )
            return

        self.source_lang_var.set(current_target)
        self.target_lang_var.set(current_source)

    def translate_text(self):
        """
        Reads the text from the input box, sends it to Google Translate
        (through deep-translator), and shows the result in the output box.
        """
        # Step 1: Get the text the user typed, removing extra spaces.
        input_text = self.input_textbox.get("1.0", "end").strip()

        # Step 2: Validate - make sure the user actually typed something.
        if not input_text:
            messagebox.showerror("Input Error", "Please enter some text to translate.")
            return

        # Step 3: Convert the friendly language names into language codes.
        source_name = self.source_lang_var.get()
        target_name = self.target_lang_var.get()
        source_code = SOURCE_LANGUAGES[source_name]
        target_code = LANGUAGES[target_name]

        # Step 4: Show a "working on it" message while we translate.
        self.status_label.configure(text="Translating...", text_color="#9a9ab0")
        self.update_idletasks()  # forces the UI to refresh immediately

        # Step 5: Try to translate. Any network/library error is caught
        # so the app never crashes - it just shows a friendly message.
        try:
            translated = GoogleTranslator(
                source=source_code, target=target_code
            ).translate(input_text)

            if not translated:
                raise ValueError("No translation was returned.")

            # Step 6: Display the result in the (read-only) output box.
            self.output_textbox.configure(state="normal")
            self.output_textbox.delete("1.0", "end")
            self.output_textbox.insert("1.0", translated)
            self.output_textbox.configure(state="disabled")

            self.status_label.configure(text="Translation complete ✔", text_color="#4ADE80")

        except Exception as error:
            # Something went wrong (no internet, invalid language, etc.)
            self.status_label.configure(text="Translation failed", text_color=ERROR_COLOR)
            messagebox.showerror(
                "Translation Error",
                f"Something went wrong while translating.\n\nDetails: {error}",
            )

    def copy_output(self):
        """Copies the translated text to the clipboard."""
        translated_text = self.output_textbox.get("1.0", "end").strip()

        if not translated_text:
            messagebox.showwarning("Nothing to Copy", "There is no translated text yet.")
            return

        self.clipboard_clear()
        self.clipboard_append(translated_text)
        self.status_label.configure(text="Copied to clipboard ✔", text_color="#4ADE80")

    def clear_text(self):
        """Clears both the input and output text boxes."""
        self.input_textbox.delete("1.0", "end")

        self.output_textbox.configure(state="normal")
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.configure(state="disabled")

        self.status_label.configure(text="")


# ---------------------------------------------------------------------------
# 6. PROGRAM ENTRY POINT
# ---------------------------------------------------------------------------
# This is where the program actually starts running.
# "if __name__ == '__main__':" is a standard Python pattern that means:
# "only run this code if this file is run directly (not imported)."
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()
