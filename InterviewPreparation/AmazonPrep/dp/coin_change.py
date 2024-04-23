def coinChange(coins: list[int], amount: int) -> int:
    # Bottom Up Implementation
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

def coinChangeTopDown(coins: list[int], amount: int) -> int:
    memo = [float("inf")] * (amount + 1)
    def helper(coin, curr):
        if curr == 0:
            return 0
        if curr < 0:
            return -1
        
        num_coins = helper(coin=coin, curr=curr - coin)
        if num_coins >= 0:
            memo[curr] = min(memo[curr], num_coins + 1)
        return memo[curr] if memo[curr] != float("inf") else -1
    
    ans = float("inf")
    for coin in coins:
        ans = min(ans, helper(coin, amount))
    return ans
        

if __name__ == "__main__":
    print(coinChangeTopDown(coins=[1, 2, 5], amount=11))

