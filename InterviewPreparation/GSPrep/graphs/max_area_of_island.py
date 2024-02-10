def maxAreaOfIsland(grid: list[list[int]]) -> int:
    def area(i, j):
        nonlocal current_area
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return
        grid[i][j] = 0
        current_area += 1
        for (x, y) in paths:
            area(i + x, j + y)

    paths = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    max_area = 0
    current_area = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                current_area = 0
                area(i, j)
                max_area = max(max_area, current_area)
    
    return max_area


if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 1, 1]
    ]
    area = maxAreaOfIsland(grid=grid)
    print(area)