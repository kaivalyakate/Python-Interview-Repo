from heapq import heappop, heappush

def findKthLargest(nums: list[int], k: int) -> int:
    if not nums:
        return -1
    pq = []
    for i in range(k):
        heappush(pq, nums[i])

    for i in range(k, len(nums)):
        while len(pq) > k:
            heappop(pq)

        curr = nums[i]
        if curr > pq[0]:
            heappop(pq)
            heappush(pq, nums[i])

    return heappop(pq)


if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    pq = []
    findKthLargest(nums=nums, k=4)