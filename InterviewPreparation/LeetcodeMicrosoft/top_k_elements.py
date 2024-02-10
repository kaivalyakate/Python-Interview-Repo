from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        num_count = {}
        for i in nums:
            num_count[i] = num_count.get(i, 0) + 1

        for i in num_count.keys():
            heapq.heappush(h, (num_count.get(i), i))

        k = len(num_count) - k
        while k > 0:
            heapq.heappop(h)
            k -= 1

        return [i[1] for i in h]


print(Solution().topKFrequent([0], 1))