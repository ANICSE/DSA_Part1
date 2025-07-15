class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeBinaryTree(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        
        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0
        root = TreeNode(v1+v2)

        root.left = self.mergeBinaryTree(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeBinaryTree(t1.right if t1 else None, t2.right if t2 else None)

        return root
    
def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=" ")
    print_inorder(node.right)

def main():
    # Tree 1
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    # Tree 2
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    sol = Solution()
    merged = sol.mergeBinaryTree(t1, t2)

    print("Inorder traversal of merged tree:")
    print_inorder(merged)

if __name__ == "__main__":
    main()