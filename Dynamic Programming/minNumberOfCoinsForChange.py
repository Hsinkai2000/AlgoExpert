def minNumberOfCoinsForChange(n, denoms):
    """
    This function calculates the minimum number of coins required to make change for a given amount.

    Parameters:
    n (int): The target amount of money.
    denoms (list): A list of coin denominations.

    Returns:
    int: The minimum number of coins needed to make change for the target amount. 
         Returns -1 if it's not possible to make change with the given denominations.
    """
    # Initialize an array to store the minimum number of coins for each amount from 0 to n.
    # Set each value to infinity initially, except for the 0th index which is 0 (base case).
    arr = [float('inf') for _ in range(n+1)]
    arr[0] = 0

    # Iterate through each denomination.
    for denom in denoms:
        # For each denomination, iterate through all amounts from 0 to n.
        for amt in range(n+1):
            # If the denomination is less than or equal to the current amount,
            # update the minimum number of coins needed for the current amount.
            if denom <= amt:
                diff = amt - denom
                arr[amt] = min(arr[amt], arr[diff] + 1)

    # If the value at index n is still infinity, it means it's not possible to make change for amount n.
    if arr[n] == float('inf'):
        return -1

    # Return the minimum number of coins needed for amount n.
    return arr[n]
