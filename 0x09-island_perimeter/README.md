# 0x09. Island Perimeter

## Description

This project focuses on calculating the perimeter of an island represented in a grid (2D array). The grid consists of water and land cells, where:
- `0` represents water
- `1` represents land

The goal is to create a function `def island_perimeter(grid):` that returns the perimeter of the island. The island is surrounded by water, and there is only one island without any lakes (water inside the island that isn't connected to the surrounding water).

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder is mandatory
- Code should use the PEP 8 style (version 1.7)
- No module imports are allowed
- All modules and functions must be documented
- All files must be executable

## Files

- `0-island_perimeter.py`: Contains the `island_perimeter` function.
- `0-main.py`: Contains the main script to test the function.
- `README.md`: Contains project description and requirements.

## Function

### island_perimeter

```python
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid representing the map, where 0 is water and 1 is land.

    Returns:
        int: The perimeter of the island.
    """
```

### Example

Given the following grid:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

The function call `island_perimeter(grid)` should return `12`.

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/Ivyratermgwangqa/alx-interview.git
   ```

2. Navigate to the project directory:
   ```sh
   cd alx-interview/0x09-island_perimeter
   ```

3. Run the main script to test the function:
   ```sh
   ./0-main.py
   ```

## Resources

- Python Official Documentation: [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- GeeksforGeeks: [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/multidimensional-arrays-in-python/)
- TutorialsPoint: [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- YouTube Tutorials: [Python 2D arrays and lists](https://www.youtube.com/results?search_query=python+2d+arrays+and+lists)

## Author

- [Lerato Mgwangqa](https://github.com/Ivuratermgwangqa)

```
