from typing import List
class solution:
    def completecircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, S = len(gas), 0, 0, 0

        for i in range(n):
            total_surplus+= gas[i] -cost[i]
            surplus+= gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                S = i+1
        if total_surplus < 0:
            return -1
        else:
            return S

def main():
    sol = solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(f"can complete from position {sol.completecircuit(gas, cost)}")

if __name__ =="__main__":
    main()