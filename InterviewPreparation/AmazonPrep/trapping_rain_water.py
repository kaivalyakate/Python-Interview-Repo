def trap(height: list[int]) -> int:
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    leftMax, rightMax = height[left], height[right]
    res = 0

    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, height[left])
            res += leftMax - height[left]
        else:
            right -= 1
            rightMax = max(rightMax, height[right])
            res += rightMax - height[right]
    
    return res


if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]