def character_replacement(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0 
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxf = max(maxf, count[s[r]])
        while (r - l + 1) - maxf > k:
            l += 1
            count[s[l]] -= 1
        
        res = max(res, r - l + 1)
    return res


if __name__ == "__main__":
    s = "ABABBA"
    k = 2
    character_replacement(s=s, k=k)