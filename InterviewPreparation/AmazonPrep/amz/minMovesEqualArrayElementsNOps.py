import sys
def minMoves(nums: list[int]) -> int:
    min_num = sys.maxsize
    for i in nums:
        min_num = min(min_num, i)
    moves = 0
    for i in nums:
        moves += i - min_num
    return moves