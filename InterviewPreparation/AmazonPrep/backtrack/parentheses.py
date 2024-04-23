def generateParenthese(n: int) -> list[str]:
    if n < 1:
        return [] 
    
    ans = []
    def helper(open: int, close: int, curr: str):
        if open == close and len(curr) == n * 2:
            ans.append(curr)
            return
        
        if open < n:
            helper(open + 1, close, curr + "(")
        
        if open > close and close < n:
            helper(open, close + 1, curr + ")")
        
    helper(0, 0, "")
    return ans


if __name__ == "__main__":
    print(generateParenthese(3))