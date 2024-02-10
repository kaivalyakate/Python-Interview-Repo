class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            elif char in (')', '}', ']'):
                element = stack.pop() if stack else '*'
                if char == ')' and element != '(':
                    return False
                elif char == '}' and element != '{':
                    return False
                elif char == ']' and element != '[':
                    return False
        return not stack

print(Solution().isValid("(){}"))