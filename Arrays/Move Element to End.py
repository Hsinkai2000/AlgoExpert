def moveElementToEnd(array, toMove):
    l, r = 0, 0
    swap = False
    while r < len(array):
        if swap == False:
            if array[r] != toMove:
                l += 1
                r += 1
            else:
                swap = True
                r += 1
        elif swap == True:
            if array[r] != toMove:
                array[l] = array[r]
                array[r] = toMove
                l += 1
                swap = False
            else:
                r += 1

    return array
