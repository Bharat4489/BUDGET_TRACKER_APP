import os
import pandas as pd

def initialize_excel():
    if not os.path.exists("data/budget_data.xlsx"):
        df = pd.DataFrame(columns=["Year", "Month", "Weekday", "Date", "Note"])
        df.to_excel("data/budget_data.xlsx", index=False)

    if not os.path.exists("data/categories.xlsx"):
        df = pd.DataFrame({"Category": ["Food", "Transport", "Rent"]})
        df.to_excel("data/categories.xlsx", index=False)

