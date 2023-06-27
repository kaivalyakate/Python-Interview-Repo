from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = dict()
        for s in strs:
            anagram = ''.join(i for i in sorted(s))
            anagrams = a_map.get(anagram, None)
            if anagrams:
                anagrams.append(s)
            else:
                a_map[anagram] = [s]
        return list(a_map.values())


print(Solution().groupAnagrams(["a"]))
print("Hello")
print("h3")
print("h1")