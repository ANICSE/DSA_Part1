from typing import List
class Solution:
    def topk(self, nums: List, k: int)->List[int]:
        count = {}
        freq = [ [] for i in range(len(nums)+ 1) ]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)

        res =[]
        for i in range(len(freq)-1, 0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
def main():
    sol = Solution()
    nums = [1,1,1,2,2,3,4]
    k=2
    print(f"{k} most frequent elemnt in {nums} is: {sol.topk(nums,k)}")

if __name__ == "__main__":
    main()
