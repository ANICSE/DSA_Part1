from typing import List
class Solution:
    def findpeak(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1

        while l < r:
            m = l + ((r - l) // 2)
            if m > 0 and arr[m] < arr[m-1]:
                r = m-1
            elif m < len(arr)-1 and arr[m] < arr[m+1]:
                l = m+1
            else:
                return m

    def findpeakoptim(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1

        while l < r:
            m = l + ((r-l)//2)
            if arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m
        return l
def main():
    sol= Solution()
    arr = [1, 2, 3, 1]
    print(f"the peak element in the array {arr} is: {sol.findpeak(arr)}")

    arr1 = [1]
    print(f"the peak element in the array {arr1} is: {sol.findpeakoptim(arr1)}")
    
if __name__ == "__main__":
    main()