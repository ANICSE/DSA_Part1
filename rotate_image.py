from typing import List
class Solution:
    def rotate_image(Self, matrix: List[List[int]])-> None:
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r -l):
                top, bottom =l, r

                #save topleft
                topleft = matrix[top][l+i]

                #move bottomleft to topleft
                matrix[top][l+i] = matrix[bottom-i][l]

                #move bottomright to bottomleft
                matrix[bottom-i][l] = matrix[bottom][r-i]

                #movetop right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                #move topleft to topright
                matrix[top+i][r] = topleft
            
            r -=1
            l +=1

def print_matrix(matrix: List[List[int]]):
    for row in matrix:
        print(row)

def main():
    sol = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    print_matrix(matrix)

    sol.rotate_image(matrix)

    print("\nRotated Matrix (90° Clockwise):")
    print_matrix(matrix)

if __name__ == "__main__":
    main()