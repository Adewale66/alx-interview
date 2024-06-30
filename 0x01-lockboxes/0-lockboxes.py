#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Lockboxes
    """
    visited = [0 for _ in range(len(boxes))]
    visited[0] = 1
    start = boxes[0]

    def dfs(key, visited, boxes):
        if (visited[key] == 1):
            return
        visited[key] = 1
        for key in boxes[key]:
            dfs(key, visited, boxes)

    for key in start:
        dfs(key, visited, boxes)

    return visited.count(1) == len(boxes)
