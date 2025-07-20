def open_monthly_view():
    import tkinter as tk
    from tkinter import ttk
    from logic.logic_views import get_monthly_summary
    from utils.helpers import format_currency

    win = tk.Toplevel()
    win.title("Monthly View")
    win.geometry("500x400")

    tk.Label(win, text="Year:").pack()
    year_cb = ttk.Combobox(win, values=[2023, 2024, 2025], state="readonly")
    year_cb.set(2025)
    year_cb.pack()

    tk.Label(win, text="Month:").pack()
    month_cb = ttk.Combobox(win, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state="readonly")
    month_cb.set("July")
    month_cb.pack()

    result_label = tk.Label(win, text="", font=("Arial", 14))
    result_label.pack(pady=20)

    def show_summary():
        summary = get_monthly_summary(month_cb.get(), int(year_cb.get()))
        result_label.config(text=f"Total: {format_currency(summary)}")

    tk.Button(win, text="Show Summary", command=show_summary).pack(pady=10)

    win.mainloop()