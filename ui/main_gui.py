def run_main_app():
    import tkinter as tk
    from tkinter import ttk, messagebox
    from tkcalendar import DateEntry
    from logic.excel_handler import initialize_excel, open_excel_file
    from logic.logic_category import load_categories
    from logic.logic_expense import add_expense
    from ui.category_manager_gui import open_category_manager
    from ui.views_gui import open_monthly_view
    from ui.category_manager_gui import open_category_manager

    initialize_excel()
    categories = load_categories()

    root = tk.Tk()
    root.title("Personal Budget Tracker")
    root.geometry("600x500")

    tk.Label(root, text="Date:").pack()
    date_entry = DateEntry(root, width=20, date_pattern='yyyy-mm-dd')
    date_entry.pack(pady=5)

    tk.Label(root, text="Category:").pack()
    category_cb = ttk.Combobox(root, values=categories, state="readonly")
    category_cb.set("Select category")
    category_cb.pack(pady=5)

    # Inside run_main_app() — after the category_cb definition
    manage_cat_btn = ttk.Button(root, text="Manage Categories", command=lambda: open_category_manager(root, categories, category_cb))
    manage_cat_btn.pack(pady=5)

    tk.Label(root, text="Amount (₹):").pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=5)

    tk.Label(root, text="Note (optional):").pack()
    note_entry = tk.Entry(root)
    note_entry.pack(pady=5)

    def on_add():
        date = date_entry.get()
        category = category_cb.get()
        amount = amount_entry.get()
        note = note_entry.get()

        if category == "Select category" or not amount.strip():
            messagebox.showerror("Error", "Please select category and enter amount.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be numeric.")
            return

        add_expense(date, category, amount, note)
        messagebox.showinfo("Success", f"✅ ₹{amount} added under '{category}' on {date}")
        amount_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)

    tk.Button(root, text="Add Expense", command=on_add).pack(pady=10)
    tk.Button(root, text="📂 Open Excel", command=open_excel_file).pack(pady=5)

    menu = tk.Menu(root)
    category_menu = tk.Menu(menu, tearoff=0)
    category_menu.add_command(label="Manage Categories", command=open_category_manager)
    menu.add_cascade(label="Categories", menu=category_menu)

    view_menu = tk.Menu(menu, tearoff=0)
    view_menu.add_command(label="View Summary", command=open_monthly_view)
    menu.add_cascade(label="Summary", menu=view_menu)

    root.config(menu=menu)
    root.mainloop()
