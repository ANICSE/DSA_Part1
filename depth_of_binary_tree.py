class TreeNode:
    def __init__(self, val = 0, left =None, right = None):
        self.val =val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: TreeNode)->int:
        if not root:
            return 0
        
        return 1 + max(self.dfs(root.left), self.dfs(root.right))
    
def main():
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(f"Maximum depth is: {sol.dfs(root)}")

if __name__ =="__main__":
    main()