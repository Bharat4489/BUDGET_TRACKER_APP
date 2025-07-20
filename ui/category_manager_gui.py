import tkinter as tk
from tkinter import simpledialog, messagebox
from logic.logic_category import load_categories, add_category, delete_category
from logic.logic_category import save_categories

def open_category_manager():
   
    win = tk.Toplevel()
    win.title("Manage Categories")
    win.geometry("400x300")

    category_list = load_categories()
    listbox = tk.Listbox(win)
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)
    for cat in category_list:
        listbox.insert(tk.END, cat)

    def on_add():
        new_cat = simpledialog.askstring("New Category", "Enter category name:", parent=win)
        if new_cat:
            add_category(new_cat)
            listbox.insert(tk.END, new_cat)

    def on_delete():
        selected = listbox.curselection()
        if selected:
            cat = listbox.get(selected[0])
            delete_category(cat)
            listbox.delete(selected[0])

    tk.Button(win, text="Add", command=on_add).pack(pady=5)
    tk.Button(win, text="Delete", command=on_delete).pack()

    win.mainloop()




## Function to open the category manager GUI
def open_category_manager(root, categories, category_cb):
    def refresh_list():
        listbox.delete(0, tk.END)
        for cat in categories:
            listbox.insert(tk.END, cat)

    def add_category():
        new_cat = new_category_entry.get().strip()
        if new_cat and new_cat not in categories:
            categories.append(new_cat)
            save_categories(categories)
            refresh_list()
            category_cb['values'] = categories
        new_category_entry.delete(0, tk.END)

    def delete_selected():
        selected = listbox.curselection()
        if selected:
            del categories[selected[0]]
            save_categories(categories)
            refresh_list()
            category_cb['values'] = categories

    cat_window = tk.Toplevel(root)
    cat_window.title("Manage Categories")
    cat_window.geometry("300x300")

    listbox = tk.Listbox(cat_window)
    listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    new_category_entry = tk.Entry(cat_window)
    new_category_entry.pack(padx=10, pady=5)

    tk.Button(cat_window, text="Add Category", command=add_category).pack(padx=10)
    tk.Button(cat_window, text="Delete Selected", command=delete_selected).pack(padx=10)

    refresh_list()
