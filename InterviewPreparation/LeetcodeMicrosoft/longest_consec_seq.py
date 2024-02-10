from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = {i: 0 for i in nums}
        result = 0
        for i in nums:
            numset[i] = 1
            count = 1
            num = i + 1
            while num in list(numset.keys()) and numset[num] == 0:
                numset[num] = 1
                count += 1
                num += 1

            num = i - 1
            while num in list(numset.keys()) and numset[num] == 0:
                numset[num] = 1
                count += 1
                num -= 1

            result = max(result, count)

        return result

print(Solution().longestConsecutive([100,4,200,1,3,2]))