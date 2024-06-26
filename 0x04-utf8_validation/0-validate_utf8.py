#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    Args:
    data (list): The data set represented by a list of integers (bytes).
    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000
    for num in data:
        # Mask to get the last 8 bits
        byte = num & 0xFF
        if num_bytes == 0:
            # Count the number of leading 1 bits
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte is of form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
