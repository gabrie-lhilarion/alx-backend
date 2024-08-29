#!/usr/bin/env python3
"""
This module provides a function to calculate the perimeter of an island
represented in a grid.

The grid is a list of lists of integers where:
- 0 represents water
- 1 represents land

Each cell is square with a side length of 1, and cells are connected
horizontally or vertically (not diagonally). The grid is completely
surrounded by water, contains only one island, and has no lakes (water
inside that isn't connected to the water surrounding the island).
"""

from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculate the perimeter of the island in the given grid.

    :param grid: List of list of integers where 0 represents
    water and 1 represents land.
    :return: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell starts with 4 sides of perimeter
                perimeter += 4

                # If there's land above, subtract
                # 2 from the perimeter (shared side)
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

                # If there's land to the left,
                # subtract 2 from the perimeter (shared side)
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
