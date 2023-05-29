from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        prefix, suffix = [1]*len(nums), [1]*len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[len(nums) - i - 1] = suffix[len(nums) - i] * nums[len(nums) - i]
        ans = [1]*len(nums)
        for i in range(0, len(nums)):
            ans[i] = prefix[i]*suffix[i]
        return ans


print(Solution.productExceptSelf(nums=[1, 2, 3, 4]))
