0x04. UTF-8 Validation

This project involves implementing a function to validate whether a given dataset represents a valid UTF-8 encoding. The UTF-8 encoding is a variable-width character encoding used for electronic communication. It can encode characters in one to four bytes.

## Project Overview

### Objective

Write a method that determines if a given data set represents a valid UTF-8 encoding.

### Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.x)
- All your files must be executable

### Concepts to Learn

- Bitwise Operations in Python
- UTF-8 Encoding Scheme
- Data Representation
- List Manipulation in Python
- Boolean Logic

## Files

- `0-validate_utf8.py`: Contains the implementation of the UTF-8 validation function.
- `0-main.py`: Main file for testing the implementation.
- `README.md`: This file containing a description of the project.

## Implementation Details

### `0-validate_utf8.py`

This file contains the function `validUTF8(data)` which determines if a given data set represents a valid UTF-8 encoding.

```python
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
    
    # Masks for checking the leading byte
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
```

### `0-main.py`

This file is used to test the `validUTF8` function with various test cases.

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
```

## How to Run

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your_username/alx-interview.git
   cd alx-interview/0x04-utf8_validation
   ```

2. **Make the Python files executable**:

   ```sh
   chmod +x 0-validate_utf8.py 0-main.py
   ```

3. **Run the test script**:

   ```sh
   ./0-main.py
   ```

## Additional Resources

- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [Python Bitwise Operators](https://www.programiz.com/python-programming/bitwise-operators)

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.
```
