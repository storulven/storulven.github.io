#!/usr/bin/env python3
import sys
import os
import tkinter as tk
from tkinter import ttk
from lib import menu
from glob import glob

sys.path += ['plugins']
PLUGINS = []

def load_plugins():
    global PLUGINS
    for plugin_path in sorted(glob(os.path.join('plugins', '*.py'))):
        plugin_name = os.path.splitext(os.path.basename(plugin_path))[0]
        module = __import__(plugin_name)
        PLUGINS.append(module)
        if "ONLOAD" in dir(module):
            module.ONLOAD()
    return

def populate_plugins_menu(menu):
    menu.delete(0, tk.END)
    for plugin in PLUGINS:
        menu.insert(tk.END, plugin.MENU_NAME)
    return

def on_item_selected(event, listbox, top_entry, bottom_entry):
    """Kalles når et element i listeboksen er valgt."""
    selection = listbox.curselection()  # tuple of selected indices
    if not selection: return  

    index = selection[0]
    plugin = PLUGINS[index]
    print(plugin) # debug til konsollen

    input_text = top_entry.get("1.0", tk.END).strip()
    bottom_entry.config(state="normal")
    bottom_entry.delete("1.0", tk.END)
    bottom_entry.insert(tk.END, plugin.process(input_text))
    bottom_entry.config(state="disabled")
    return

def main():
    load_plugins()
    root = tk.Tk()
    root.title("LocalChef")

    root.geometry("800x600")
    menubar = menu.build_menu(root) # fra lib/menu.py
    root.config(menu=menubar)

    # Use a horizontal PanedWindow to split left/right
    main_pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
    main_pane.pack(fill=tk.BOTH, expand=True)

    # --- Left side: Listbox ---
    left_frame = ttk.Frame(main_pane, padding=5)
    listbox = tk.Listbox(left_frame)
    listbox.pack(fill=tk.BOTH, expand=True)
    
    # Add example items
    #for i in range(1, 21):
    #    listbox.insert(tk.END, f"Item {i}")
    populate_plugins_menu(listbox)

    main_pane.add(left_frame, weight=1)

    # --- Right side: Two stacked input boxes ---
    right_frame = ttk.Frame(main_pane, padding=5)
    main_pane.add(right_frame, weight=2)

    # Top input
    top_entry = tk.Text(right_frame, height=6, wrap=tk.WORD)
    top_entry.pack(fill=tk.BOTH, expand=True, pady=(0,5))

    # Bottom input
    bottom_entry = tk.Text(right_frame, height=6, wrap=tk.WORD)
    bottom_entry.pack(fill=tk.BOTH, expand=True)
    bottom_entry.config(state="disabled")  # Read-only
    listbox.bind("<<ListboxSelect>>", lambda e: on_item_selected(e, listbox, top_entry, bottom_entry))

    # Optional: make resizing smooth
    root.update_idletasks()

    root.mainloop()

if __name__ == "__main__":
    main()
