#!/usr/bin/python3

"""
Module: 0-lockboxes
Description: This module contains a function `canUnlockAll`
             in a given list of lists can be unlocked.
Usage:
    To use the function `canUnlockAll`, import the module.
    Example:
        from 0-lockboxes import canUnlockAll
        boxes = [[1], [2], [3], [4], []]
        print(canUnlockAll(boxes))  # Output: True

Dependencies:
    None

Notes:
    This module is part of the ALX interview practice projects.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked based on the keys within them.

    Args:
        boxes (list of list of int): A list where each index represents a box
                                     and each box contains a list of keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    Example:
        boxes = [[1], [2], [3], [4], []]
        print(canUnlockAll(boxes))  # True
    """
    unlocked_boxes = set()
    queue = []

    unlocked_boxes.add(0)
    queue.append(0)

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)

    return len(unlocked_boxes) == len(boxes)
