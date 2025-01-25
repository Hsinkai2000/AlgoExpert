def numberOfWaysToMakeChange(n, denoms):
    """
    Calculate the number of ways to make change for a given amount using a list of denominations.

    Args:
        n (int): The target amount for which we want to make change.
        denoms (List[int]): A list of coin denominations available to make change.

    Returns:
        int: The number of ways to make change for the target amount using the given denominations.

    Example:
        >>> numberOfWaysToMakeChange(6, [1, 5])
        2
        >>> numberOfWaysToMakeChange(10, [1, 5, 10])
        4

    The function uses dynamic programming to build up the number of ways to make change for each amount from 0 to n.
    """
    # Initialize a list to store the number of ways to make change for each amount from 0 to n
    ways = [0 for i in range(n+1)]
    # There is exactly one way to make change for 0 amount, which is using no coins
    ways[0] = 1

    # Iterate over each denomination
    for denom in denoms:
        # For each denomination, iterate over each amount from 1 to n
        for amt in range(1, n+1):
            # If the denomination is less than or equal to the current amount
            if denom <= amt:
                # Update the number of ways to make change for the current amount
                # by adding the number of ways to make change for (current amount - denomination)
                ways[amt] += ways[amt-denom]

    # Return the number of ways to make change for the amount n
    return ways[n]
