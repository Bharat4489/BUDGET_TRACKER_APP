def open_category_manager():
    import tkinter as tk
    from tkinter import simpledialog, messagebox
    from logic.logic_category import load_categories, add_category, delete_category

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
