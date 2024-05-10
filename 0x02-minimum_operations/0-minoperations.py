#!/usr/bin/python3
"""
0-minoperations.py - Module for calculating the minimum number of operations
                     required to achieve a given number of characters using
                     "Copy All" and "Paste" operations.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations required to achieve a given
    number of characters using "Copy All" and "Paste" operations.

    Args:
    - n (int): The target number of characters to achieve.

    Returns:
    - int: The minimum number of operations needed to reach 'n' characters.
           Returns 0 if 'n' is less than or equal to 1.

    Example:
    >>> minOperations(4)
    4
    >>> minOperations(12)
    7
    """

    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    # Find all prime factors and calculate the required operations
    while divisor <= n:
        while n % divisor == 0:
            operations += divisor  # Adding the divisor as a "Copy All" followed by divisor - 1 "Paste"
            n //= divisor  # Reduce n by the divisor
        divisor += 1  # Check the next possible divisor
    
    return operations

if __name__ == "__main__":
    # Example usage
    n = 12
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")
