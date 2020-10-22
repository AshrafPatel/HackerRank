def hourglassSum(arr):
    arrRow = 0
    arrColumn = 0
    hourGlasses = []
    while arrRow < len(arr)-2:
        arrColumn = 0
        while arrColumn < len(arr)-2:
            sum = arr[arrRow][arrColumn] + arr[arrRow][arrColumn+1] + arr[arrRow][arrColumn+2] + arr[arrRow+1][arrColumn+1] + arr[arrRow+2][arrColumn] + arr[arrRow+2][arrColumn+1] + arr[arrRow+2][arrColumn+2]
            hourGlasses.append(sum)
            arrColumn += 1
        arrRow += 1
        
    hourGlasses.sort();
    max = hourGlasses[-1]
    return max