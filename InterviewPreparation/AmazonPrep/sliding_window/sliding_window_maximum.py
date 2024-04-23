from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    dq = deque()
    ans = []
    for i in range(k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)

    ans.append(nums[dq[0]])

    for i in range(k, len(nums)):
        if dq and dq[0] == i-k:
            dq.popleft()
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        
        dq.append(i)
        ans.append(nums[dq[0]])
    return ans


def minSlidingWindow(nums: list[int], k: int) -> list[int]:
    dq = deque()
    ans = []
    for i in range(k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)

    ans.append(nums[dq[0]])

    for i in range(k, len(nums)):
        if dq and dq[0] == i-k:
            dq.popleft()
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        
        dq.append(i)
        ans.append(nums[dq[0]])
    return ans


if __name__ == "__main__":
    print(maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3))