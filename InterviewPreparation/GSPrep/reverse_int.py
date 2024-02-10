def reverse(x: int) -> int:
    is_negative = True if x < 0 else False
    num = 0
    if is_negative: x = -x
    while x > 0:
        right = x % 10
        num = ((num * 10) + right)
        if num >= ((2**31) - 1):
            return 0
        x //= 10
    return num if not is_negative else -num


if __name__ == "__main__":
    print(reverse(-123))