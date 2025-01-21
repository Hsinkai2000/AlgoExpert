def twoNumberSum(array, targetSum):
    htable = {}
    for num in array:
        if targetSum-num in htable:
            return [num, targetSum-num]
        else:
            htable[num] = 1
    return []
