from collections import Counter
from heapq import heappush, heappop


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


def topKFrequent(words: list[str], k: int) -> list[str]:
    cnt = Counter(words)
    h = []
    for word, freq in cnt.items(): # -> O(N)
        heappush(h, Pair(word, freq)) # -> O(log N) (Push + Heapify Process)
        if len(h) > k:
            heappop(h) # -> O(1)
    return [p.word for p in sorted(h, reverse=True)] 
    

if __name__ == "__main__":
    print(topKFrequent(words=["i", "love", "i", "leetcode", "love"], k=2))