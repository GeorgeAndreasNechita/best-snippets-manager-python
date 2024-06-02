import tkinter as tk
import time
import keyboard
import win32gui

# Sample array of items
items = [
    "test.py best-snippets-manager-python",
    "readTxts.py best-snippets-manager-python",
    "starter.py Coding help project * python",
    "class.py Coding help project * python",
    "import os Untitled-1",
    "snippet1 copy.txt best-snippets-manager-python * snippets",
    "settings.json C:\\Users\\Andreas\\AppData\\Roaming\\Code\\User",
    "altOHotkey.py best-snippets-manager-python",
    "snippets.json Coding help project"
]

# Create the main window
window = tk.Tk()
window.title("Item Selector")

# Create a listbox to display the items
listbox = tk.Listbox(window, height=len(items))
listbox.pack()

# Insert the items into the listbox
for item in items:
    listbox.insert(tk.END, item)

# Set the initial selection to the first item
listbox.selection_set(0)

# Function to handle arrow key events
def handle_arrow_keys(event):
    current_selection = listbox.curselection()
    if event.keysym == "Up":
        if current_selection[0] > 0:
            listbox.selection_clear(current_selection)
            listbox.selection_set(current_selection[0] - 1)
    elif event.keysym == "Down":
        if current_selection[0] < len(items) - 1:
            listbox.selection_clear(current_selection)
            listbox.selection_set(current_selection[0] + 1)

# Function to handle Enter key event
def handle_enter_key(event):
    selected_item = listbox.get(listbox.curselection())
    # Get the handle of the Tkinter window
    tkinter_window_handle = window.winfo_id()

    # Get the handle of the currently active window
    active_window_handle = win32gui.GetForegroundWindow()

    # Minimize the Tkinter window
    window.iconify()

    # Set focus to the previously active window
    win32gui.SetForegroundWindow(active_window_handle)

    # Send Ctrl+V command
    keyboard.press_and_release('ctrl+v')
    time.sleep(2)

# Bind arrow keys and Enter key to the listbox
listbox.bind("<Up>", handle_arrow_keys)
listbox.bind("<Down>", handle_arrow_keys)
listbox.bind("<Return>", handle_enter_key)

# Set focus to the listbox
listbox.focus_set()

# Start the Tkinter event loop
window.mainloop()