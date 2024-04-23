def maxLuckyNumber(x: int, y: int, n: int):
    ans = float("-inf")
    def dfs(curr_num: int, curr_sum: int):
        nonlocal ans
        if curr_sum > n:
            return float("-inf")
        if curr_sum == n:
            ans = max(ans, curr_num)
            return 
        
        dfs(curr_num*10+x, curr_sum+x)
        dfs(curr_num*10+y, curr_sum+y)

    dfs(x, x)
    dfs(y, y)
    return ans


if __name__ == "__main__":
    print(maxLuckyNumber(3, 4, 13))