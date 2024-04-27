def pascal_triangle(n):
    if n <= 0:
        return []

    # Start with the first row
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Every row starts with 1
        # Add the values between the first and last element of the row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle
