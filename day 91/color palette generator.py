# ============================================================
#  DAY 91: Portfolio Project
#  PROJECT: Image to Colour Palette Generator
# ============================================================
#
#  SKILLS USED: PIL/Pillow, colorgram, Tkinter, k-means clustering
#
#  REQUIREMENTS:
#    - Open any image
#    - Extract the dominant colours (k-means or colorgram)
#    - Display a colour swatch palette
#    - Show hex codes for each colour
#    - Copy a hex code to clipboard on click
#
#  pip install pillow colorgram.py pyperclip
#
# ============================================================

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import colorgram
import pyperclip

class PaletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colour Palette Generator")
        self.root.config(padx=20, pady=20, bg="#1e1e2e")
        self.setup_ui()

    def setup_ui(self):
        tk.Button(self.root, text="Open Image", command=self.open_image,
                  bg="#89b4fa", fg="#1e1e2e", font=("Arial", 12, "bold")).pack(pady=10)

        self.img_label = tk.Label(self.root, bg="#1e1e2e")
        self.img_label.pack()

        self.palette_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.palette_frame.pack(pady=10)

        self.status = tk.Label(self.root, text="", bg="#1e1e2e", fg="#cdd6f4")
        self.status.pack()

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")])
        if not path:
            return

        # Show thumbnail
        img = Image.open(path)
        img.thumbnail((400, 300))
        self.tk_img = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.tk_img)

        # --------------------------------------------------
        #  TODO 1: Extract 10 dominant colours using colorgram
        # --------------------------------------------------
        # colours = colorgram.extract(path, 10)
        # Each colour has .rgb (r,g,b tuple) and .proportion

        colours = colorgram.extract(path, 10)
        self.show_palette(colours)

    def show_palette(self, colours):
        # Clear old swatches
        for widget in self.palette_frame.winfo_children():
            widget.destroy()

        # --------------------------------------------------
        #  TODO 2: Create a colour swatch for each colour
        # --------------------------------------------------
        # For each colour:
        #   hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
        #   Create a Frame with background = hex_code
        #   Create a Label inside showing the hex code
        #   Bind a click to copy the hex to clipboard

        for colour in colours:
            r, g, b = colour.rgb
            hex_code = f"#{r:02x}{g:02x}{b:02x}"

            swatch = tk.Frame(self.palette_frame, bg=hex_code, width=80, height=80, cursor="hand2")
            swatch.pack(side=tk.LEFT, padx=4)
            swatch.pack_propagate(False)

            # Choose readable text colour (white on dark, black on light)
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            text_color = "white" if brightness < 128 else "black"

            label = tk.Label(swatch, text=hex_code, bg=hex_code, fg=text_color, font=("Courier", 8))
            label.place(relx=0.5, rely=0.5, anchor="center")

            # TODO: bind click to copy hex_code to clipboard
            # swatch.bind("<Button-1>", lambda e, h=hex_code: pyperclip.copy(h))
            # label.bind("<Button-1>", lambda e, h=hex_code: ...)

        self.status.config(text=f"Extracted {len(colours)} colours. Click a swatch to copy hex.")


root = tk.Tk()
app  = PaletteApp(root)
root.mainloop()
