from typing import List


class Solution:
    @staticmethod
    def contains_duplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums)
