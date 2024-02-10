import math
def gas_station(gas: list[int], cost: list[int]) -> int:
    max_gas_cost_ratio = -math.inf
    start = 0
    for i in range(0, len(gas)):
        ratio = gas[i] / cost[i]
        if ratio > max_gas_cost_ratio:
            max_gas_cost_ratio, start = ratio, i
    
    i = (start + 1) % len(gas)
    curr_gas, curr_cost = gas[start], cost[start]
    while curr_gas > 0:
        if i == start:
            return start
        curr_gas = curr_gas - curr_cost
        if curr_gas <= 0:
            return -1
        curr_gas += gas[i]
        curr_cost = cost[i]
        i = (i + 1) % len(gas)
    return -1


if __name__ == "__main__":
    gas = [5,8,2,8]
    cost = [6,5,6,6]
    print(gas_station(gas, cost))