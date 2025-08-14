def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price  # Update the lowest price seen so far
        elif price - min_price > max_profit:
            max_profit = price - min_price  # Update the max profit

    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(maxProfit([7, 6, 4, 3, 1]))     # Output: 0
