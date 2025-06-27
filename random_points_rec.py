import random
import bisect
from typing import List

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0
        for x1, y1, x2, y2 in rects:
            area = (x2 - x1 + 1) * (y2 - y1 +1)
            total+= area
            self.prefix.append(total)
        self.total = total
    
    def pick(self) -> List[int]:
        rand_val = random.randint(0, self.total - 1)
        idx = bisect.bisect_right(self.prefix, rand_val)
        x1, y1, x2, y2 = self.rects[idx]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]
    
def main():
    rects = [
        [1, 1, 2, 2],
        [3, 3, 4, 4]
    ]
    sol = Solution(rects)
    print("Random points picked from rectangles:")
    for _ in range(20):
        print(sol.pick())
    
if __name__ == "__main__":
    main()