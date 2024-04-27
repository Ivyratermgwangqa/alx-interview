#!/usr/bin/python3
"""
Module to create Pascal's Triangle of a given size `n`.
"""

def pascal_triangle(n):
    """
    Create Pascal's Triangle with `n` rows.

    :param n: Number of rows for Pascal's Triangle
    :return: List of lists representing Pascal's Triangle

    Returns an empty list if `n` is less than or equal to 0.
    """
    if n <= 0:
        return []

    # List to store all rows of Pascal's Triangle
    triangle = []
    
    # First row is always [1]
    row = [1]
    
    # Add each row to the triangle and compute the next row
    for _ in range(n):
        triangle.append(row)  # Add the current row to the triangle
        
        # Generate the next row based on the current row
        new_row = []
        
        # Add the first '1'
        new_row.append(1)
        
        # Compute the elements in between
        for i in range(1, len(row)):
            new_row.append(row[i - 1] + row[i])
        
        # Add the last '1'
        new_row.append(1)
        
        # Set the new row for the next iteration
        row = new_row
    
    return triangle
