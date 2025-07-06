import collections
from typing import List

class solution():
    def max_sliding_Window(self, nums: List[int], k: int)->List[int]:
        l = r = 0
        q = collections.deque()
        output = []
        while r < len(nums):
            #Pop smaller values from queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #remove left val from q
            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                output.append(nums[q[0]])
                l += 1
            r +=1

        return output
    
    def Brute_max_sliding_Window(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return None
        
        result = []
        for i in range(len(nums) - k +1):
            window = nums[i:i+k]
            result.append(max(window))

        return result

def main():
    sol = solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k =3
    print(f"Max values in the sliding window: {sol.Brute_max_sliding_Window(nums, k)}")
    print(f"Max values in the sliding window usin deque: {sol.max_sliding_Window(nums, k)}")

if __name__ == "__main__":
    main()