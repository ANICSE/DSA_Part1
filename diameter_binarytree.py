class TreeNode:
    def __init__(self, data=None, left = None, right=None):
        self.data = data
        self.left = left
        self.right = right

def diameter_binary_tree(root):
    diameter = 0
    def find_height(node):
        nonlocal diameter
        if not node:
            return 0
        left_height = find_height(node.left)
        right_height = find_height(node.right)

        diameter = max(diameter, left_height + right_height)

        return 1 + max(left_height, right_height)
    find_height(root)
    return diameter
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def main():
    print("Length of binary Tree")
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, TreeNode(6), TreeNode(7))
    print(inorder(root))
    print(diameter_binary_tree(root))
if __name__ == "__main__":
    main()