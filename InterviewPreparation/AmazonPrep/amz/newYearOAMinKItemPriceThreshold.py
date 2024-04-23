from heapq import heappush, heappop

def reduceGifts(prices: list[int], k: int, threshold: int) -> int:
    if len(prices) < k:
        return -1
    min_items = -1
    pq = []
    running_sum = 0
    for price in prices:
        if len(pq) >= k:
            if running_sum > threshold:
                min_items += 1
            running_sum -= heappop(pq)
        running_sum += price
        heappush(pq, price)
    if running_sum > threshold:
        min_items += 1
    return min_items


if __name__ == "__main__":
    prices = [3,2,1,4,6,5]
    k = 3
    threshold = 14
    print(reduceGifts(prices, k=k, threshold=threshold))