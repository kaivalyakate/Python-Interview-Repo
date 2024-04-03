from collections import defaultdict

def delete_and_earn(nums: list[int]) -> int:
    points = defaultdict(int)
    max_num = 0
    for num in nums:
        points[num] += num
        max_num = max(max_num, num)
    
    dp = [0] * (max_num + 1)
    dp[1] = points[1]

    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i-2] + points[i])
    
    return dp[max_num]

if __name__ == "__main__":
    nums = [3,4,2]
    delete_and_earn(nums=nums)