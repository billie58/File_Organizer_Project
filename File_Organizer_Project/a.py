import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleFileOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple File Organizer")
        self.root.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        # Directory Selection
        tk.Label(self.root, text="Select Folder:").pack(pady=10)
        
        self.dir_entry = tk.Entry(self.root, width=40)
        self.dir_entry.pack(pady=5)
        
        tk.Button(self.root, text="Browse", command=self.browse_directory).pack(pady=5)

        # Fixed method name (no underscore)
        tk.Button(self.root, text="Start Organizing", 
                command=self.organizefiles).pack(pady=10)  # Changed to organizefiles

        # Status Hint
        self.status = tk.Label(self.root, text="", fg="blue")
        self.status.pack()

    def browse_directory(self):
        folder = filedialog.askdirectory()
        self.dir_entry.delete(0, tk.END)
        self.dir_entry.insert(0, folder)
        self.status.config(text="Folder selected: " + folder)

    # Correct method name (no underscore)
    def organizefiles(self):  # Same name as used in the button command
        target_dir = self.dir_entry.get()
        if not target_dir:
            messagebox.showerror("Error", "Please select a folder first!")
            return

        try:
            categories = {
                "Documents": [".pdf", ".doc", ".docx", ".txt"],
                "Images": [".jpg", ".png", ".gif"],
                "Videos": [".mp4", ".mov"],
                "Others": []
            }

            for filename in os.listdir(target_dir):
                file_path = os.path.join(target_dir, filename)
                if os.path.isfile(file_path):
                    ext = os.path.splitext(filename)[1].lower()
                    
                    for category, exts in categories.items():
                        if ext in exts:
                            dest = os.path.join(target_dir, category)
                            os.makedirs(dest, exist_ok=True)
                            shutil.move(file_path, os.path.join(dest, filename))
                            break
                    else:
                        dest = os.path.join(target_dir, "Others")
                        os.makedirs(dest, exist_ok=True)
                        shutil.move(file_path, os.path.join(dest, filename))

            self.status.config(text="Organization completed!", fg="green")
            messagebox.showinfo("Done", "Files organized successfully!")

        except Exception as e:
            self.status.config(text=f"Error: {str(e)}", fg="red")
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleFileOrganizer(root)
    root.mainloop()