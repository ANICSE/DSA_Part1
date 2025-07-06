from typing import List
from collections import defaultdict

class Solution:
    def canCourse(self, numcourses: int, prerequisites: List[List[int]])->bool:
        #Building an prerequiste graph -> adjacency list
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        #initialize all nodes to 0
        visited = [0] * numcourses # 0 -> unvisited, 1 -> visted, -1 -> visiting

        def dfs(course):
            if visited[course] == -1: #cycle detected
                return False
            
            if visited[course] == 1:
                return True
            
            visited[course] = -1  #Mark as visiting

            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False

            visited[course] = 1
            return True

        for i in range(numcourses):
            if not dfs(i):
                return False
        
        return True
    
def main():
    sol = Solution()

    # ✅ Test Case 1: No cycle
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    print("Can finish courses (test 1)?", sol.canCourse(numCourses, prerequisites))
    # Output: True

    # ❌ Test Case 2: Cycle exists
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [0, 2]]
    print("Can finish courses (test 2)?", sol.canCourse(numCourses, prerequisites))
    # Output: False

if __name__ == "__main__":
    main()