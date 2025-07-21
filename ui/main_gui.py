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

    def refresh_comboboxes():
        nonlocal subcategories_dict
        subcategories_dict = load_categories()
        category_cb['values'] = list(subcategories_dict.keys())
        category_cb.set("Select category")
        subcategory_cb.set("")

    def update_subcategories(event=None):
        selected_cat = category_cb.get()
        subcats = subcategories_dict.get(selected_cat, [])
        subcategory_cb['values'] = subcats
        subcategory_cb.set("Select subcategory")

    root = tk.Tk()
    root.title("Personal Budget Tracker")
    root.geometry("600x520")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    tk.Label(root, text="Date:").pack()
    date_entry = DateEntry(root, width=20, date_pattern='yyyy-mm-dd')
    date_entry.pack(pady=5)

    tk.Label(root, text="Category:").pack()
    category_cb = ttk.Combobox(root, state="readonly")
    category_cb.pack(pady=5)
    category_cb.bind("<<ComboboxSelected>>", update_subcategories)

    tk.Label(root, text="Subcategory:").pack()
    subcategory_cb = ttk.Combobox(root, state="readonly")
    subcategory_cb.pack(pady=5)

    tk.Label(root, text="Amount (₹):").pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=5)

    tk.Label(root, text="Note (optional):").pack()
    note_entry = tk.Entry(root)
    note_entry.pack(pady=5)

    def on_add():
        date = date_entry.get()
        category = category_cb.get()
        subcategory = subcategory_cb.get()
        amount = amount_entry.get()
        note = note_entry.get()

        if category == "Select category" or subcategory == "Select subcategory" or not amount.strip():
            messagebox.showerror("Error", "Please select category, subcategory and enter amount.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be numeric.")
            return

        full_category = f"{category} > {subcategory}"
        add_expense(date, full_category, amount, note)
        messagebox.showinfo("Success", f"✅ ₹{amount} added under '{full_category}' on {date}")
        amount_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)

    # Buttons
    tk.Button(root, text="Add Expense", command=on_add).pack(pady=10)
    tk.Button(root, text="📂 Open Excel", command=open_excel_file).pack(pady=5)

    # Category manager (single button)
    tk.Button(root, text="Manage Categories & Subcategories", command=lambda: [open_category_manager(root), refresh_comboboxes()]).pack(pady=5)

    # Menu bar
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
