def knapsack(weights: list[int], values: list[int]) -> int:
    max_weight = 10
    dp = [0 for i in range(max_weight+1)]

    for i in range(1, len(values)+1):
        for j in range(max_weight, weights[i-1], -1):
            


if __name__ == "__main__":
    weights = [4,3,7,2]
    vals = [60,90,40,10]
    max_val = knapsack(weights=weights, values=vals)
    print(max_val)