# Lockboxes Project

## Description
This project contains a function `canUnlockAll` that determines if all boxes in a given list can be unlocked based on the keys contained within those boxes. The function is part of a coding exercise to understand graph traversal, set operations, and queue-based algorithms in Python.

## Installation
1. Clone or download this repository.
2. Ensure you have Python installed on your system. This project was developed and tested with Python 3.4.3.
3. To execute the code, ensure the files are executable and have the correct permissions:
   ```bash
   chmod +x 0-lockboxes.py main_0.py
   ```

## Usage
To use the `canUnlockAll` function:
1. Import the function from the module:
   ```python
   from 0-lockboxes import canUnlockAll
   ```

2. Pass a list of lists representing boxes and their keys to the function:
   ```python
   boxes = [[1], [2], [3], [4], []]
   result = canUnlockAll(boxes)
   print("Can unlock all boxes:", result)  # Expected output: True
   ```

## Testing
To test the functionality, you can run the provided test script `main_0.py`:
```bash
./main_0.py
```
It should output results indicating whether the boxes can be unlocked.

## Contributing
If you'd like to contribute to this project, feel free to open issues or submit pull requests on GitHub. Make sure your code adheres to PEP 8 style guidelines.

## License
This project is released under the MIT License. See the `LICENSE` file for more details.
```

### Explanation of Each Section
- **Title and Description**: A brief explanation of the project.
- **Installation**: Instructions on setting up the project.
- **Usage**: Information on how to use the primary function.
- **Testing**: Instructions on running the test script.
- **Contributing**: Guidelines for contributing to the project.
- **License**: Specifies the project's license (if applicable).

### Creating `README.md`
To create the `README.md` file, you can use a text editor or a command-line approach:

1. **Using a Text Editor**:
   - Open a text editor (e.g., `vim`, `nano`, `emacs`).
   - Write or paste the content into the editor.
   - Save the file as `README.md`.

2. **Using Command Line**:
   - Open a terminal.
   - Use `echo` or a here-doc to create the file with the desired content:
     ```bash
     cat <<EOF > README.md
     # Lockboxes Project
     ## Description
     This project contains a function `canUnlockAll`...
     EOF
     ```
