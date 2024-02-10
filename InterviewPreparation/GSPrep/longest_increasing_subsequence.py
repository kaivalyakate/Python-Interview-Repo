def lis(nums: list[int]) -> int:
    if not nums:
        return 0
    
    sub = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > sub[-1]:
            sub.append(nums[i])
        else:
            j = 0
            while nums[i] > sub[j]:
                j += 1

            sub[j] = nums[i]
        
    return len(sub)


if __name__ == "__main__":
    lis(nums=[10,9,2,5,3,7,101,18])