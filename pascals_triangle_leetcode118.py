from typing import List
class Solution:
    def pascals(self, numRows: int) -> List[List[int]]:

        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
    
def main():
    sol = Solution()
    numRows = 5
    print(f"Pascals traingle for {numRows} of rows is: {sol.pascals(numRows)}")

if __name__ == "__main__":
    main()

