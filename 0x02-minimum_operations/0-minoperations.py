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
    while divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
