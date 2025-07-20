import pandas as pd

def get_monthly_summary(month, year):
    df = pd.read_excel("data/budget_data.xlsx")
    filtered = df[(df['Month'] == month) & (df['Year'] == year)]
    return filtered['Amount'].sum()

