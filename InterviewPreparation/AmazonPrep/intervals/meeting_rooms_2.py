def minMeetingRooms(intervals: list[list[int]]) -> int:
    ans = 0
    intervals = sorted(intervals, key = lambda interval: interval[1])
    
    return -1