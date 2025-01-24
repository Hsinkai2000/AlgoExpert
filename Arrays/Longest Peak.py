def longestPeak(array):
    maxLen = 0

    for i in range(1, len(array) - 1):
        # Check if `i` is a peak
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            # Expand left and right to find the peak boundaries
            left = i - 1
            while left > 0 and array[left] > array[left - 1]:
                left -= 1

            right = i + 1
            while right < len(array) - 1 and array[right] > array[right + 1]:
                right += 1

            # Calculate the peak length
            peakLength = right - left + 1
            maxLen = max(maxLen, peakLength)

    return maxLen
