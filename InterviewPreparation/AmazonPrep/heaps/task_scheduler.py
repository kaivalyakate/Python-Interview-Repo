from collections import Counter, deque
from heapq import heappop, heappush, heapify


def least_interval(tasks: list[str], n: int) -> int:
    count = Counter(tasks)
    count = sorted(list(count.values()), reverse=True)

    chunk = count[0]-1
    idle = chunk * n

    for freq in count[1:]:
        idle -= min(chunk, freq)
    
    return idle + len(tasks) if idle >= 0 else len(tasks)


if __name__ == "__main__":
    print(least_interval(tasks=["A", "A", "A", "B", "B", "B"], n=2))