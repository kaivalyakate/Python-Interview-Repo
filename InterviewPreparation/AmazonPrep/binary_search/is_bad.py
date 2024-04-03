def first_bad(n: int) -> int:
    start, end = 1, n
    while start < end:
        mid = (start + end) // 2
        if not isBad(mid) and isBad(mid+1):
            return mid + 1
        elif not isBad(mid):
            start = mid + 1
        else:
            end = mid
    return start

def isBad(n: int) -> bool:
    if n == 4:
        return True
    return False


if __name__ == "__main__":
    first_bad(5)