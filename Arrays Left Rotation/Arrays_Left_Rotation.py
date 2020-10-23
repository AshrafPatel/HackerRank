# Complete the rotLeft function below.
def rotLeft(a, d):
    newArr = [None]*len(a)
    for i in range(len(a)):
        newIdx = i-d
        while newIdx < 0:
            newIdx = len(a) - abs(newIdx)
        newArr[newIdx] = a[i]
    return newArr