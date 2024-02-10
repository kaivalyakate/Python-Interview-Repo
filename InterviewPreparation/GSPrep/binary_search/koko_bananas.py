import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    if not piles or h < 1: return h
    start, end = 1, max(piles)
    while start < end:
        mid = (start + end) // 2
        temp_hours = 0
        for pile in piles:
            temp_hours += math.ceil(pile/mid)
        if temp_hours <= h:
            end = mid 
        else:
            start = mid + 1
    return end


if __name__ == "__main__":
    piles = [312884470]
    print(minEatingSpeed(piles=piles, h=312884469))