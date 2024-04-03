def getMaximumGold(grid: list[list[int]]) -> int:
    def dfs(i, j, prev):
        if i < 0 or j < 0 or i >= len(grid) \
           or j >= len(grid[0]) or grid[i][j] == 0 or visited[i][j]:
            return prev

        visited[i][j] = 1
        prev = grid[i][j] + prev
        max_gold = 0
        for x, y in directions:
            max_gold = max(max_gold, dfs(i + x, j + y, prev))
        visited[i][j] = 0
        return max_gold

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    ans = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            visited = [[0 for __ in range(len(grid[0]))]
                           for _ in range(len(grid))]
            ans = max(ans, dfs(i, j, 0))

    return ans


if __name__ == "__main__":
    grid = [[0, 0, 0, 0, 0, 0, 32, 0, 0, 20], 
            [0, 0, 2, 0, 0, 0, 0, 40, 0, 32], 
            [13, 20, 36, 0, 0, 0, 20, 0, 0, 0], 
            [0, 31, 27, 0, 19, 0, 0, 25, 18, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 18, 0, 6], 
            [0, 0, 0, 25, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 21, 0, 30, 0, 0, 0, 0], 
            [19, 10, 0, 0, 34, 0, 2, 0, 0, 27], 
            [0, 0, 0, 0, 0, 34, 0, 0, 0, 0]]
    print(getMaximumGold(grid=grid))
