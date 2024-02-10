import sys
def find_second_smallest_element(nums: list[int]):
    if len(nums) < 2: return 0
    first, second = sys.maxsize, sys.maxsize
    for i in nums:
        if i < first:
            second = first
            first = i
        elif i < second:
            second = i
    return second

if __name__ == "__main__":
    print(find_second_smallest_element(nums=[2,3,1,1,3,4,2]))