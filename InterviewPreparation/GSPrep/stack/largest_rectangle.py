def largestRectangle(heights: list[int]) -> int:
    stack = [-1]
    max_area = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    return max_area


if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    largestRectangle(heights=heights)