from typing import List
import heapq

def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals.sort()
    min_heap = []
    res, i = {}, 0
    for q in sorted(queries):
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            heapq.heappush(min_heap, (r - l + 1, r))
            i += 1

        while min_heap and min_heap[0][1] < q:
            heapq.heappop(min_heap)
        res[q] = min_heap[0][0] if min_heap else -1

    return [res[q] for q in queries]


if __name__ == "__main__":
    intervals = [[2,3],[2,5],[1,8],[20,25]]
    queries = [2,19,5,22]
    print(minInterval(intervals=intervals, queries=queries))