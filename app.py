import tkinter as tk
from tkinter import filedialog


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

if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()