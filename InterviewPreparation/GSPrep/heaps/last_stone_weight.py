from heapq import heappop, heappush

def last_stone_weight(stones: list[int]) -> int:
    if not stones: return 0
    q = []
    for i in stones:
        heappush(q, -i)
    
    while len(q) >= 2:
        max_one: int = -heappop(q)
        max_two: int = -heappop(q)

        if max_one != max_two:
            heappush(q, -(max_one - max_two))
    
    return -heappop(q) if q else 0


if __name__ == "__main__":
    print(last_stone_weight(stones=[1]))