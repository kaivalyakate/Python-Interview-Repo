def minWindow(s: str, t: str) -> int:
    have, need = 0, len(t)
    t_count, window = {}, {}
    for i in t:
        t_count[i] = t_count.get(i, 0) + 1
    
    l = 0
    res_len, res = [-1, -1], float("-inf")
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        
        if c in t_count.keys() and window[c] == t_count[c]:
            have += 1

        while have == need:
            if (r - l + 1) < res:
                res_len = [l, r]
                res = (r - l + 1)
            
            window[s[l]] -= 1
            if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                have -= 1
            l += 1
    l, r = res_len
    return s[l:r+1] if res != float("-inf") else ""