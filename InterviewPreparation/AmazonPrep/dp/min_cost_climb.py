def min_cost(cost: list[int]) -> int:
    dp = [0] * (len(cost) + 1)
    for i in range(2, len(cost)+1):
        dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
    return dp[len(cost)]


if __name__ == "__main__":
    cost: list[int] = [10, 15, 20]
    print(min_cost(cost=cost))