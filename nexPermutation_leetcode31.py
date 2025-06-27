from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n =len(nums)
        i = n-2
        #find the Pivot
        while i >= 0 and nums[i] >= nums[i+1]:
            i-= 1

        #Find the successor
        if i >= 0:
            j = n-1
            while j > i and nums[i] >= nums[j]:
                j-= 1
            nums[i], nums[j] = nums[j], nums[i]

        #Reverse the list
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1

def main():
    sol =Solution()
    #nums = [1, 3, 5, 4, 3, 2, 1]
    nums = [5,1,1]
    sol.nextPermutation(nums)
    print(f"The next permutation is {nums}")

if __name__ == "__main__":
    main()
