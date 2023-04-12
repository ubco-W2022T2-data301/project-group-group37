import pandas as pd

def combineDeviceInternet(df):
    if((df["Internet Type"] == "Wifi") and (df["Device"] == "Computer")):
        return "W + C"
    elif((df["Internet Type"] == "Wifi") and (df["Device"] == "Tab")):
        return "W + T"
    elif((df["Internet Type"] == "Wifi") and (df["Device"] == "Mobile")):
        return "W + M"
    elif((df["Internet Type"] == "Mobile Data") and (df["Device"] == "Computer")):
        return "MD + C"
    elif((df["Internet Type"] == "Mobile Data") and (df["Device"] == "Tab")):
        return "MD + T"
    else: 
        return "MD + M"
    
def addCombination(df):
    df["Combination"] = combineDeviceInternet(df)
    return df

def load_process_dataset(path):
    df = (pd.read_csv(path)
        .drop(["Gender", "Age", "Education Level", "Institution Type", "IT Student", "Location", "Load-shedding", "Financial Condition", "Class Duration", "Self Lms"], axis = "columns")  
        .apply(addCombination, axis = "columns")
    )
    
    return df
