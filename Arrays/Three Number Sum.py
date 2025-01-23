def threeNumberSum(array, targetSum):
    finalArray = []

    array.sort()
    for index in range(len(array)-2):
        l, r = index+1, len(array)-1
        while l < r:
            sum = array[index] + array[l] + array[r]
            if sum > targetSum:
                r -= 1
            elif sum < targetSum:
                l += 1
            else:
                finalArray.append([array[index], array[l], array[r]])
                l += 1
                r -= 1

    return finalArray
