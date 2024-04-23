def longestValidSubstring(word: str, forbidden: list[str]) -> int:
    curr_right = len(word) - 1
    ans = 0 
    seen = set(forbidden)
    for left in range(len(word) - 1, -1, -1):
        for right in range(left, min(curr_right, left + 10) + 1):
            if word[left:right+1] in seen:
                curr_right = right - 1
        ans = max(ans, curr_right - left + 1)
    return ans


if __name__ == "__main__":
    print(longestValidSubstring(word="cbaaaabc", forbidden=["aaa", "cb"]))