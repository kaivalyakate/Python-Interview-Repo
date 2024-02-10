from dataclasses import dataclass
from heapq import heappop, heappush


def least_interval(tasks: list[str], n: int) -> int:
    @dataclass
    class Task:
        name: int 
        count: int

        def __lt__(self, obj):
            return self.count < obj.count
    
    if not tasks: return 0
    q: list[Task] = []
    count_map = {}
    for i in tasks:
        count_map[i] = count_map.get(i, 0) + 1
    # Build a Heap of items containing (task.name, task.count)
    for k, v in count_map.items():
        heappush(q, Task(k, -v))
    
    time = 0
    while q:
        task = heappop(q)
        name, count = task.name, -task.count
        if count < 1:
            continue
        cooldown = 0

        temp_queue: list[Task] = []
        while q:
            next_task = heappop(q)
            task_name, task_count = next_task.name, -next_task.count
            if task_count < 1:
                continue
            heappush(temp_queue, Task(task_name, -(task_count - 1)))
            cooldown += 1

        heappush(q, Task(name, -(count - 1)))
        for i in temp_queue:
            heappush(q, i)
        if cooldown < n :
            cooldown += (n - cooldown)
        time += cooldown

    return time


if __name__ == "__main__":
    print(least_interval(tasks=["A", "A", "A", "B", "B", "B"], n=2))