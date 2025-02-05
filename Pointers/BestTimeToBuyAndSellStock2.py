def maxProfit(self, prices: List[int]) -> int:
    """
    Calculates the maximum profit that can be achieved from buying and selling a stock.

    This function takes a list of stock prices where each element represents the price of the stock on a given day.
    It determines the maximum profit that can be made by buying on one day and selling on another later day.

    Args:
        prices (List[int]): A list of integers representing the stock prices on different days.

    Returns:
        int: The maximum profit that can be achieved from the given list of stock prices.

    Example:
        >>> maxProfit([7, 1, 5, 3, 6, 4])
        5
        >>> maxProfit([7, 6, 4, 3, 1])
        0

    Notes:
        - The function uses a two-pointer approach to traverse the list of prices.
        - It keeps track of the left pointer (l) for the buying day and the right pointer (r) for the selling day.
        - The maximum profit is updated whenever a higher profit is found.
        - If the price at the right pointer is less than the price at the left pointer, the left pointer is updated to the right pointer.
        - The function also handles cases where the prices are in descending order, resulting in no profit.
    """
    l = 0
    r = 1
    maxProfit = 0
    currProfit = 0

    while r < len(prices):
        print(f'l = {l}, r = {r}')
        if prices[r] < prices[l]:
            l = r

        elif prices[r] > prices[l]:
            diff = prices[r]-prices[l]
            currProfit = max(currProfit, diff)
        if r < len(prices)-1:
            if prices[r] > prices[r+1]:
                maxProfit += currProfit
                currProfit = 0
                l = r+1
                r += 1
        else:
            maxProfit += currProfit

        r += 1

    return max(maxProfit, currProfit)
