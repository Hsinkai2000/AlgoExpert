def isValidSubsequence(array, sequence):
    if sequence == array:
        return True

    if sequence == [] or array == []:
        return False

    curr = 0

    for num in array:
        if num == sequence[curr]:
            curr += 1
            if curr == len(sequence):
                return True

    return False
