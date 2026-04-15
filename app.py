import tkinter as tk

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal File Converter")
        self.root.geometry("500x300")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()