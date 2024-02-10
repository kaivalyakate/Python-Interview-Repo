from heapq import heappush, heappop

class Pair:

    def __init__(self, time, dest) -> None:
        self.time = time
        self.dest = dest

    def __lt__(self, obj):
        return self.time < obj.time
    

def djikstra(adj_list: dict[int, list[Pair]], signal_received_at: list[int], source: int, n: int):
    q = [Pair(0, source)]

    signal_received_at[source] = 0
    while q:
        current = heappop(q)

        if current.time > signal_received_at[current.dest]:
            continue

        if not adj_list.get(current.dest, False):
            continue
        
        for neighbour in adj_list.get(current.dest):
            if signal_received_at[neighbour.dest] > current.time + neighbour.time:
                signal_received_at[neighbour.dest] = current.time + neighbour.time
                heappush(q, neighbour)


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    adj_list: dict[int, list[Pair]] = {}
    signal_received_at = [float("inf") for _ in range(n+1)]
    for node_info in times:
        source, dest, time = node_info[0], node_info[1], node_info[2]
        if source not in adj_list:
            adj_list[source] = [Pair(time, dest)]
        else:
            neighbours = adj_list.get(source)
            neighbours.append(Pair(time, dest))
            adj_list[source] = neighbours
    
    djikstra(adj_list, signal_received_at, k, n)

    min_time = float("-inf")
    for i in range(1, n+1):
       min_time = max(min_time, signal_received_at[i])

    return -1 if min_time == float("inf") else min_time


if __name__ == "__main__":
    times = [[1,2,1]]
    print(networkDelayTime(times, 2, 2))