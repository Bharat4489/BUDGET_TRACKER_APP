import os
import pandas as pd
import platform
import subprocess

def initialize_excel():
    os.makedirs("data", exist_ok=True)  # ✅ Ensures the 'data' folder exists

    if not os.path.exists("data/budget_data.xlsx"):
        df = pd.DataFrame(columns=["Year", "Month", "Weekday", "Date", "Category", "Amount", "Note"])
        df.to_excel("data/budget_data.xlsx", index=False, engine="openpyxl")

    if not os.path.exists("data/categories.xlsx"):
        df = pd.DataFrame({"Category": ["Food", "Transport", "Rent"]})
        df.to_excel("data/categories.xlsx", index=False, engine="openpyxl")

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


