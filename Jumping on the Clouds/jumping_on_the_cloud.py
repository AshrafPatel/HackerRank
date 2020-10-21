# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = 0
    i = 0
    l = len(c)
    print(c)
    while i < l:
        print(i, steps)
        if i+2  c[i+2] or c[i+1] == c[i+2] else 1
            steps += 1
        elif i+1 < l:
            i += 1
            steps += 1
        else:
            i+=1
    return steps