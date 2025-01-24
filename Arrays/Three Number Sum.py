def threeNumberSum(array, targetSum):
    finalArray = []  # Initialize the final array to store triplets

    array.sort()  # Sort the array
    # Iterate through the array
    for index in range(len(array) - 2):
        l, r = index + 1, len(array) - 1  # Initialize left and right pointers
        while l < r:
            # Calculate the sum of the triplet
            sum = array[index] + array[l] + array[r]
            if sum > targetSum:
                r -= 1  # Move the right pointer left if the sum is too large
            elif sum < targetSum:
                l += 1  # Move the left pointer right if the sum is too small
            else:
                # Add the triplet to the final array
                finalArray.append([array[index], array[l], array[r]])
                l += 1
                r -= 1

    return finalArray  # Return the array of triplets
