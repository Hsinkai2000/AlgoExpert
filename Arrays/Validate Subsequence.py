def isValidSubsequence(array, sequence):
    # If the sequence is exactly the same as the array, return True
    if sequence == array:
        return True

    # If either the sequence or array is empty, return False
    if sequence == [] or array == []:
        return False

    curr = 0  # Initialize a pointer for the sequence

    # Iterate through the array
    for num in array:
        # If the current number matches the current sequence element, move the pointer
        if num == sequence[curr]:
            curr += 1
            # If the pointer has reached the end of the sequence, return True
            if curr == len(sequence):
                return True

    # If the end of the array is reached without matching the entire sequence, return False
    return False
