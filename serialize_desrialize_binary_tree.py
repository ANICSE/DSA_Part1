class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right =None
    
class Solution:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
    
    def deserialize(self, data):
        vals = data.split(",")

        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i +=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i +=1
            node.left =dfs()
            node.right = dfs()
            return node
        return dfs()
    
def print_in_order(node):
    if not node:
        return
    print_in_order(node.left)
    print(node.val, end=" ")
    print_in_order(node.right)

def main():
    # Construct a binary tree manually:
    #      1
    #     / \
    #    2   3
    #       / \
    #      4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    sol = Solution()

    # Serialize
    serialized = sol.serialize(root)
    print("Serialized Tree:", serialized)

    # Deserialize
    deserialized_root = sol.deserialize(serialized)
    print("In-order Traversal of Deserialized Tree:", end=" ")
    print_in_order(deserialized_root)
    print()

if __name__ == "__main__":
    main()
