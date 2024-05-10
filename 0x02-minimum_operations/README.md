# 0x02. Minimum Operations

## Project Description
This project involves creating an algorithm that calculates the minimum number of operations required to achieve a given number of characters in a text file. The operations that can be used are "Copy All" and "Paste". The objective is to determine the optimal sequence of operations to get the specified number of characters.

## Approach
To solve the problem, the algorithm considers the prime factorization of the target number `n`. The reasoning behind this approach is that the operations required to achieve `n` characters can be derived from the sum of its prime factors.

- A "Copy All" operation allows duplication of the current content.
- A "Paste" operation adds the copied content to the existing text.
- To reach `n` characters from a single "H", the efficient method involves repeated "Copy All" and "Paste" operations.

The key to minimizing operations is the prime factorization:
- For each prime factor `d`, a single "Copy All" followed by `d - 1` "Paste" operations achieves the desired multiplication.
- The total operations required are the sum of all prime factors.

## Implementation
- The main logic is contained in the `minOperations` function, which takes an integer `n` and returns the minimum number of operations needed to achieve `n` characters.
- If `n` is less than or equal to 1, the function returns `0`, as it's either impossible or already has the desired result.
- For prime factors `d`, the algorithm performs one "Copy All" followed by multiple "Paste" operations, reducing `n` by the divisor at each step.

## Requirements
- Python 3.4.3 or later.
- The project will be tested on Ubuntu 20.04 LTS.
- PEP 8 style compliance is expected.

## Usage
1. Clone this repository.
2. Import the `minOperations` function into your Python script or use the provided `0-main.py` to test different cases.
3. Call `minOperations(n)` with the desired number of characters to calculate the minimum operations required.

### Example
```python
from 0-minoperations import minOperations

print(minOperations(4))  # Output: 4
print(minOperations(12)) # Output: 7
```

## Project Structure
- `0-minoperations.py`: Contains the implementation of the `minOperations` function.
- `0-main.py`: A sample test script to test the `minOperations` function.
- `README.md`: This file, providing information about the project.

## License
This project is open-source and licensed under the MIT License.
