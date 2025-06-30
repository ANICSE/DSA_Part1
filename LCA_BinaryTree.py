class TreeNode:
    def __init__(self, val = 0, left = None, right =None):
        self.root = val
        self.left = left
        self.right = right

class Solution:   
    def LCA_Binary_Tree(self, root: TreeNode, p: TreeNode, q: TreeNode)->TreeNode:
        if not root:
            return None
        
        if root == p or root == q:
            return root

        left_lca = self.LCA_Binary_Tree(root.left, p, q)
        right_lca = self.LCA_Binary_Tree(root.right, p, q)

        if left_lca and right_lca:
            return root
        
        if left_lca:
            return left_lca
        else:
            return right_lca

def main():
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    
    p = root.left.right.left        # Node with value 5
    q = root.left.right.right        # Node with value 1

    lca = sol.LCA_Binary_Tree(root, p, q)
    print(f"LCA of the given tree is {lca.root if lca else None}")

if __name__ =="__main__":
    main()