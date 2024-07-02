#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Lockboxes
    """
    visited = set()

    def dfs(key):
        if (key in visited or key >= len(boxes)):
            return
        visited.add(key)
        for room in boxes[key]:
            dfs(room)

    dfs(0)

    return len(visited) == len(boxes)
