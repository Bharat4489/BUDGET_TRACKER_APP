import os
import pandas as pd
import platform
import subprocess

def initialize_excel():
    os.makedirs("data", exist_ok=True)  # ✅ Ensures the 'data' folder exists

    # Ensure budget_data.xlsx has the required columns
    budget_path = "data/budget_data.xlsx"
    if not os.path.exists(budget_path):
        df = pd.DataFrame(columns=["Year", "Month", "Weekday", "Date", "Category", "Subcategory", "Amount", "Type", "Note"])
        df.to_excel(budget_path, index=False, engine="openpyxl")
    else:
        df = pd.read_excel(budget_path, engine="openpyxl")
        required_cols = ["Year", "Month", "Weekday", "Date", "Category", "Subcategory", "Amount", "Type", "Note"]
        for col in required_cols:
            if col not in df.columns:
                df[col] = ""
        df.to_excel(budget_path, index=False, engine="openpyxl")

    # Ensure categories.xlsx is in new format
    cat_path = "data/categories.xlsx"
    if not os.path.exists(cat_path):
        df = pd.DataFrame({
            "Category": ["Food", "Transport", "Rent", "Utilities"],
            "Subcategory": ["Groceries", "Bus", "Flat", "Electricity"]
        })
        df.to_excel(cat_path, index=False, engine="openpyxl")
    else:
        df = pd.read_excel(cat_path, engine="openpyxl")
        if "Subcategory" not in df.columns:
            df["Subcategory"] = ""
            df.to_excel(cat_path, index=False, engine="openpyxl")


# Function to open the Excel file in the default application
def open_excel_file(filename="data/budget_data.xlsx"):
    abs_path = os.path.abspath(filename)
    if os.path.exists(abs_path):
        if platform.system() == "Windows":
            os.startfile(abs_path)
        elif platform.system() == "Darwin":
            subprocess.call(["open", abs_path])
        else:
            subprocess.call(["xdg-open", abs_path])
    else:
        print(f"❌ File not found: {abs_path}")


