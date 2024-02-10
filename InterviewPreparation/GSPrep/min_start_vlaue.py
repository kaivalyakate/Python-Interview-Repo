def min_start_value(arr: list[int]) -> int:
    x = 0
    running_sum = x
    for i in arr:
        running_sum += i
        if running_sum < 0:
            x += 1 - running_sum
            running_sum += x

    return x

if __name__ == "__main__":
    print(min_start_value(arr = [-4, 3, -7, 1]))