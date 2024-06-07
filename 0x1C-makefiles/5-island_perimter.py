#!/usr/bin/python3
"""Defining an island permiter of the measuring function as given"""

def island_perimeter(grid):
    """Returns pm of the island

    Grid re presents water by Zero && land by One.

    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0
    
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[1 - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2
