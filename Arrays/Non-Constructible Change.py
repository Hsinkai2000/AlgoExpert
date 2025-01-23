def nonConstructibleChange(coins):
    if len(coins) == 0:
        return 1

    coins.sort()
    print(coins)
    curr = 0

    for coin in coins:
        print(str(curr) + " | " + str(coin))
        if (curr+1 >= coin):
            curr += coin
        else:
            return curr+1

    return curr+1
