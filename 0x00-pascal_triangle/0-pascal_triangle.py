#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's Triangle with 'n' rows.

    Pascal's Triangle is a triangular array of binomial coefficients.
    This function returns a list of lists where each inner list represents
    a row in the triangle.

    Args:
    - n (int): The number of rows to generate. Must be an integer.

    Returns:
    - List[List[int]]: A list of lists representing Pascal's Triangle.
      If 'n' is less than or equal to zero, returns an empty list.
    """
    if n <= 0:
        return []

    # The triangle starts with the first row [1]
    triangle = [[1]]

    # Generate each subsequent row
    for i in range(1, n):
        prev_row = triangle[-1]  # Get the last row
        new_row = [1]  # Each row starts with 1
        # Calculate the inner elements based on the previous row
        for j in range(1, i):
            # Add adjacent elements from the previous row
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Each row ends with 1
        triangle.append(new_row)

    return triangle
