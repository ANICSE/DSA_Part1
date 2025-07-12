from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) ->List[List[int]]:
        RoWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or 
                r < 0 or c < 0 or r ==RoWS or c == COLS or
                heights[r][c] < prevHeight):
                return
            
            visit.add((r,c))
            #Enquiing and Running DFS on all the neighbors of [r,c]
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])  #for top row--> Pacific Ocean
            dfs(RoWS -1, c, atl, heights[RoWS-1][c])  #for bottom row Atlantic Ocean

        for r in range(RoWS):
            dfs(r, 0, pac, heights[r][0]) #for leftmost col--> Pacific Ocean
            dfs(r, COLS -1, atl, heights[r][COLS-1]) # for rightmst col -> Atlantic Ocean

        res =[]
        for r in range(RoWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
    
def main():
    sol = Solution()
    heights = [[1,2,2,3,5], [3,2,3,4,4], [2,4,5,3,1], [6,7,1,4,5], [5,1,1,2,4]]

    print(f"co-odrinates from where we can reach both pacific and atlabtic: {sol.pacificAtlantic(heights)}")

if __name__ == "__main__":
    main()