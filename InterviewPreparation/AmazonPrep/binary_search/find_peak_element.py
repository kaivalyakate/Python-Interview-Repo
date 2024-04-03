def peak_element(nums: list[int]) -> int:
    start, end = 0, len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > nums[mid+1]:
            end = mid
        else:
            start = mid + 1
    return start


if __name__ == "__main__":
    peak_element(nums=[1, 2, 3])