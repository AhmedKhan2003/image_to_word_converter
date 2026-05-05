import tkinter as tk
from tkinter import filedialog, messagebox

from preprocess import preprocess_image
from ocr import extract_text
from formatter import detect_formatting
from doc_generator import generate_doc


def process_image():
    path = filedialog.askopenfilename(
        filetypes=[("Images", "*.png *.jpg")]
    )

    if not path:
        return

    image = preprocess_image(path)
    text_data = extract_text(image)
    words = detect_formatting(text_data)
    generate_doc(words)

    messagebox.showinfo(
        "Success",
        "Word file generated as output.docx"
    )


root = tk.Tk()
root.title("Image to Word Converter")
root.geometry("300x200")

btn = tk.Button(
    root,
    text="Upload Image",
    command=process_image
)
btn.pack(expand=True)

root.mainloop()
