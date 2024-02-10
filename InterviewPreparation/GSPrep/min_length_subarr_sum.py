def minLength(arr: list[int], target: int) -> int:
    i, start = 0, 0
    min_len = float("inf")
    curr_sum = 0
    while i < len(arr):
        curr_sum += arr[i]
        while curr_sum >= target:
            min_len = min(min_len, i - start + 1)
            curr_sum -= arr[start]
            start += 1
        i += 1
    return min_len


minLength(arr=[1,2,3,4], target=6)