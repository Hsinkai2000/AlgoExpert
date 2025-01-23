def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    arr = []

    oPt, tPt = 0, 0
    minDiff = max(arrayOne[len(arrayOne)-1], arrayTwo[len(arrayTwo)-1])

    while oPt != len(arrayOne) and tPt != len(arrayTwo):
        if (minDiff > abs(arrayOne[oPt] - arrayTwo[tPt])):
            minDiff = abs(arrayOne[oPt] - arrayTwo[tPt])
            arr = [arrayOne[oPt], arrayTwo[tPt]]

        if (arrayOne[oPt] < arrayTwo[tPt]):
            oPt += 1
        else:
            tPt += 1

    return arr
