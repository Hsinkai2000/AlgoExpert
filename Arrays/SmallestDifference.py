def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()  # Sort the first array
    arrayTwo.sort()  # Sort the second array
    arr = []  # Initialize the array to store the pair with the smallest difference

    oPt, tPt = 0, 0  # Initialize pointers for both arrays
    # Initialize the minimum difference
    minDiff = max(arrayOne[len(arrayOne) - 1], arrayTwo[len(arrayTwo) - 1])

    # Iterate through both arrays
    while oPt != len(arrayOne) and tPt != len(arrayTwo):
        # Update the minimum difference and the pair if a smaller difference is found
        if minDiff > abs(arrayOne[oPt] - arrayTwo[tPt]):
            minDiff = abs(arrayOne[oPt] - arrayTwo[tPt])
            arr = [arrayOne[oPt], arrayTwo[tPt]]

        # Move the pointer of the array with the smaller element
        if arrayOne[oPt] < arrayTwo[tPt]:
            oPt += 1
        else:
            tPt += 1

    return arr  # Return the pair with the smallest difference
