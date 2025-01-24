def twoNumberSum(array, targetSum):
    htable = {}  # Initialize a hash table
    for num in array:
        # Check if the complement of the current number exists in the hash table
        if targetSum - num in htable:
            return [num, targetSum - num]  # Return the pair if found
        else:
            htable[num] = 1  # Add the current number to the hash table
    return []  # Return an empty list if no pair is found
