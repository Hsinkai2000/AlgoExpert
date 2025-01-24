def sortedSquaredArray(array):
    # Square each element in the array
    for i in range(len(array)):
        array[i] *= array[i]

    array.sort()  # Sort the squared elements
    return array  # Return the sorted squared array
