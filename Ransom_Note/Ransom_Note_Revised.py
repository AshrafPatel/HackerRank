# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    countM = Counter(magazine)
    countN = Counter(note)
    
    for key, value in countN.items():
        c = countM.get(key, 0)
        if c < value:
            print("No")
            return

    print("Yes")