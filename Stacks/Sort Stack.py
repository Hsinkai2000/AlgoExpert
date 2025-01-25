
def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()

    sortStack(stack)
    insertInSortedOrder(stack, top)

    return stack


def insertInSortedOrder(stack, value):
    """
    Inserts a value into a stack in sorted order.

    This function takes a stack and a value, and inserts the value into the stack
    such that the stack remains sorted in ascending order. It uses recursion to 
    find the correct position for the value and then inserts it.

    Args:
        stack (list): The stack represented as a list of integers.
        value (int): The value to be inserted into the stack.

    Returns:
        None: The function modifies the stack in place and does not return anything.

    Example:
        stack = [1, 3, 5]
        insertInSortedOrder(stack, 2)
        # stack is now [1, 2, 3, 5]
    """
    if len(stack) == 0 or stack[len(stack)-1] <= value:
        stack.append(value)
        return
    top = stack.pop()
    insertInSortedOrder(stack, value)
    stack.append(top)
