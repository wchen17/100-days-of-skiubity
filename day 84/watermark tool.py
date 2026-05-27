# ============================================================
#  DAY 84: Portfolio Project
#  PROJECT: Image Watermarking Desktop App
# ============================================================
#
#  SKILLS USED: Tkinter, PIL/Pillow, file dialogs, OOP
#
#  REQUIREMENTS:
#    - Open any image via file dialog
#    - Let user type custom watermark text
#    - Choose font size and opacity
#    - Preview the watermarked image
#    - Save the result to a new file
#
#  pip install pillow
#
# ============================================================

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

class WatermarkApp:
    def __init__(self, root):
        self.root  = root
        self.root.title("Image Watermarker")
        self.image = None
        self.tk_image = None
        self.setup_ui()

    def setup_ui(self):
        # Control panel
        controls = tk.Frame(self.root)
        controls.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Button(controls, text="Open Image", command=self.open_image).pack(fill=tk.X, pady=4)

        tk.Label(controls, text="Watermark Text:").pack()
        self.text_var = tk.StringVar(value="© wchen17")
        tk.Entry(controls, textvariable=self.text_var, width=20).pack()

        tk.Label(controls, text="Font Size:").pack()
        self.size_var = tk.IntVar(value=36)
        tk.Scale(controls, from_=12, to=120, variable=self.size_var, orient=tk.HORIZONTAL).pack(fill=tk.X)

        tk.Label(controls, text="Opacity (0-255):").pack()
        self.opacity_var = tk.IntVar(value=128)
        tk.Scale(controls, from_=0, to=255, variable=self.opacity_var, orient=tk.HORIZONTAL).pack(fill=tk.X)

        tk.Button(controls, text="Preview",   command=self.preview,   bg="blue",  fg="white").pack(fill=tk.X, pady=4)
        tk.Button(controls, text="Save",      command=self.save,       bg="green", fg="white").pack(fill=tk.X)

        # Image canvas
        self.canvas = tk.Canvas(self.root, width=600, height=500, bg="#1e1e2e")
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if path:
            self.image = Image.open(path).convert("RGBA")
            self.display_image(self.image)

    def display_image(self, img):
        display = img.copy()
        display.thumbnail((600, 500))
        self.tk_image = ImageTk.PhotoImage(display)
        self.canvas.delete("all")
        self.canvas.create_image(300, 250, image=self.tk_image)

    # --------------------------------------------------
    #  TODO 1: apply_watermark(image) → Image
    # --------------------------------------------------
    # Create a transparent overlay: Image.new("RGBA", image.size, (0,0,0,0))
    # Use ImageDraw to write the text at the bottom-right corner
    # Use opacity_var for the text fill alpha: (255, 255, 255, opacity)
    # Composite: Image.alpha_composite(image, overlay)
    # Return the composited image

    def apply_watermark(self, image):
        pass   # TODO

    def preview(self):
        if self.image is None:
            messagebox.showwarning("No Image", "Please open an image first.")
            return
        result = self.apply_watermark(self.image.copy())
        self.display_image(result)

    # --------------------------------------------------
    #  TODO 2: save()
    # --------------------------------------------------
    # Open a save dialog (asksaveasfilename)
    # Apply watermark to the original (full-size) image
    # Convert to RGB before saving as JPEG (JPEG doesn't support alpha)
    # Save the file

    def save(self):
        pass   # TODO


root = tk.Tk()
app  = WatermarkApp(root)
root.mainloop()
