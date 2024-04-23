def rodCut(length: int, prices: list[int]) -> int:
    revenue = [float("-inf")] * (length + 1)
    revenue[0] = 0
    for j in range(1, length+1):
        for i in range(1, j+1):
            revenue[j] = max(revenue[j], prices[i - 1] + revenue[j - i])
    return revenue[length]


if __name__ == "__main__":
    print(rodCut(length=10, prices=[1,5,8,9,10,17,17,20,24,30]))