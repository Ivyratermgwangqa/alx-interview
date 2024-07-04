#!/usr/bin/python3
"""
Module: 0-prime_game

This module contains the implementation of a game where two players,
Maria and Ben,take turns picking prime numbers and removing them
and their multiples from a set of consecutive integers. The player
who cannot make a move loses the game.

Functions:
- sieve_of_eratosthenes(limit): Returns a list of all prime numbers
up to a given limit.
- isWinner(x, nums): Determines the winner of each game round and
returns the overall winner.
"""


def sieve_of_eratosthenes(limit):
    """
    Generate all prime numbers up to a given limit using the Sieve
    of Eratosthenes algorithm.

    Args:
    limit (int): The upper boundary of the range to look for prime
    numbers.

    Returns:
    list: A list of prime numbers up to the specified limit.
    """
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
    return primes


def isWinner(x, nums):
    """
    Determine the winner of each game round and return the overall winner.

    Maria and Ben take turns picking prime numbers and removing them
    and their multiples from a set of consecutive integers. Maria always
    goes first.

    Args:
    x (int): The number of game rounds.
    nums (list of int): A list where each element represents the range
    (from 1 to n) for each game round.

    Returns:
    str or None: The name of the player who won the most rounds
    ("Maria" or "Ben").
                 Returns None if the winner cannot be determined.
    """
    if x == 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    def play_game(n):
        """
        Simulate a single round of the game with a given range (1 to n).

        Args:
        n (int): The upper boundary of the range to play the game with.

        Returns:
        int: The player who wins the round (0 for Maria, 1 for Ben).
        """
        nonlocal primes
        available = set(range(1, n + 1))
        current_player = 0  # Maria starts first (0 -> Maria, 1 -> Ben)
        while available:
            move_made = False
            for prime in primes:
                if prime in available:
                    multiples = {k for k in range(prime, n + 1, prime)}
                    available -= multiples
                    move_made = True
                    current_player = 1 - current_player
                    break
            if not move_made:
                break
        return 1 - current_player  # Return the player who made the last move

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
