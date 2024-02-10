class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        filtered_str = ""
        for i in s:
            if i.isalnum():
                filtered_str += i.lower()
        if filtered_str[::-1] == filtered_str:
            return True
        return False

print(Solution().isPalindrome(" "))