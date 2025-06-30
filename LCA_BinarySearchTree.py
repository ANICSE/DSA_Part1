class TreeNode:
    def __init__(self, root = 0, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right
class Solution:
    def LCA_BST(self, root: TreeNode, p: TreeNode, q: TreeNode)->TreeNode:
        curr = root

        while curr:
            if p.root > curr.root and q.root > curr.root:
                curr = curr.right
            elif p.root < curr.root and q.root < curr.root:
                curr = curr.left
            else:
                return curr


def main():
    sol = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    
    p = root.right.left        # Node with value 5
    q = root.right.right        # Node with value 1

    lca = sol.LCA_BST(root, p, q)
    print(f"LCA of the given tree is {lca.root if lca else None}")

if __name__ =="__main__":
    main()