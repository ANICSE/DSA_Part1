from typing import List

class Solution:
    def DFS_Island(self, islands: List[List[str]])-> int:
        if not islands:
            return
        row, col = len(islands), len(islands[0])
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or islands[r][c] == '0':
                return            
            islands[r][c] = '0'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(row):
            for c in range(col):
                if islands[r][c] == '1':
                    dfs(r,c)
                    count += 1            

        return count
    
def main():
    sol = Solution()
    island = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    print("Number of island possible", sol.DFS_Island(island))

if __name__ =="__main__":
    main()