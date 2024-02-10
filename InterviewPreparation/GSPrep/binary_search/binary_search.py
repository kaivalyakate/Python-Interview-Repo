def binary_search(nums: list[int], target: int):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (end + start) // 2
        if target == nums[mid]: return mid
        if target < nums[mid]: end = mid - 1
        if target > nums[mid]: start = mid + 1
    return -1


if __name__ == "__main__":
    binary_search([-1,0,3], target=3)