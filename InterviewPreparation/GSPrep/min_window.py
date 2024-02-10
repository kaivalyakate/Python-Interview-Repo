def min_window(s: str, t:  str) -> str:
    window, count_t = {}, {}
    for c in t:
        count_t[c] = 1 + count_t.get(c, 0)
    
    have, need = 0, len(count_t)
    res, res_len = [-1, -1], float("inf")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        if c in count_t and window[c] == count_t[c]:
            have += 1
        
        while have == need:
            if (r - l + 1) < res_len:
                res_len = (r - l + 1)
                res = [l, r]
            
            window[s[l]] -= 1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    min_window(s=s, t=t)