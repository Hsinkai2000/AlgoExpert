def moveElementToEnd(array, toMove):
    l, r = 0, 0  # Initialize left and right pointers
    swap = False  # Initialize a flag to indicate if a swap is needed
    while r < len(array):
        if not swap:
            if array[r] != toMove:
                l += 1
                r += 1
            else:
                swap = True
                r += 1
        else:
            if array[r] != toMove:
                array[l] = array[r]
                array[r] = toMove
                l += 1
                swap = False
            else:
                r += 1

    return array  # Return the modified array
