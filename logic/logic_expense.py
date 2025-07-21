import pandas as pd
from datetime import datetime
import os

EXCEL_FILE = "data/budget_data.xlsx"

def add_expense(date_str, category,subcategory, amount, note):
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
    else:
        columns = ["Year", "Month", "Weekday", "Date", "Category", "Subcategory", "Amount", "Note"]
        df = pd.DataFrame(columns=columns)

    date = datetime.strptime(date_str, "%Y-%m-%d")
    row = {
        "Year": date.year,
        "Month": date.strftime("%B"),
        "Weekday": date.strftime("%A"),
        "Date": date_str,
        "Category": category,
        "Subcategory": subcategory,
        "Amount": amount,
        "Note": note
    }
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")
    print(f"✅ Added ₹{amount} to '{category}-{subcategory}' on {date_str} with note: {note}")


