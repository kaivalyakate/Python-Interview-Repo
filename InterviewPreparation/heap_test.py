import datetime
from typing import List
import collections


class Solution:
    @staticmethod
    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        nums_map = {}
        for i in nums1:
            if i in nums_map.keys():
                nums_map[i] += 1
            else:
                nums_map[i] = 1
        ans = []
        for i in nums2:
            if i in nums_map.keys() and nums_map[i] > 0:
                nums_map[i] -= 1
                ans.append(i)
        return ans


print(Solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))