def countingValleys(steps, path):
    currentLevel = 0
    valleys = 0
    prevLevel = 0
    for p in path:
        prevLevel = currentLevel
        if p == "D":
            currentLevel -= 1
        elif p == "U":
            currentLevel += 1
        if (currentLevel == 0 and prevLevel == -1):
            valleys += 1
    return valleys