def merge(intevals: list[list[int]]) -> list[list[int]]:
    if not intervals or len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda interval: interval[0])
    i = 1
    merged = [intervals[0]]
    prev = merged[0]
    while i < len(intervals):
        current = intervals[i]
        if prev[1] >= current[0] and current[1] > prev[1]:
            prev[1] = current[1]
        elif prev[1] < current[0]:
            prev = current
            merged.append(current)
        i += 1
    return merged


if __name__ == "__main__":
    intervals = [[1,4],[0,1]]
    print(merge(intevals=intervals))