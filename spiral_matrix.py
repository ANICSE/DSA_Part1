from typing import List
class Solution:
    def SpiralOrder(self, matrix: List[List[int]])-> List[int]:
        res= []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            #get every i in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            #get every i in right col
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -=1
            if not (left < right and top < bottom):
                break

            #get every i in bottom row
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -=1

            #get every i in left col
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left +=1
        return res

def main():
    sol = Solution()
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    print("Spiral Order of matrix1:", sol.SpiralOrder(matrix1))
    print("Spiral Order of matrix2:", sol.SpiralOrder(matrix2))

if __name__ == "__main__":
    main()