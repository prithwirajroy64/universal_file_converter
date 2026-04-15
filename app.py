import tkinter as tk

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal File Converter")
        self.root.geometry("500x300")
        # empty file path
        self.file_path = ""
        tk.Label(root, text = "Select File:", font=("Arial", 12)).pack(pady=10)
        self.path_entry = tk.Entry(root, width=50)
        self.path_entry.pack(pady=5)
        # file select button 
        tk.Button(root, text="Browse").pack(pady=5)
        tk.Label(root, text="Convert To (extension):", font=("Arial", 12)).pack(pady=10)
        self.format_entry = tk.Entry(root)
        self.format_entry.pack(pady=5)
        tk.Button(root, text="Convert", bg="green", fg="white").pack(pady=20)
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()