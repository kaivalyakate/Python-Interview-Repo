from heapq import heappush, heappop

def find_median_sorted_arr(nums1: list[int], nums2: list[int]) -> float:
    heap = []
    m, n = len(nums1), len(nums2)
    median_count = 