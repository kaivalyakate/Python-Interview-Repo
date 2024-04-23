def subsets(nums: list[int]) -> list[list[int]]:
    if not nums:
        return []
    ans = []
    def dfs(curr: list, next: int):
        nonlocal ans
        ans.append(curr)

        if next >= len(nums):
            return
        
        for i in range(next, len(nums)):
            dfs(curr + [nums[i]], i+1)

    dfs([], 0)
    return ans


if __name__ == "__main__":
    print(subsets(nums=[0]))