from typing import List
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int])-> TreeNode:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) #first value of preorder is alwasys the root
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
    
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.val, end=" ")
        print_inorder(node.right)

def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    sol = Solution()
    root = sol.buildTree(preorder, inorder)

    print("Inorder traversal of the constructed tree:")
    print_inorder(root)  # Should print: 9 3 15 20 7

if __name__ == "__main__":
    main()