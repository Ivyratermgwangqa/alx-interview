# 0x03. Log Parsing

## Description

This project involves creating a Python script that reads and parses log entries from standard input (stdin). The script will compute specific metrics based on the input data, including the total file size and the number of occurrences of various HTTP status codes. It is designed to handle data streams in real-time and print statistics every 10 lines or upon receiving a keyboard interruption (CTRL + C).

## Requirements

- The script must be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All files should end with a new line.
- The first line of the Python script must be `#!/usr/bin/python3`.
- The script should use the PEP 8 style (version 1.7.x).
- All files must be executable.

## Usage

1. Clone the repository and navigate to the project directory:

    ```sh
    git clone https://github.com/Ivyratermgwangqa/alx-interview.git
    cd alx-interview/0x03-log_parsing
    ```

2. Make the Python script executable:

    ```sh
    chmod +x 0-stats.py
    ```

3. Run the script with input from a log generator or any other source that provides log lines in the specified format:

    ```sh
    ./0-generator.py | ./0-stats.py
    ```

    - Alternatively, you can manually provide input by typing log lines followed by pressing Enter.

## Log Format

The input log lines must follow this format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Example:

```
192.168.1.1 - [2024-05-16 14:55:36] "GET /projects/260 HTTP/1.1" 200 1024
```

- `<IP Address>`: IP address of the client.
- `<date>`: Date and time of the request.
- `<status code>`: HTTP status code returned by the server.
- `<file size>`: Size of the file in bytes.

## Script Output

The script will print the following statistics:

- Total file size: The sum of all file sizes from the beginning.
- Number of lines by status code: Count of each status code encountered.

Example output after every 10 lines or upon keyboard interruption (CTRL + C):

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

## Handling Keyboard Interrupt

If the script receives a keyboard interruption (CTRL + C), it will print the current statistics before exiting.

## Files

- `0-stats.py`: The main Python script that reads from stdin and computes metrics.
- `README.md`: This file, providing an overview and instructions for the project.

## Author

- Lerato Mgwangqa
- [Ivyratermgwangqa](https://github.com/Ivyratermgwangqa)
```
