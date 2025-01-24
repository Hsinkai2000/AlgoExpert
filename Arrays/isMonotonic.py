def isMonotonic(array):
    if len(array) == 0 or len(array) == 1:
        return True

    state = 'up'
    if array[0] > array[-1]:
        state = 'down'

    for i in range(1, len(array)):
        if state == 'up':
            if array[i-1] > array[i]:
                return False
        else:
            if array[i-1] < array[i]:
                return False
    return True
