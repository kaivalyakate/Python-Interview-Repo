def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    def backtrack(element_index: int, combination: list[int], curr_sum: int):
        if curr_sum > target:
            return None
        if curr_sum == target:
            result.append(combination.copy())
            return combination
        for i in range(element_index, len(candidates)):
            combination.append(candidates[i])
            backtrack(i, combination=combination, curr_sum=curr_sum+candidates[i])
            combination.pop()
    result = []
    backtrack(0, [], 0)
    return result


if __name__ == "__main__":
    result = combinationSum(candidates=[2,3,6,7], target=7)
    print(result)