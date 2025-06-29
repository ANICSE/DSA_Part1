from typing import List, Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasSumPath(self, root: Optional[TreeNode], target_sum: int)-> bool:
        def dfs(node, curr_sum):
            if not node:
                return False
            curr_sum += node.val
            if not node.left and not node.right: #ensures its a leaf node
                return curr_sum == target_sum
            
            return (dfs(node.left, curr_sum) or dfs(node.right, curr_sum))
        return dfs(root, 0)
    
def main():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    sol = Solution()
    target_sum = 18
    print("Has path sum 26?", sol.hasSumPath(root, target_sum))  # Output: True

if __name__ == "__main__":
    main()
