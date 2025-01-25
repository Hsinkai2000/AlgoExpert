def sunsetViews(buildings, direction):
    """
    Determines which buildings have a view of the sunset.

    Args:
        buildings (list): A list of integers representing the heights of the buildings.
        direction (str): A string indicating the direction of the sunset ("EAST" or "WEST").

    Returns:
        list: A list of indices of the buildings that have a view of the sunset.

    The function works as follows:
    - If the direction is "EAST", it iterates from the end of the list to the beginning.
    - If the direction is "WEST", it iterates from the beginning of the list to the end.
    - It keeps track of the buildings that have a view of the sunset by comparing the heights of the buildings.
    - The indices of the buildings with a sunset view are collected and returned in ascending order.
    """
    arr = []

    if buildings == []:
        return []

    if direction == "EAST":
        arr.append(len(buildings)-1)
        for i in range(len(buildings)-2, -1, -1):
            if (buildings[i] > buildings[arr[-1]]):
                arr.append(i)
    else:
        arr.append(0)
        for i in range(1, len(buildings)):
            if buildings[i] > buildings[arr[-1]]:
                arr.append(i)

    arr.sort()
    return arr
