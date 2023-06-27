from typing import List


class Solution:
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq, streak = 0, 0
        for i in range(0, len(nums)):
            if nums[i]-1 not in nums_set:
                streak = 0
                temp = nums[i]
                while True:
                    if temp in nums_set:
                        streak += 1
                        temp += 1
                    else:
                        break
                if streak > max_seq:
                    max_seq = streak
        return max_seq


print(Solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print("SOlution")