from sortedcontainers import SortedList
import random

def kthMinimumInArray(nums: list[int], k: int, m: int) -> list[int]:
    window = SortedList(nums[:m])
    ans = []
    ans.append(window[k-1])
    for i in range(m, len(nums)):
        window.remove(nums[i - m])
        window.add(nums[i])
        ans.append(window[k - 1])
    return ans

if __name__ == "__main__":
    
    kthMinimumInArray(nums=[1,3,2,1], k=2, m=3)