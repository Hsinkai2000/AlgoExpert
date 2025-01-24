def longestPeak(array):
    # Initialize the maximum length of the peak
    maxLen = 0

    # Iterate through the array starting from the second element to the second last element
    for i in range(1, len(array) - 1):
        # Check if the current element is a peak
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            # Initialize left pointer to find the left boundary of the peak
            left = i - 1
            while left > 0 and array[left] > array[left - 1]:
                left -= 1

            # Initialize right pointer to find the right boundary of the peak
            right = i + 1
            while right < len(array) - 1 and array[right] > array[right + 1]:
                right += 1

            # Calculate the length of the current peak
            peakLength = right - left + 1
            # Update the maximum length of the peak found so far
            maxLen = max(maxLen, peakLength)

    # Return the maximum length of the peak
    return maxLen
