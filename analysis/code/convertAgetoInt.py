def convertAgeToInt(x):
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