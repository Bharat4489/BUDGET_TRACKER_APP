import pandas as pd

def load_categories():
    df = pd.read_excel("data/categories.xlsx", engine="openpyxl")
    return df['Category'].tolist()

def add_category(new_cat):
    df = pd.read_excel("data/categories.xlsx", engine="openpyxl")
    if new_cat not in df['Category'].values:
        df = pd.concat([df, pd.DataFrame({"Category": [new_cat]})], ignore_index=True)
        df.to_excel("data/categories.xlsx", index=False, engine="openpyxl")

def delete_category(cat):
    df = pd.read_excel("data/categories.xlsx", engine="openpyxl")
    df = df[df['Category'] != cat]
    df.to_excel("data/categories.xlsx", index=False, engine="openpyxl")
