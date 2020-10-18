def sockMerchant(n, ar):
    newArr = ar
    newArr.sort()
    pair = 0
    counter = 0
    currentSock = ""
    print(newArr)

    for item in newArr:
        if currentSock == item:
            counter+=1
        else:
            count = int(counter/2)
            pair += count
            currentSock = item
            counter = 1
        print(currentSock, counter, pair)
    if counter > 1:
        pair += int(counter/2)
    return pair