#!/usr/bin/python3

def makeChange(coins, total):
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

if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
