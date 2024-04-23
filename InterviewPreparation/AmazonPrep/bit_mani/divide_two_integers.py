def divide(dividend: int, divisor: int) -> int:
    sign = 1
    if (dividend >= 0 and divisor < 0): sign = -1
    if (dividend < 0 and divisor > 0): sign = -1 
    ans = 0
    n = abs(dividend)
    d = abs(divisor)
    while n >= d:
        cnt = 0
        while (n >= (d << (cnt + 1))):
            cnt += 1
        ans += 1 << cnt
        n -= (d << cnt)
    ans *= sign
    if ans > ((2 ** 31) - 1): return (2 ** 31) - 1
    if ans < -(2 ** 31): return -(2 ** 31)
    return ans


if __name__ == "__main__":
    print(divide(-2147483648, 1))