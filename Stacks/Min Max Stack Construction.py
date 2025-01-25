# Feel free to add new properties and methods to the class.
class MinMaxStack:
    """
    A stack data structure that supports retrieving the minimum and maximum values in constant time.

    Methods:
        __init__():
            Initializes an empty MinMaxStack.

        peek():
            Returns the top element of the stack without removing it.

        pop():
            Removes and returns the top element of the stack.

        push(number):
            Adds a new element to the top of the stack and updates the min and max values.

            Args:
                number (int): The number to be added to the stack.

        getMin():
            Returns the minimum value in the stack.

        getMax():
            Returns the maximum value in the stack.

    The class works as follows:
    - It maintains two stacks: one for the actual stack elements and one for the min and max values.
    - When a new element is pushed, it updates the min and max values based on the current element and the previous min and max values.
    - The min and max values can be retrieved in constant time by accessing the top of the minMaxStack.
    """

    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        # Write your code here.
        return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[-1]
            newMinMax["min"] = min(lastMinMax['min'], number)
            newMinMax["max"] = max(lastMinMax['max'], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[-1]['min']

    def getMax(self):
        return self.minMaxStack[-1]['max']
