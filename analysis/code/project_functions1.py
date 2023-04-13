import pandas as pd
import numpy as np


def load_dataset(path):
    df = (pd.read_csv(path)
          .drop(["Education Level", "Institution Type", "IT Student", "Self Lms", "Load-shedding", "Internet Type", "Network Type", "Class Duration", "Device"], axis="columns"))
    return df

def convert_age_to_int(x):
    """Converts the age range (x) to an integer.

    Args:
        x (String): Age range to be converted

    Returns:
        int: returns an integer of the first age in the age range
    """
    if x == "1-5":
        return 1
    elif x == "6-10":
        return 6
    elif x == "11-15":
        return 11
    elif x == "16-20":
        return 16
    elif x == "21-25":
        return 21
    elif x == "26-30":
        return 26
    else:
        print("error")