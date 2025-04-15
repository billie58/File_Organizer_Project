import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ttkbootstrap import Style
import os
import shutil
import hashlib
import datetime
import json
from PIL import Image, ImageTk

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.style = Style(theme="minty")
        self.root.title("File Organizer")
        self.current_dir = ""
        self.operation_stack = []
        
        self.history_dir = "file_organization_history"
        os.makedirs(self.history_dir, exist_ok=True)
        
        self.create_widgets()
        self.setup_bindings()
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        toolbar = ttk.Frame(main_frame)
        toolbar.pack(fill=tk.X, pady=5)
        
        button_config = {
            "Open Folder": self.open_folder,
            "Organize Files": self.organize_files,
            "Find Duplicates": self.find_duplicates,
            "Undo All Moves": self.undo_all_moves,
            "View History": self.show_history
        }
        
        for text, command in button_config.items():
            ttk.Button(toolbar, text=text, command=command).pack(side=tk.LEFT, padx=2)
        
        self.paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(self.paned_window, columns=("size", "type"), selectmode="browse")
        self.configure_treeview_columns()
        self.paned_window.add(self.tree)
        
        right_panel = self.create_function_panel()
        self.paned_window.add(right_panel)
        
    def configure_treeview_columns(self):
        columns = {
            "#0": ("Name", 300),
            "size": ("Size", 100),
            "type": ("Type", 100)
        }
        for col, (text, width) in columns.items():
            self.tree.heading(col, text=text)
            self.tree.column(col, width=width)
        
    def create_function_panel(self):
        panel = ttk.Frame(self.paned_window)
        self.notebook = ttk.Notebook(panel) 
        
        tabs = {
            "Preview": self.create_preview_tab,
            "History": self.create_history_tab
        }
        
        for text, creator in tabs.items():
            frame = ttk.Frame(self.notebook)
            creator(frame)
            self.notebook.add(frame, text=text)
        
        self.notebook.pack(expand=True, fill=tk.BOTH)
        return panel
                
    def create_preview_tab(self, parent):
        preview_frame = ttk.Frame(parent)
        preview_frame.pack(fill=tk.BOTH, expand=True)
        
        self.preview_label = ttk.Label(preview_frame, text="Preview Area")
        self.preview_label.pack(pady=20)
        
        self.image_label = ttk.Label(preview_frame)
        self.image_label.pack()
        
    def create_history_tab(self, parent):
        history_frame = ttk.Frame(parent)
        self.history_tree = ttk.Treeview(history_frame, columns=("operation", "source", "destination"))
        
        columns = {
            "#0": ("Timestamp", 150),
            "operation": ("Operation", 80),
            "source": ("Source", 300),
            "destination": ("Destination", 300)
        }
        
        for col, (text, width) in columns.items():
            self.history_tree.heading(col, text=text)
            self.history_tree.column(col, width=width)
        
        self.history_tree.pack(fill=tk.BOTH, expand=True)
        ttk.Button(history_frame, text="Refresh", command=self.load_history).pack(pady=5)
        history_frame.pack(fill=tk.BOTH, expand=True)
        
    def setup_bindings(self):
        self.tree.bind("<<TreeviewSelect>>", self.show_preview)
    
    def open_folder(self):
        path = filedialog.askdirectory()
        if not path:
            return
            
        self.current_dir = path
        self.tree.delete(*self.tree.get_children())
        self.load_directory_tree(path)
        
    def load_directory_tree(self, path):
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                is_dir = os.path.isdir(full_path)
                size = os.path.getsize(full_path) if not is_dir else 0
                ftype = "Folder" if is_dir else "File"
                
                self.tree.insert("", "end", text=item, 
                               values=(self.format_size(size), ftype))
        except Exception as e:
            messagebox.showerror("Error", f"Directory load failed: {str(e)}")
            
    def organize_files(self):
        if not self.current_dir:
            messagebox.showwarning("Warning", "Please select a folder first")
            return
            
        try:
            organized_files = []
            for filename in os.listdir(self.current_dir):
                src = os.path.join(self.current_dir, filename)
                if os.path.isfile(src):
                    ext = filename.split('.')[-1].lower()
                    dest_dir = os.path.join(self.current_dir, f"{ext}_files")
                    os.makedirs(dest_dir, exist_ok=True)
                    dest = os.path.join(dest_dir, filename)
                    shutil.move(src, dest)
                    
                    self.log_operation("MOVE", src, dest)
                    organized_files.append({
                        "type": "MOVE",
                        "from": dest,
                        "to": src,
                        "timestamp": datetime.datetime.now()
                    })
            
            if organized_files:
                self.operation_stack.extend(organized_files)
                messagebox.showinfo("Complete", f"Organized {len(organized_files)} files")
                self.load_directory_tree(self.current_dir)
        except Exception as e:
            messagebox.showerror("Error", f"Organization failed: {str(e)}")
            
    def undo_all_moves(self):
        move_operations = [op for op in self.operation_stack if op["type"] == "MOVE"]
        if not move_operations:
            messagebox.showinfo("Info", "No move operations to undo")
            return
            
        success_count = 0
        error_messages = []
        
        for op in reversed(move_operations):
            try:
                shutil.move(op["from"], op["to"])
                self.log_operation("UNDO MOVE", op["from"], op["to"])
                success_count += 1
            except Exception as e:
                error_messages.append(f"{op['from']} -> {op['to']}: {str(e)}")
        
        self.operation_stack = [op for op in self.operation_stack if op not in move_operations]
        
        self.load_directory_tree(self.current_dir)
        
        result = f"Successfully undone {success_count} moves"
        if error_messages:
            result += f"\n\nFailed operations:\n" + "\n".join(error_messages)
        messagebox.showinfo("Undo Complete", result)
        
    def find_duplicates(self):
        path = filedialog.askdirectory()
        if not path:
            return
            
        hashes = {}
        duplicates = []
        
        for root, _, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                try:
                    file_hash = self.calculate_md5(full_path)
                    if file_hash in hashes:
                        duplicates.append((full_path, hashes[file_hash]))
                    else:
                        hashes[file_hash] = full_path
                except Exception as e:
                    print(f"Error processing {full_path}: {str(e)}")
                
        self.display_duplicates(duplicates)
        
    def display_duplicates(self, duplicates):
        if duplicates:
            msg = "\n\n".join([f"• {f1}\n  Duplicate of: {f2}" for f1, f2 in duplicates])
            messagebox.showinfo("Duplicates Found", f"Found {len(duplicates)} duplicates:\n\n{msg}")
        else:
            messagebox.showinfo("Result", "No duplicate files found")
            
    def show_preview(self, event=None):
        selected = self.tree.selection()
        if not selected:
            return
            
        item = self.tree.item(selected[0])
        filename = item["text"]
        path = os.path.join(self.current_dir, filename)
        
        try:
            self.clear_preview()
            if path.lower().endswith(('.png', '.jpg', '.jpeg')):
                self.display_image_preview(path)
            elif path.lower().endswith(('.txt', '.md', '.csv', '.json')):
                self.display_text_preview(path)
            else:
                self.preview_label.config(text="Preview not available")
        except Exception as e:
            self.preview_label.config(text=f"Preview error: {str(e)}")
            
    def clear_preview(self):
        self.preview_label.config(text="")
        self.image_label.config(image="")
        
    def display_image_preview(self, path):
        img = Image.open(path)
        img.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
    def display_text_preview(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            preview = f.read(1000)
        self.preview_label.config(text=preview)
        
    def show_history(self):
        self.load_history()
        self.notebook.select(1)
        
    def load_history(self):
        self.history_tree.delete(*self.history_tree.get_children())
        history_files = sorted([f for f in os.listdir(self.history_dir) 
                              if f.startswith("history_")], reverse=True)
        
        for hfile in history_files:
            self.load_history_file(hfile)
            
    def load_history_file(self, filename):
        filepath = os.path.join(self.history_dir, filename)
        try:
            with open(filepath, "r", encoding='utf-8') as f:
                for line in f:
                    entry = json.loads(line)
                    timestamp = datetime.datetime.fromisoformat(
                        entry["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
                    self.history_tree.insert("", "end", text=timestamp,
                                           values=(entry["operation"],
                                                   entry["source"],
                                                   entry.get("destination", "")))
        except Exception as e:
            print(f"Error loading {filename}: {str(e)}")
            
    def log_operation(self, operation, src, dest=None):
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "operation": operation,
            "source": src,
            "destination": dest,
            "user": os.getlogin()
        }
        
        log_file = os.path.join(self.history_dir, 
                              f"history_{datetime.date.today()}.json")
        
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
            
    @staticmethod
    def format_size(size):
        if not size:
            return "0 B"
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"
            
    @staticmethod
    def calculate_md5(filepath):
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")
    app = FileManagerApp(root)
    root.mainloop()