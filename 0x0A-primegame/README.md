# 0x0A. Prime Game

## Overview
This project implements a game where two players, Maria and Ben, take turns choosing prime numbers from a set of consecutive integers and removing them along with their multiples. The player who cannot make a move loses. The goal is to determine the winner of each game round and identify the overall winner.

## Requirements
- Python 3.4.3 or later
- Ubuntu 20.04 LTS

## Files
- `0-prime_game.py`: Contains the implementation of the prime game and the function to determine the winner.
- `README.md`: This file.

## Functions
### `sieve_of_eratosthenes(limit)`
Generates all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

**Arguments**:
- `limit (int)`: The upper boundary of the range to look for prime numbers.

**Returns**:
- `list`: A list of prime numbers up to the specified limit.

### `isWinner(x, nums)`
Determines the winner of each game round and returns the overall winner.

**Arguments**:
- `x (int)`: The number of game rounds.
- `nums (list of int)`: A list where each element represents the range (from 1 to n) for each game round.

**Returns**:
- `str or None`: The name of the player who won the most rounds ("Maria" or "Ben"). Returns None if the winner cannot be determined.

## Usage
Run the following command to determine the winner of the game:

```bash
./0-prime_game.py
