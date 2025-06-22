from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            n =abs(n)
            if nums[n-1] > 0: 
                nums[n-1] *= -1
            else:
                result.append(n)
        return result

    def find_Duplicates_hash(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = set()

        for n in nums:
            if n in seen:
                duplicates.add(n)
            else:
                seen.add(n)
        return duplicates
    
def main():
    sol = Solution()
    A = [4, 3, 2, 1, 4, 2, 3, 1]
    print(f"The duplicate entrie are: {sol.findDuplicates(A)}")
    B = [4, 3, 2, 1, 4, 2, 3, 1]
    print(f"The duplicate entrie using HashSet are: {sol.findDuplicates(B)}")

if __name__ =="__main__":
    main()