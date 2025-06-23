from typing import List
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root ==None:
            return result
        cache = {}
        self.minC, self.maxC = 0, 0

        def dfs(node, r, c):
            if node == None:
                return
            if c in cache: 
                cache[c].append([r, node.data])
            else:
                cache[c] = [[r, node.data]]
            self.minC = min(self.minC, c)
            self.maxC = max(self.maxC, c)
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
        
        dfs(root, 0,0)

        for c in range(self.minC, self.maxC+1):
            col = sorted(cache[c], key = lambda x: (x[0], x[1]))
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            result.append(col_sorted)
        return result

def main():
    # Build the sample tree: [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol =Solution()
    result = sol.verticalTraversal(root)
    print("Vertical order traversal:")
    for col in result:
        print(col)

if __name__ == "__main__":
    main()