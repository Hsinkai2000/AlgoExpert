def maxProfit(self, prices: List[int]) -> int:
    """
    Calculates the maximum profit that can be achieved from buying and selling a stock.

    This function takes a list of stock prices where each element represents the stock price on a given day.
    It determines the maximum profit that can be made by buying on one day and selling on another later day.

    Args:
        prices (List[int]): A list of integers representing the stock prices on different days.

    Returns:
        int: The maximum profit that can be achieved. If no profit is possible, returns 0.

    Example:
        >>> maxProfit([7, 1, 5, 3, 6, 4])
        5
        >>> maxProfit([7, 6, 4, 3, 1])
        0

    """
    l = 0
    r = 1
    maxProfit = 0

    while r < len(prices):
        print(f'l = {l}, r = {r}')
        if prices[r] < prices[l]:
            l = r

        elif prices[r] > prices[l]:
            diff = prices[r]-prices[l]
            maxProfit = max(maxProfit, diff)
        r += 1

    return maxProfit
