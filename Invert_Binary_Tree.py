class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def invert(self, root: TreeNode)-> TreeNode:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invert(root.left)
        self.invert(root.right)

        return root
    
def main():
    sol = Solution()
    root  = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print(f"Inverted tree is: {sol.invert(root)}")

if __name__ == "__main__":
    main()
