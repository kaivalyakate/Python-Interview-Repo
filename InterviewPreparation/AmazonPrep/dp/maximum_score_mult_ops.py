def maximum_score(nums: list[int], multipliers: list[int]) -> int:
    n, m = len(nums), len(multipliers)
    dp = [[0] * (n) for _ in range(m)]   
    def helper(i: int, left: int):
        if i == m:
            return 0 
        
        if dp[i][left] != 0:
            return dp[i][left]

        mult = multipliers[i]
        right = n - 1 - (i - left)
        dp[i][left] = max(mult * nums[left] + helper(i+1, left+1), mult * nums[right] + helper(i+1, left))
        return dp[i][left]

    return helper(0, 0)


if __name__ == "__main__":
    nums = [1,2,3]
    multipliers = [3,2,1]
    print(maximum_score(nums, multipliers))