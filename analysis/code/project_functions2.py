import pandas as pd
import numpy as np

def load_dataset(path):
    df = (pd.read_csv(path)
          .drop(["Gender", "Institution Type", "IT Student", "Location", "Load-shedding", "Financial Condition", "Internet Type", "Network Type", "Class Duration", "Device"], axis = "columns"))
    numeric_var = {"Numeric Adaptability":{"Low":0, "Moderate":1, "High":2}}
    df["Numeric Adaptability"] = df["Adaptivity Level"]
    df = df.replace(numeric_var)   
    return df