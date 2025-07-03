import random
import bisect
from typing import List
class Solution:
    def __init__(self, w: List[int]) -> int:
        self.prefix_nums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_nums.append(total)
        self.total = total
    
    def pickIndex(self)-> int:
        r = random.randint(1, self.total)
        index = bisect.bisect_left(self.prefix_nums, r)
        return index
    
def main():
    
    w = [1,3]
    sol = Solution(w)

    for _ in range(10):
        print(sol.pickIndex())
    # Step 1: Create the object with weights
    # obj = Solution([1, 3])

    # # Step 2: Call pickIndex multiple times
    # print(obj.pickIndex())
    # print(obj.pickIndex())
    # print(obj.pickIndex())
    # print(obj.pickIndex())
    # print(obj.pickIndex())

if __name__ == "__main__":
    main()

