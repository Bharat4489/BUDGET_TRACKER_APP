# logic/logic_category.py
import os
import pandas as pd

def initialize_category_file():
    path = "data/categories.xlsx"
    if not os.path.exists(path):
        df = pd.DataFrame(columns=["Category", "Subcategory"])
        df.to_excel(path, index=False, engine='openpyxl')

def load_categories():
    df = pd.read_excel("data/categories.xlsx", engine="openpyxl")
    categories = df["Category"].dropna().unique().tolist()
    subcategories = {
        cat: df[df["Category"] == cat]["Subcategory"].dropna().tolist()
        for cat in categories
    }
    return subcategories

def save_categories(subcategories_dict):
    data = []
    for cat, subcats in subcategories_dict.items():
        for sub in subcats:
            data.append({"Category": cat, "Subcategory": sub})
    df = pd.DataFrame(data)
    df.to_excel("data/categories.xlsx", index=False, engine="openpyxl")

def delete_category(subcategories_dict, category):
    if category in subcategories_dict:
        del subcategories_dict[category]
    return subcategories_dict

def delete_subcategory(subcategories_dict, category, subcategory):
    if category in subcategories_dict and subcategory in subcategories_dict[category]:
        subcategories_dict[category].remove(subcategory)
    return subcategories_dict

def add_category(subcategories_dict, category):
    if category not in subcategories_dict:
        subcategories_dict[category] = []
    return subcategories_dict

def add_subcategory(subcategories_dict, category, subcategory):
    if category in subcategories_dict:
        if subcategory not in subcategories_dict[category]:
            subcategories_dict[category].append(subcategory)
    else:
        subcategories_dict[category] = [subcategory]
    return subcategories_dict
