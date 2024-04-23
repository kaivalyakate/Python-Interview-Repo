import sys

def maxSubarrayLen(nums: list[int], k: int) -> int:
    counter = {}
    max_len = -1
    j = 0
    for i in range(0, len(nums)):
        num = nums[i]
        counter[num] = counter.get(num, 0) + 1
        while j < len(nums) and counter[num] > k:
            counter[nums[j]] -= 1
            j += 1
        max_len = max(max_len, i - j + 1)
    return max_len


if __name__ == "__main__":
    arr = [1, 1, 1]
    k = 0
    print(maxSubarrayLen(nums=arr, k=k))