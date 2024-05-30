# 0x05. N Queens

The N Queens problem is a classic algorithmic problem in computer science and mathematics. The challenge is to place N non-attacking queens on an N×N chessboard. This project implements a solution using a backtracking algorithm.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the PEP 8 style (version 1.7.*)
- All files must be executable
- You are only allowed to import the `sys` module

## Usage

To run the program, use the following command:

```sh
./0-nqueens.py N
```

Where `N` is the size of the board and the number of queens. `N` must be an integer greater than or equal to 4.

## Example

```sh
./0-nqueens.py 4
```

This will output the possible solutions for a 4x4 board, such as:

```sh
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Implementation

### 0-nqueens.py

This script contains the implementation of the N Queens problem using a backtracking algorithm. 

#### Functions

- `is_safe(board, row, col)`: Checks if it's safe to place a queen at `board[row][col]`.
- `solve_nqueens(N)`: Solves the N Queens problem and returns all solutions.
- `print_solutions(solutions)`: Prints the solutions in the required format.

#### Main Execution

The script handles command-line arguments to get the value of `N`. It validates the input to ensure `N` is an integer greater than or equal to 4. If the input is invalid, it prints an appropriate error message and exits with a status code of 1. If the input is valid, it solves the N Queens problem and prints all possible solutions.

### Example Run

```sh
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- This project is part of the curriculum for the ALX Software Engineering program.
- Special thanks to the authors of the resources listed in the "Additional Resources" section for their helpful tutorials and documentation.
```
