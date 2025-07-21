def run_main_app():
    import tkinter as tk
    from tkinter import ttk, messagebox
    from tkcalendar import DateEntry
    from logic.excel_handler import initialize_excel, open_excel_file
    from logic.logic_category import load_categories
    from logic.logic_expense import add_expense
    from ui.category_manager_gui import open_category_manager
    from ui.views_gui import open_monthly_view

    initialize_excel()
    subcategories_dict = load_categories()
    all_categories = list(subcategories_dict.keys())

    root = tk.Tk()
    root.title("Personal Budget Tracker")
    root.geometry("600x520")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    tk.Label(root, text="Date:").pack()
    date_entry = DateEntry(root, width=20, date_pattern='yyyy-mm-dd')
    date_entry.pack(pady=5)

    tk.Label(root, text="Category:").pack()
    category_cb = ttk.Combobox(root, state="normal")
    category_cb.pack(pady=5)

    tk.Label(root, text="Subcategory:").pack()
    subcategory_cb = ttk.Combobox(root, state="normal")
    subcategory_cb.pack(pady=5)

    tk.Label(root, text="Amount (₹):").pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=5)

    tk.Label(root, text="Note (optional):").pack()
    note_entry = tk.Entry(root)
    note_entry.pack(pady=5)

    

    # 🔎 Search-as-you-type filtering
    def bind_search_filter(combobox, full_values):
        def on_keyrelease(event):
            typed = combobox.get().lower()
            if typed == "":
                combobox['values'] = full_values
            else:
                filtered = [val for val in full_values if typed in val.lower()]
                combobox['values'] = filtered
                combobox.event_generate('<Down>')
        combobox.bind('<KeyRelease>', on_keyrelease)

    bind_search_filter(category_cb, all_categories)
    bind_search_filter(subcategory_cb, [])


    # 🔁 Update subcategories when a category is selected
    def update_subcategories(event=None):
        selected_cat = category_cb.get()
        subcats = subcategories_dict.get(selected_cat, [])
        subcategory_cb['values'] = subcats
        subcategory_cb.set("")
        bind_search_filter(subcategory_cb, subcats)  # ✅ Added live filter

    category_cb.bind("<<ComboboxSelected>>", update_subcategories)

    def refresh_comboboxes():
        nonlocal subcategories_dict, all_categories
        subcategories_dict = load_categories()
        all_categories = list(subcategories_dict.keys())
        category_cb['values'] = all_categories
        subcategory_cb.set("")
        category_cb.set("")
        bind_search_filter(category_cb, all_categories)

    def on_add():
        date = date_entry.get()
        category = category_cb.get()
        subcategory = subcategory_cb.get()
        amount = amount_entry.get()
        note = note_entry.get()

        # 🛑 Check if selected values are valid
        if category not in subcategories_dict:
            messagebox.showerror("Invalid Category", f"'{category}' is not a valid category.")
            return
        if subcategory not in subcategories_dict[category]:
            messagebox.showerror("Invalid Subcategory", f"'{subcategory}' is not a valid subcategory under '{category}'.")
            return
        if not amount.strip():
            messagebox.showerror("Error", "Amount is required.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        main_category = f"{category}"
        sub_category  = f"{subcategory}"
        add_expense(date, main_category,sub_category, amount, note)
        messagebox.showinfo("Success", f"✅ ₹{amount} added under '{main_category}-{sub_category}'on {date}")
        amount_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)

    # Buttons
    tk.Button(root, text="Add Expense", command=on_add).pack(pady=10)
    tk.Button(root, text="📂 Open Excel", command=open_excel_file).pack(pady=5)
    tk.Button(root, text="Manage Categories & Subcategories", command=lambda: [open_category_manager(root), refresh_comboboxes()]).pack(pady=5)

    # Menu
    menu = tk.Menu(root)
    category_menu = tk.Menu(menu, tearoff=0)
    category_menu.add_command(label="Manage Categories", command=lambda: [open_category_manager(root), refresh_comboboxes()])
    menu.add_cascade(label="Categories", menu=category_menu)

    view_menu = tk.Menu(menu, tearoff=0)
    view_menu.add_command(label="View Summary", command=open_monthly_view)
    menu.add_cascade(label="Summary", menu=view_menu)

    root.config(menu=menu)

    refresh_comboboxes()
    root.mainloop()
