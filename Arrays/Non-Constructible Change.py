def nonConstructibleChange(coins):
    if len(coins) == 0:
        return 1  # If there are no coins, the smallest change that cannot be created is 1

    coins.sort()  # Sort the coins
    curr = 0  # Initialize the current change that can be created

    # Iterate through the sorted coins
    for coin in coins:
        # If the current change + 1 is less than the coin, return the current change + 1
        if curr + 1 < coin:
            return curr + 1
        curr += coin  # Update the current change

    return curr + 1  # Return the current change + 1 if all coins are used
