from heapq import heappop, heappush
from collections import Counter

def minimumKeypresses(s: str) -> int:
    c = Counter(s)
    ans = cnt = 0
    for i, freq in enumerate(sorted(c.values(), reverse=True)):  # sort reversely
        if i % 9 == 0:
            cnt += 1
        ans += cnt * freq                                        # add `num_of_time_to_press_the_key * frequency` to result
    return ans


if __name__ == "__main__":
    print(minimumKeypresses(s="abcdefghijkl"))