def rob(nums: list[int]) -> int:
    if not nums: return 0
    if len(nums) < 2: return max(nums)
    mem = [0] * len(nums)
    mem[0], mem[1] = nums[0], max(nums[0], nums[1]) 
    for i in range(2, len(nums)):
        mem[i] = max(mem[i-1], nums[i]+mem[i-2])
    return mem[len(nums)-1]

if __name__ == "__main__":
    nums = [2, 1, 1, 2]
    print(rob(nums=nums))