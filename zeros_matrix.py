from typing import List
class Solution:
    def zeros(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        rows_zero = set()
        cols_zero = set()

        #first parse: Traverse
        for i in range(rows):
            for j in range (cols):
                if matrix[i][j]==0:
                    rows_zero.add(i)
                    cols_zero.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in rows_zero or j in cols_zero:
                    matrix[i][j] = 0
        
def main():
    sol=Solution()
    matrix = [[1, 2, 1], [0, 1, 0], [2, 3, 4]]
    print(matrix)
    sol.zeros(matrix)
    print(matrix)

if __name__ == "__main__":
    main()
