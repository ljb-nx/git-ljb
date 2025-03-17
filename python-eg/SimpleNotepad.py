import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext,simpledialog

class SimpleNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("未命名 - 简易记事本")
        self.current_file = None
        self.setup_ui()
        
    def setup_ui(self):
        # 创建菜单栏
        menubar = tk.Menu(self.root)
        
        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="新建", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="打开", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="保存", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="另存为", accelerator="Ctrl+Shift+S", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.exit_app)
        menubar.add_cascade(label="文件", menu=file_menu)
        
        # 编辑菜单
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="撤销", accelerator="Ctrl+Z", command=self.undo)
        edit_menu.add_command(label="重做", accelerator="Ctrl+Y", command=self.redo)
        edit_menu.add_command(label="查找", accelerator="Ctrl+F",command=self.find_text)
        edit_menu.add_command(label="替换", accelerator="Ctrl+H",command=self.replace_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="剪切", accelerator="Ctrl+X", command=self.cut)
        edit_menu.add_command(label="复制", accelerator="Ctrl+C", command=self.copy)
        edit_menu.add_command(label="粘贴", accelerator="Ctrl+V", command=self.paste)
        menubar.add_cascade(label="编辑", menu=edit_menu)
        
        self.root.config(menu=menubar)
        
        # 文本编辑区域
        self.text_area = scrolledtext.ScrolledText(
            self.root, 
            wrap=tk.WORD, 
            undo=True,
            font=("微软雅黑", 12)
        )
        self.text_area.pack(expand=True, fill='both')
        
        # 绑定快捷键
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda e: self.save_as())
        self.root.bind("<Control-z>", lambda e: self.undo())
        self.root.bind("<Control-y>", lambda e: self.redo())
        self.root.bind("<Control-f>", lambda e: self.find_text())
        self.root.bind("<Control-h>", lambda e: self.replace_text())

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("未命名 - 简易记事本")
        
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("文本文档", "*.txt"), ("所有文件", "*.*")]
        )
        if not file_path:
            return
            
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.current_file = file_path
            self.root.title(f"{file_path} - 简易记事本")
        except Exception as e:
            messagebox.showerror("错误", f"无法打开文件:\n{str(e)}")
            
    def save_file(self):
        if self.current_file:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("保存成功", "文件已保存")
            except Exception as e:
                messagebox.showerror("错误", f"保存失败:\n{str(e)}")
        else:
            self.save_as()
            
    def save_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("文本文档", "*.txt"), ("所有文件", "*.*")]
        )
        if not file_path:
            return
            
        try:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            self.current_file = file_path
            self.root.title(f"{file_path} - 简易记事本")
            messagebox.showinfo("保存成功", "文件已保存")
        except Exception as e:
            messagebox.showerror("错误", f"保存失败:\n{str(e)}")
            
    def exit_app(self):
        self.root.destroy()
    
    def find_text(self):
        # 弹出查找对话框
        search_string = simpledialog.askstring("查找", "请输入要查找的文本：")
        if search_string:
            start_pos = "1.0"
            while True:
                start_pos = self.text_area.search(search_string, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(search_string)}c"
                self.text_area.tag_add("found", start_pos, end_pos)
                start_pos = end_pos
                self.text_area.tag_config("found", background="yellow")

    def replace_text(self):
        # 弹出替换对话框
        search_string = simpledialog.askstring("替换", "请输入要查找的文本：")
        replace_string = simpledialog.askstring("替换", "请输入要替换成的文本：")
        if search_string and replace_string:
            start_pos = "1.0"
            while True:
                start_pos = self.text_area.search(search_string, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(search_string)}c"
                self.text_area.replace(start_pos, end_pos, replace_string)
                start_pos = end_pos
        
    # 编辑功能
    def undo(self):
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass
            
    def redo(self):
        try:
            self.text_area.edit_redo()
        except tk.TclError:
            pass
            
    def cut(self):
        self.text_area.event_generate("<<Cut>>")
        
    def copy(self):
        self.text_area.event_generate("<<Copy>>")
        
    def paste(self):
        self.text_area.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = SimpleNotepad(root)
    root.mainloop()