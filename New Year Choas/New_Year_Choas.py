# Complete the minimumBribes function below.
def minimumBribes(q):
    bribeCount = 0
    #[5, 3, 1, 2, 4]
    for i, num in enumerate(q):
        # 5 is at position 0 - postion 0+1 due to array index we do + 1 to get difference
        # This provides the amount of bribes this formula
        bribeAmount = num - (i + 1)
        if bribeAmount > 2:
            print("Too chaotic")
            return           
        else:
            for j in range(i):
                if q[j] > num:
                    bribeCount+=1
    print(bribeCount)