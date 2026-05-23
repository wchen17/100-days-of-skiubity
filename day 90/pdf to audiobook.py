# ============================================================
#  DAY 90 — Portfolio Project
#  PROJECT: PDF to Audiobook Converter
# ============================================================
#
#  SKILLS USED: PyPDF2/pypdf, pyttsx3 or gtts, file dialogs, Tkinter
#
#  REQUIREMENTS:
#    - Select a PDF file via file dialog
#    - Extract text from each page
#    - Convert text to speech (offline with pyttsx3 or online with gTTS)
#    - Play audio directly or save as .mp3
#    - Show page progress
#
#  pip install pypdf pyttsx3 gtts
#
# ============================================================

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os

# Try pyttsx3 (offline TTS) — falls back gracefully if not installed
try:
    import pyttsx3
    TTS_ENGINE = "pyttsx3"
except ImportError:
    TTS_ENGINE = None

# Try gTTS (online TTS, saves to mp3)
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

# PDF reader
try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        PdfReader = None


class AudiobookApp:
    def __init__(self, root):
        self.root      = root
        self.root.title("PDF to Audiobook")
        self.root.config(padx=20, pady=20)
        self.pdf_path  = None
        self.is_playing = False
        self.setup_ui()

    def setup_ui(self):
        tk.Button(self.root, text="Open PDF", command=self.open_pdf,
                  bg="#4a90d9", fg="white", font=("Arial", 12)).pack(pady=5)

        self.file_label = tk.Label(self.root, text="No file selected", wraplength=400)
        self.file_label.pack()

        self.page_label = tk.Label(self.root, text="Page: -/-")
        self.page_label.pack()

        tk.Button(self.root, text="▶ Read Aloud (pyttsx3)",
                  command=self.read_aloud, bg="#45ba78", fg="white").pack(pady=5)
        tk.Button(self.root, text="💾 Save as MP3 (gTTS)",
                  command=self.save_mp3, bg="#f59e0b", fg="white").pack(pady=5)
        tk.Button(self.root, text="⏹ Stop",
                  command=self.stop, bg="#ef4444", fg="white").pack(pady=5)

        self.status = tk.Label(self.root, text="", font=("Arial", 11), fg="gray")
        self.status.pack()

    def open_pdf(self):
        path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if path:
            self.pdf_path = path
            self.file_label.config(text=os.path.basename(path))
            self.status.config(text="PDF loaded. Ready to read.")

    # --------------------------------------------------
    #  TODO 1: extract_text(pdf_path) → list of page strings
    # --------------------------------------------------
    def extract_text(self, path):
        if PdfReader is None:
            messagebox.showerror("Error", "pypdf not installed. pip install pypdf")
            return []
        reader = PdfReader(path)
        pages  = [page.extract_text() or "" for page in reader.pages]
        return pages

    # --------------------------------------------------
    #  TODO 2: read_aloud() — run in a thread so UI stays responsive
    # --------------------------------------------------
    # Extract pages, loop through each:
    #   Update page_label
    #   engine = pyttsx3.init()
    #   engine.say(page_text)
    #   engine.runAndWait()
    #   If not self.is_playing: break

    def read_aloud(self):
        if not self.pdf_path:
            messagebox.showwarning("No PDF", "Open a PDF first.")
            return
        self.is_playing = True
        thread = threading.Thread(target=self._read_thread, daemon=True)
        thread.start()

    def _read_thread(self):
        pages = self.extract_text(self.pdf_path)
        if TTS_ENGINE == "pyttsx3":
            engine = pyttsx3.init()
            for i, page in enumerate(pages, 1):
                if not self.is_playing:
                    break
                self.page_label.config(text=f"Page: {i}/{len(pages)}")
                engine.say(page)
                engine.runAndWait()
        else:
            self.status.config(text="pyttsx3 not available. Use Save as MP3 instead.")

    # --------------------------------------------------
    #  TODO 3: save_mp3() — use gTTS to save each page as mp3
    # --------------------------------------------------
    def save_mp3(self):
        pass   # TODO

    def stop(self):
        self.is_playing = False
        self.status.config(text="Stopped.")


root = tk.Tk()
app  = AudiobookApp(root)
root.mainloop()
