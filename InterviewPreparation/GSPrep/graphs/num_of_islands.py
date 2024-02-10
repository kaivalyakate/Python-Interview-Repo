from collections import deque
def numOfIslands(grid: list[list[int]]) -> int:
    paths = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    def mark_island(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        for (x, y) in paths:
            mark_island(i + x, j + y)

    num_of_islands = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "1":
                num_of_islands += 1
                mark_island(i, j)
    
    return num_of_islands


if __name__ == "__main__":
    grid = [
        [1, 0, 0],
        [1, 0, 1],
        [1, 0, 0]
    ]
    numOfIslands(grid=grid)