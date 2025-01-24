def isMonotonic(array):
    # If the array has 2 or fewer elements, it is monotonic by default
    if len(array) <= 2:
        return True

    # Determine the initial state (increasing or decreasing)
    state = 'up'
    if array[0] > array[-1]:
        state = 'down'

    # Iterate through the array to check if it is monotonic
    for i in range(1, len(array)):
        if state == 'up':
            # If the state is 'up' and a decreasing pair is found, return False
            if array[i-1] > array[i]:
                return False
        else:
            # If the state is 'down' and an increasing pair is found, return False
            if array[i-1] < array[i]:
                return False

    # If no violations are found, the array is monotonic
    return True
