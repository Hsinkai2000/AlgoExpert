def balancedBrackets(string):
    """
    Determines if the brackets in the given string are balanced.

    Args:
        string (str): A string containing various types of brackets ('{', '}', '(', ')', '[', ']').

    Returns:
        bool: True if the brackets are balanced, False otherwise.

    The function works as follows:
    - It iterates through each character in the string.
    - If the character is an opening bracket ('{', '(', '['), it is pushed onto a stack.
    - If the character is a closing bracket ('}', ')', ']'), it checks if the stack is empty.
    - If the stack is empty, it means there is no corresponding opening bracket, so it returns False.
    - If the stack is not empty, it checks if the top of the stack is the corresponding opening bracket.
    - If it is not, it returns False.
    - If it is, it pops the top of the stack.
    - After iterating through the string, if the stack is not empty, it means there are unmatched opening brackets, so it returns False.
    - If the stack is empty, it means all brackets are matched, so it returns True.
    """
    array = []

    for c in string:
        print("current :" + c)
        if c == '{' or c == '(' or c == '[':
            array.append(c)
        elif c == '}' or c == ')' or c == ']':
            if len(array) == 0:
                return False
            if c == '}' and array[-1] != '{':
                return False
            elif c == ')' and array[-1] != '(':
                return False
            elif c == ']' and array[-1] != '[':
                return False
            else:
                array.pop(-1)

    if len(array) > 0:
        return False

    return True
