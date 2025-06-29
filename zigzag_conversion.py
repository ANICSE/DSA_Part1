class Solution:
    def zigzag(self, s: str, numRows: int)->str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows =[' '] * numRows
        going_down = False
        curr_row = 0

        for char in s:
            rows[curr_row] += char

            if curr_row == 0 or curr_row == numRows -1:
                going_down = not going_down
            if going_down:
                curr_row += 1
            else:
                curr_row -= 1

        return ''.join(rows)
    
def main():
    sol = Solution()
    s = "PAYPALISHIRING"
    print(sol.zigzag(s, numRows=3))

if __name__ == "__main__":
    main()