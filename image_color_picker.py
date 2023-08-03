import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def get_hex_code(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

def show_hex_code(event):
    x, y = event.x, event.y
    rgb = img.getpixel((x, y))
    hex_code = get_hex_code(rgb)
    label.config(text=f"Hex Code: {hex_code}")

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        global img
        img = Image.open(file_path)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        canvas.config(scrollregion=canvas.bbox(tk.ALL), width=img.width, height=img.height)

# Create the main window
root = tk.Tk()
root.title("Color Picker")

# Create a canvas to display the image
canvas = tk.Canvas(root)
canvas.pack()

# Create a label to display the hex code
label = tk.Label(root, text="Hover over the image to get the Hex Code.")
label.pack()

# Open button to load an image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Bind the mouse motion event to show the hex code
canvas.bind("<Motion>", show_hex_code)

# Start the main event loop
root.mainloop()
