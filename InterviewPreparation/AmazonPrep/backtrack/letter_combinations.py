def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    key_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
               "7": "pqrs", "8": "tuv", "9": "wxyz"}
    ans = []
    def helper(idx: int, curr: str):
        nonlocal ans
        if idx >= len(digits):
            return
        
        letters = key_map[digits[idx]]
        for i in letters:
            if len(curr + i) == len(digits):
                ans.append(curr + i)
            helper(idx + 1, curr + i)
    
    helper(0, "")
    return ans


if __name__ == "__main__":
    ans =letterCombinations(digits="23")
    print(ans)