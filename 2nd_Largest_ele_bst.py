#Approach 1: Parent/left subtree
# time complexity: O(h)
# Space Complexity: o(1)
# Doest not generalize to k-th largest element (drawback)

class TreeNode:
    def __init__(self, data= None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left
def find_second_larget(root):
    if not root or (not root.left and not root.right):
        return None # Empty tree or has one node
    
    parent = None
    node = root

    while node.right:
        parent = node
        node = node.right

    #Case 1: Largest node has a left subtree
    if node.left:
        node =node.left
        while node.right:
            node = node.right
        return node.data
    
    #Case2: Largets node has no left subtree
    return parent.data if parent else None
def find_second_largest_inorder(root):
    def reverse_inorder(node):
        nonlocal count, result
        if node and count < 5:
            reverse_inorder(node.right)
            count+= 1
            if count == 5:
                result = node.data
                print(f"{count}th largest number is {result}")
                return
            reverse_inorder(node.left)
    count = 0 
    result = None
    reverse_inorder(root)
    return result

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
def revinorder(root, result):
    if root:
        revinorder(root.right, result)
        result.append(root.data)
        print(root.data, end=' ')
        revinorder(root.left, result)

def main():
    print("Binary Search Tree")
    # root = TreeNode(5)
    # root.left = TreeNode(3)
    # root.right = TreeNode(8, TreeNode(7), TreeNode(10, TreeNode(9)))
    # root = TreeNode(9)
    # root.left = TreeNode(7, TreeNode(6), TreeNode(8))
    # root.right = TreeNode(11, TreeNode(10), TreeNode(12))
    # root = TreeNode(8)
    # root.left = TreeNode(7, TreeNode(5))
    # root.left.left.right = TreeNode(6)
    # root.right = TreeNode(11, TreeNode(9), TreeNode(10))
    result = []
    root = TreeNode(16)
    root.left = TreeNode(10)
    root.left.left = TreeNode(8)
    root.right = TreeNode(20, TreeNode(18, TreeNode(17), TreeNode(19)), TreeNode(24))
    inorder(root)
    
    print("Reverse Inorder Traversal")
    print(revinorder(root, result))
    tree_size = len(result)
    print("tree size", tree_size)
    print(find_second_largest_inorder(root))

if __name__ == "__main__":
    main() 