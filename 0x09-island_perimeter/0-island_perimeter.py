#!/usr/bin/python3
"""
0-island_perimeter module
Defines the island_perimeter function that calculates the perimeter
of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the given grid.

    Args:
        grid (list of list of int): 2D grid representing the map,
        where 0 is water and 1 is land.

    Returns:
        int: The perimeter of the island.

    The function iterates through each cell in the grid.
    For each land cell (value 1),
    it checks the adjacent cells (up, down, left, right).
    If an adjacent cell is water
    (value 0) or out of grid bounds, it contributes to the perimeter.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
