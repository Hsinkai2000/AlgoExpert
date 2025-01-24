def spiralTraverse(array):
    # Initialize the starting and ending indices for rows and columns
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    # Initialize the result array
    arr = []

    # Print the input array (for debugging purposes)
    print(array)

    # Traverse the array in a spiral order
    while startRow <= endRow and startCol <= endCol:
        # Traverse from left to right along the top row
        for col in range(startCol, endCol + 1):
            arr.append(array[startRow][col])

        # Traverse from top to bottom along the right column
        for row in range(startRow + 1, endRow + 1):
            arr.append(array[row][endCol])

        # Check if there are more rows and columns to traverse
        if endRow != startRow and endCol != startCol:
            # Traverse from right to left along the bottom row
            for col in range(endCol - 1, startCol - 1, -1):
                arr.append(array[endRow][col])

            # Traverse from bottom to top along the left column
            for row in range(endRow - 1, startRow, -1):
                arr.append(array[row][startCol])
        else:
            # Break the loop if there are no more rows and columns to traverse
            break

        # Move the boundaries inward
        startCol += 1
        startRow += 1
        endRow -= 1
        endCol -= 1

    # Print the result array (for debugging purposes)
    print(arr)
    return arr
