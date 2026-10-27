import tkinter as tk
from tkinter import messagebox

def generate_listbox_with_input():
    root = tk.Tk()
    root.title("Interactive Listbox Generator")
    root.geometry("400x350")
    
    # Frame for input controls
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)
    
    tk.Label(input_frame, text="Add Item:").pack(side=tk.LEFT)
    entry = tk.Entry(input_frame, width=20)
    entry.pack(side=tk.LEFT, padx=5)
    
    # Create listbox with scrollbar
    listbox_frame = tk.Frame(root)
    listbox_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    scrollbar = tk.Scrollbar(listbox_frame)
    listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Functions to add and remove items
    def add_item():
        item = entry.get().strip()
        if item:
            listbox.insert(tk.END, item)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an item!")
    
    def remove_item():
        try:
            selected_index = listbox.curselection()[0]
            listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to remove!")
    
    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)
    
    tk.Button(button_frame, text="Add", command=add_item).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Remove", command=remove_item).pack(side=tk.LEFT, padx=5)
    tk.Button(input_frame, text="Add", command=add_item).pack(side=tk.LEFT, padx=5)
    
    # Bind Enter key to add function
    entry.bind('<Return>', lambda event: add_item())
    
    root.mainloop()

if __name__ == "__main__":
    generate_listbox_with_input()