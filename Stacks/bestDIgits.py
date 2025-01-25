def bestDigits(number, numDigits):
    """
    Determines the best digits to form the largest possible number by removing a specified number of digits.

    Args:
        number (str): A string representing the original number.
        numDigits (int): The number of digits to remove from the original number.

    Returns:
        str: The largest possible number as a string after removing the specified number of digits.

    The function works as follows:
    - It initializes a stack with the first digit of the number.
    - It iterates through the remaining digits of the number.
    - For each digit, it compares it with the digits in the stack from the end to the beginning.
    - If the current digit is greater than the digit in the stack and there are still digits to remove, it removes the digit from the stack.
    - It then adds the current digit to the stack.
    - After processing all digits, if there are still digits to remove, it removes them from the end of the stack.
    - Finally, it returns the resulting stack as a string.
    """
    stack = number[0]
    for i in range(1, len(number)):
        if numDigits > 0:
            for num in range(len(stack)-1, -1, -1):
                if stack[num] < number[i] and numDigits > 0:
                    numDigits -= 1
                    stack = stack[:-1]
        stack += number[i]

    if numDigits > 0:
        diff = numDigits * -1
        stack = stack[:diff]
    return stack
