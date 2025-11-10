import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os

def encrypt_image(path, key):
    img = Image.open(path)
    arr = np.array(img, dtype=np.uint8)
    enc = (arr + key) % 256
    enc_img = Image.fromarray(enc.astype(np.uint8))
    out = os.path.splitext(path)[0] + "_encrypted.png"
    enc_img.save(out)
    return out

def decrypt_image(path, key):
    img = Image.open(path)
    arr = np.array(img, dtype=np.uint8)
    dec = (arr - key) % 256
    dec_img = Image.fromarray(dec.astype(np.uint8))
    out = os.path.splitext(path)[0] + "_decrypted.png"
    dec_img.save(out)
    return out

def choose_file():
    global img_path
    img_path = filedialog.askopenfilename(
        initialdir=".",
        filetypes=[("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("All","*.*")]
    )
    file_label.config(text=img_path if img_path else "No file selected")
    if img_path:
        show_original(img_path)

def show_original(path):
    img = Image.open(path)
    img = img.resize((250, 250))
    img_tk = ImageTk.PhotoImage(img)
    preview_original.config(image=img_tk)
    preview_original.image = img_tk

def show_result(path):
    img = Image.open(path)
    img = img.resize((250, 250))
    img_tk = ImageTk.PhotoImage(img)
    preview_result.config(image=img_tk)
    preview_result.image = img_tk

def save_as():
    global last_output_path
    if not last_output_path:
        messagebox.showwarning("Warning","No result to save yet!")
        return
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG","*.png"),("All","*.*")]
    )
    if save_path:
        Image.open(last_output_path).save(save_path)
        messagebox.showinfo("Saved","Saved as:\n"+save_path)

def run(mode):
    global last_output_path
    if not img_path:
        messagebox.showwarning("Warning", "Choose an image first!")
        return
    try:
        key = int(key_entry.get())
    except:
        messagebox.showerror("Error", "Key must be a number")
        return
    
    if mode=="enc":
        last_output_path = encrypt_image(img_path, key)
    else:
        last_output_path = decrypt_image(img_path, key)

    show_result(last_output_path)
    messagebox.showinfo("DONE", "Saved result:\n"+last_output_path)

#gui
root = tk.Tk()
root.title("Image Encryption - SkillCraft Task 02")

img_path = ""
last_output_path = ""

tk.Button(root, text="Select Image", command=choose_file).grid(row=0, column=0, pady=10)
file_label = tk.Label(root, text="No file selected", width=40)
file_label.grid(row=0, column=1)

tk.Label(root, text="Key Value").grid(row=1, column=0)
key_entry = tk.Entry(root)
key_entry.grid(row=1, column=1)

tk.Button(root, text="Encrypt", width=15, command=lambda: run("enc")).grid(row=2, column=0, pady=10)
tk.Button(root, text="Decrypt", width=15, command=lambda: run("dec")).grid(row=2, column=1, pady=10)


tk.Label(root, text="Original Image").grid(row=4, column=0)
tk.Label(root, text="Result Image").grid(row=4, column=1)

preview_original = tk.Label(root)
preview_original.grid(row=5, column=0, padx=10, pady=10)

preview_result = tk.Label(root)
preview_result.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()

 
