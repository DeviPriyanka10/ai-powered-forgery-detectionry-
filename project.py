import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageChops, ImageEnhance, ImageDraw, ImageFont, ImageTk
import numpy as np
import os
import datetime

def perform_ela_analysis(image_path, quality=90):
    original = Image.open(image_path).convert('RGB')
    temp_path = "temp_compressed.jpg"
    original.save(temp_path, "JPEG", quality=quality)
    compressed = Image.open(temp_path)
    diff = ImageChops.difference(original, compressed)
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    scale = 255.0 / max_diff if max_diff != 0 else 1
    ela_image = ImageEnhance.Brightness(diff).enhance(scale)
    return ela_image, np.mean(np.array(diff))

def create_side_by_side(original_path, ela_image, verdict, score):
    original = Image.open(original_path).convert('RGB')
    ela_resized = ela_image.resize(original.size)
    combined = Image.new('RGB', (original.width * 2, original.height))
    combined.paste(original, (0, 0))
    combined.paste(ela_resized, (original.width, 0))
    draw = ImageDraw.Draw(combined)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    text = f"Result: {verdict} (ELA diff = {score:.2f})"
    draw.text((10, 10), text, fill="red" if verdict == 'FORGED' else "green", font=font)
    return combined

def detect_forgery():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg *.jpeg")])
    if not file_path:
        return
    ela_img, diff_score = perform_ela_analysis(file_path)
    verdict = "FORGED" if diff_score > 12 else "ORIGINAL"
    final_img = create_side_by_side(file_path, ela_img, verdict, diff_score)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    result_path = f"ela_result_{timestamp}.jpg"
    final_img.save(result_path)
    messagebox.showinfo("Analysis Complete", f"{verdict} (ELA diff = {diff_score:.2f})\nSaved as {result_path}")
    os.startfile(result_path)

app = tk.Tk()
app.title("Image Forgery Detection - ELA")
app.geometry("400x200")
app.resizable(False, False)
label = tk.Label(app, text="Click below to choose a JPEG image", font=("Segoe UI", 12))
label.pack(pady=20)
btn = tk.Button(app, text="Browse Image", command=detect_forgery, font=("Segoe UI", 11), bg="#4CAF50", fg="white", padx=10, pady=5)
btn.pack()
app.mainloop()