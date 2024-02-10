from collections import deque
def police_thief(pos: list[str], k: int) -> int:
    p_q = deque([])
    t_q = deque([])
    i = 0
    count = 0
    while i < len(pos):
        if pos[i] == "P":
            if t_q and i - t_q[0] <= k:
                count += 1
                t_q.popleft()
            else:
                p_q.append(i)
            i += 1
        elif pos[i] == "T":
            if not p_q:
                t_q.append(i)
                i += 1
                continue
            while p_q and pos[i] == "T":
                if p_q[0] - i <= k:
                    count += 1
                    p_q.popleft()
                    i += 1
                else:
                    t_q.append(i)
    return count


if __name__ == "__main__":
    police_thief(pos=["P", "T", "T", "P", "T", "T", "P"], k=2)
    