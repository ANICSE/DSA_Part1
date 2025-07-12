class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isValidBST(self, root: TreeNode)-> bool:

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
    
        return valid(root, float("-inf"), float("+inf"))
    
def main():
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(8)

    print(f"valid BST ? {sol.isValidBST(root)}")

if __name__ == "__main__":
    main()
        