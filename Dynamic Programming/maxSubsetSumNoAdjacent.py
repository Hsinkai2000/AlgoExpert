def maxSubsetSumNoAdjacent(array):
    """
    Finds the maximum sum of non-adjacent elements in the given array.

    This function takes an array of integers and returns the maximum sum
    that can be obtained by summing up non-adjacent elements. If the array
    is empty, it returns 0. If the array has only one element, it returns
    that element.

    Args:
        array (list of int): The input array of integers.

    Returns:
        int: The maximum sum of non-adjacent elements in the array.

    Example:
        >>> maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])
        330
    """

    # Check if the array is empty
    if not len(array):
        return 0  # If the array is empty, return 0

    # Check if the array has only one element
    elif len(array) == 1:
        return array[0]  # If there's only one element, return that element

    # Create a copy of the array to store the maximum sums
    maxArr = array[:]
    # Set the second element to be the maximum of the first two elements
    maxArr[1] = max(array[0], array[1])

    # Iterate through the array starting from the third element
    for i in range(2, len(array)):
        # Update the current element with the maximum sum of non-adjacent elements
        maxArr[i] = max(maxArr[i-1], maxArr[i-2] + array[i])

    # Return the last element which contains the maximum sum of non-adjacent elements
    return maxArr[-1]
