Image Encryption Tool (Pixel Manipulation – Python GUI)

This project is a simple image-based encryption & decryption tool created using Python, Tkinter GUI, Pillow, and NumPy.

The program encrypts and decrypts an image by applying a mathematical operation to each pixel value.
You can also click Save Result As… to store the final output image.

Features

1.Select image from file explorer	
2.Show original image preview	
3.Encrypt image using a key	
4.Decrypt image using a key	
5.Show encrypted/decrypted result preview
6.Save result to a custom file name	

How It Works

Pixel values are loaded from the selected image.

To Encrypt → each pixel value gets + key (mod 256)

To Decrypt → each pixel value gets - key (mod 256)

Result is displayed immediately in the GUI.

Example:
If a pixel value = 100 and key = 40
→ encrypted pixel = (100 + 40) mod 256 = 140

This is a basic classical image manipulation cipher and is only for learning purposes.

Requirements / Dependencies
Library	Usage
tkinter	GUI window
pillow (PIL + ImageTk)	image loading + preview display
numpy	pixel array manipulation

Install dependencies (Ubuntu):
sudo apt install python3-numpy python3-pil python3-pil.imagetk

To Run the Program:
python3 img_encryption.py

How to Use

Run the script

1.Click Select Image → choose .png/.jpg/.jpeg
2.Enter a numeric key (example: 42)
3.Click Encrypt or Decrypt
4.The result image appears in the right preview panel

Credits:

Project done as part of SkillCraft Technology – Cybersecurity Training / Internship
 – Image Encryption via Pixel Manipulation
