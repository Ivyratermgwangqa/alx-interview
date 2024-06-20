# 0x08. Making Change

This project tackles the classic coin change problem using dynamic programming. The goal is to find the minimum number of coins required to make up a given total amount from a list of coin denominations.

## Project Overview

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

### Prototype
```python
def makeChange(coins, total)
```

### Requirements
- Return the fewest number of coins needed to meet the total.
- If the total is 0 or less, return 0.
- If the total cannot be met by any number of coins you have, return -1.
- `coins` is a list of the values of the coins in your possession.
- The value of a coin will always be an integer greater than 0.
- Assume you have an infinite number of each denomination of coin in the list.
- The solution’s runtime will be evaluated.

## Usage

Clone the repository:

```bash
git clone https://github.com/Ivyratermgwangqa/alx-interview.git
cd alx-interview/0x08-making_change
```

Create a Python file `0-main.py` with the following content to test the function:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Expected output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
```

Make the script executable and run it:

```bash
chmod +x 0-main.py
./0-main.py
```

## Algorithm Explanation

### Dynamic Programming Approach

1. **Base Cases**:
   - If `total` is 0 or less, return 0 because no coins are needed.
   - If the total cannot be met with the given coin denominations, return -1.

2. **Dynamic Programming Table**:
   - Create a list `dp` where `dp[i]` represents the minimum number of coins required to get a total of `i`.
   - Initialize `dp[0]` to 0 since no coins are needed to make the total of 0.
   - Initialize other values in `dp` to infinity (`float('inf')`) because initially, we assume it's impossible to reach those totals.

3. **Fill the DP Table**:
   - For each coin in the list of coins, update the `dp` list by iterating through all totals from the coin value up to the total amount.
   - For each value `i` from coin to total, update `dp[i]` to be the minimum of `dp[i]` and `dp[i - coin] + 1`.

4. **Return Result**:
   - If `dp[total]` is still infinity, return -1 (since it's impossible to form the total with given coins).
   - Otherwise, return `dp[total]`.

### Code Implementation

```python
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
```

## Additional Resources

- **Python Official Documentation**:
  - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (for loops, if statements)
- **GeeksforGeeks Articles**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials**:
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=Y0ZqKpToTic)

## License

This project is licensed under the ALX Curriculum.
```
