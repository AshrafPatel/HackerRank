# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    currentNum = 1
    counter = 0
    length = len(arr)
    print(arr)
    i = 0
    
    while i < length:
        if arr[i] == currentNum:
            if arr[i] == i+1:
                currentNum += 1
            else:
                arr[i], arr[currentNum-1] = arr[currentNum-1], arr[i]
                currentNum+=1
                counter+=1
                i=0
        i+=1
    return counter