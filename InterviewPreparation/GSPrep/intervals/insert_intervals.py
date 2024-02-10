def insert_interval(intervals: list[list[int]], newInterval: list[int]) -> list[int]:
    if not intervals: return [newInterval]
    i = 0
    merged = []
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        merged.append(intervals[i])
        i += 1
    
    if i == len(intervals): 
        merged.append(newInterval)
        return merged
    
    if intervals[i][0] > newInterval[1]:
        merged.append(newInterval)
    elif intervals[i][1] >= newInterval[0]:
        merged.append([min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])])

    for j in range(i, len(intervals)):
        current = intervals[j]
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            merged[-1][1] = max(merged[-1][1], current[1])
    
    return merged


if __name__ == "__main__":
    intervals = [[1,5]]
    print(insert_interval(intervals=intervals, newInterval=[2,3]))