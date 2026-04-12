import tkinter as tk
import os
from tkinter import filedialog
from tkinter import filedialog, messagebox
import shutil
from PIL import Image


class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal File Converter")
        self.root.geometry("500x300")
        self.file_path = ""
        tk.Label(root, text="Select File:", font=("Arial", 12)).pack(pady=10)
        self.path_entry = tk.Entry(root, width=50)
        self.path_entry.pack(pady=5)
        tk.Button(root, text="Browse", command=self.browse_file).pack(pady=5)
        tk.Label(root, text="Convert To (extension):", font=("Arial", 12)).pack(pady=10)
        self.format_entry = tk.Entry(root)
        self.format_entry.pack(pady=5)
        tk.Button(root, text="Convert", command=self.convert_file, bg="green", fg="white").pack(pady=20)
        
    def browse_file(self):
      file = filedialog.askopenfilename()
      if file:
          self.file_path = file
          self.path_entry.delete(0, tk.END)
          self.path_entry.insert(0, file)
          
    def convert_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file first")
            return

        target_ext = self.format_entry.get().lower().strip()
        if not target_ext:
            messagebox.showerror("Error", "Enter target format (e.g., png, jpg, txt)")
            return
        
        base, ext = os.path.splitext(self.file_path)
        new_file = base + "." + target_ext
        
        # IMAGE CONVERSION
        if ext.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
            img = Image.open(self.file_path)
            img.save(new_file)
        # SIMPLE FILE COPY (for text-like formats)
        else:
            shutil.copy(self.file_path, new_file)
        messagebox.showinfo("Success", f"File converted to {new_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()