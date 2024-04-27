#!/usr/bin/python3
"""
Module that generates Pascal's Triangle for a given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with `n` rows.
    Args:
        n (int): Number of rows to generate.
    Returns:
        list of lists: A list containing rows of Pascal's Triangle.
    """ 
    if n <= 0:
        return []
        triangle = []
        row = [1]  # First row is always [1]
    for _ in range(n):
        triangle.append(row)  # Add the current row to the triangle
        new_row = []
        new_row.append(1)  # Add the first '1'
        # Compute the elements in between
        for i in range(1, len(row)):
            new_row.append(row[i - 1] + row[i])
        new_row.append(1)  # Add the last '1'
        # Update the row to be the new row
        row = new_row
    return triangle
