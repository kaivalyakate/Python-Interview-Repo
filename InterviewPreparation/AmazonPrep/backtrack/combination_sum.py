def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    candidates.sort()
    def backtrack(element_index: int, combination: list[int], curr_sum: int):
        nonlocal result
        if curr_sum > target:
            return None
        if curr_sum == target:
            result.append(combination.copy())
            return combination
        prev = -1
        for i in range(element_index, len(candidates)):
            if candidates[i] == prev:
                continue
            curr_combination = combination + [candidates[i]]
            backtrack(i+1, combination=curr_combination, curr_sum=curr_sum+candidates[i])
            prev = candidates[i]
    backtrack(0, [], 0)
    return result


if __name__ == "__main__":
    result = combinationSum(candidates=[10,1,2,7,6,1,5], target=8)
    print(result)