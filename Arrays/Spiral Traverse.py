def spiralTraverse(array):
    # Write your code here.
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    arr = []

    print(array)

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol+1):
            arr.append(array[startRow][col])

        for row in range(startRow+1, endRow+1):
            arr.append(array[row][endCol])

        if endRow != startRow and endCol != startCol:
            for col in range(endCol-1, startCol-1, -1):
                arr.append(array[endRow][col])

            for row in range(endRow-1, startRow, -1):
                arr.append(array[row][startCol])
        else:
            break

        startCol += 1
        startRow += 1
        endRow -= 1
        endCol -= 1

    print(arr)
    return arr
