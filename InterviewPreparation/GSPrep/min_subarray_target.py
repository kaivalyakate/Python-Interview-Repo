import sys
from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    start = 0
    min_sub_array_len = sys.maxsize
    running_sum = 0
    for i in range(len(nums)):
        running_sum += nums[i]
        while running_sum >= target:
            min_sub_array_len = min(min_sub_array_len, i - start + 1)
            running_sum -= nums[start]
            start += 1

    return 0 if min_sub_array_len == sys.maxsize else min_sub_array_len


if __name__ == "__main__":
    print(minSubArrayLen(nums=[2,3,1,2,4,3], target=7))
