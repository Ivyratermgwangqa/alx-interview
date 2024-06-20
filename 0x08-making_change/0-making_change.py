#!/usr/bin/python3
"""
Coin Change Problem
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total.

    Parameters:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount of money.

    Returns:
    int: The fewest number of coins needed to meet the total. If the total
         cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0
    
    # Initialize the dp array with infinity for all values except 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
