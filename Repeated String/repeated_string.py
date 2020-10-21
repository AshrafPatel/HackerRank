def repeatedString(s, n):
    count = 0
    l = len(s)

    for a in s:
        if a == "a":
            count+=1
    
    multiplyBy = int(n/len(s))
    counter = count*multiplyBy
    remainderBy = n%len(s)
    
    if not remainderBy == 0:
        for a in s[0:remainderBy]:
            if a == "a":
                counter +=1

    return counter