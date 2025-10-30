# lib/menu.py
from tkinter import messagebox

def on_new():
    messagebox.showinfo("New File", "Create a new file (not implemented)")

def on_open():
    messagebox.showinfo("Open File", "Open a file (not implemented)")

def on_exit(root):
    root.quit()

def on_cut():
    messagebox.showinfo("Cut", "Cut text (not implemented)")

def on_copy():
    messagebox.showinfo("Copy", "Copy text (not implemented)")

def on_paste():
    messagebox.showinfo("Paste", "Paste text (not implemented)")

def on_about():
    messagebox.showinfo("About", "Sample Tkinter GUI\n(c) 2025 Your Friendly Red Team, ltd.")

def build_menu(root):
    """Return a tkinter.Menu instance attached to root."""
    from tkinter import Menu
    menubar = Menu(root)

    # File menu
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="New", command=on_new)
    file_menu.add_command(label="Open...", command=on_open)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=lambda: on_exit(root))
    menubar.add_cascade(label="File", menu=file_menu)

    # Edit menu
    edit_menu = Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Cut", command=on_cut)
    edit_menu.add_command(label="Copy", command=on_copy)
    edit_menu.add_command(label="Paste", command=on_paste)
    menubar.add_cascade(label="Edit", menu=edit_menu)

    plugin_menu = Menu(menubar, tearoff=0)
    plugin_menu.add_command(label="reload plugins", command=lambda: messagebox.showinfo("Plugins", "Reload plugins (not implemented)"))
    menubar.add_cascade(label="Plugins", menu=plugin_menu)

    # Help / About menu
    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=on_about)
    menubar.add_cascade(label="Help", menu=help_menu)

    return menubar
