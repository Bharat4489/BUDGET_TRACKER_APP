# ui/category_manager_gui.py
import tkinter as tk
from tkinter import ttk
from logic.logic_category import *

def open_category_manager(root):
    subcategories_dict = load_categories()

    def refresh_all():
        category_listbox.delete(0, tk.END)
        for cat in subcategories_dict:
            category_listbox.insert(tk.END, cat)
        update_subcategory_listbox()
        subcat_cat_combo['values'] = list(subcategories_dict.keys())


    def update_subcategory_listbox():
        subcategory_listbox.delete(0, tk.END)
        selected_cat = category_listbox.get(tk.ACTIVE)
        if selected_cat in subcategories_dict:
            for sub in subcategories_dict[selected_cat]:
                subcategory_listbox.insert(tk.END, sub)

    def add_new_category():
        new_cat = category_entry.get().strip()
        if new_cat:
            add_category(subcategories_dict, new_cat)
            save_categories(subcategories_dict)
            refresh_all()
            category_entry.delete(0, tk.END)

    def delete_selected_category():
        selected = category_listbox.curselection()
        if selected:
            cat = category_listbox.get(selected[0])
            delete_category(subcategories_dict, cat)
            save_categories(subcategories_dict)
            refresh_all()

    def add_new_subcategory():
        cat = subcat_cat_combo.get().strip()
        sub = subcategory_entry.get().strip()
        if cat and sub:
            add_subcategory(subcategories_dict, cat, sub)
            save_categories(subcategories_dict)
            update_subcategory_listbox()
            subcategory_entry.delete(0, tk.END)

    def delete_selected_subcategory():
        selected_cat = category_listbox.get(tk.ACTIVE)
        selected = subcategory_listbox.curselection()
        if selected_cat and selected:
            sub = subcategory_listbox.get(selected[0])
            delete_subcategory(subcategories_dict, selected_cat, sub)
            save_categories(subcategories_dict)
            update_subcategory_listbox()

    win = tk.Toplevel(root)
    win.title("Manage Categories and Subcategories")
    win.geometry("500x600")

    # Category Section
    tk.Label(win, text="Categories").pack()
    category_listbox = tk.Listbox(win, height=6)
    category_listbox.pack(fill=tk.X, padx=10)
    category_listbox.bind("<<ListboxSelect>>", lambda e: update_subcategory_listbox())

    category_entry = tk.Entry(win)
    category_entry.pack(padx=10, pady=2)
    tk.Button(win, text="Add Category", command=add_new_category).pack(padx=10)
    tk.Button(win, text="Delete Selected Category", command=delete_selected_category).pack(padx=10, pady=5)

    # Subcategory Section
    tk.Label(win, text="Subcategories").pack()
    subcategory_listbox = tk.Listbox(win, height=6)
    subcategory_listbox.pack(fill=tk.X, padx=10)

    subcat_cat_combo = ttk.Combobox(win)
    subcat_cat_combo.pack(padx=10, pady=2)
    subcategory_entry = tk.Entry(win)
    subcategory_entry.pack(padx=10, pady=2)
    tk.Button(win, text="Add Subcategory", command=add_new_subcategory).pack(padx=10)
    tk.Button(win, text="Delete Selected Subcategory", command=delete_selected_subcategory).pack(padx=10, pady=5)

    refresh_all()
