import tkinter as tk
from tkinter import *
import tkinter.filedialog

class TextEditor:
    def __init__(self, root):

        self.root = root
        self.create_menu()
        self.create_text_area()

    def create_menu(self):
        self.root.title('Text Editor')
        self.root.geometry("800x500")
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

    def create_text_area(self):
        self.text = tk.Text(self.root)
        self.text.pack(fill='both', expand=True)

    def open_file(self):
        # Prompt the user to select a file to open
        filepath = tkinter.filedialog.askopenfilename()

        # Read the contents of the file into the text editor
        with open(filepath, "r") as file:
            self.text_edit.delete("1.0", "end")
            self.text_edit.insert("1.0", file.read())

    def save_file(self):
        # Prompt the user to select a file to save
        filepath = tkinter.filedialog.asksaveasfilename()

        # Write the contents of the text editor to the selected file
        with open(filepath, "w") as file:
            file.write(self.text_edit.get("1.0", "end-1c"))


    def cut(self):
        # Get the selected text
        selected_text = self.text_edit.selection_get()

        # Clear the clipboard
        self.clipboard_clear()

        # Add the selected text to the clipboard
        self.clipboard_append(selected_text)

        # Delete the selected text from the text editor widget
        self.text_edit.delete("sel.first", "sel.last")
 
       
root = tk.Tk()
app = TextEditor(root)
root.mainloop()
