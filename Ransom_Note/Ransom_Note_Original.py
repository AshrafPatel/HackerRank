# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for n in note:
        countN = note.count(n)
        countM = magazine.count(n)

        if countM < countN:
            print("No")
            return
    print("Yes")