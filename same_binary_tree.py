from collections import deque
class TreeNode:
    def __init__(self, data= None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def is_same_tree_BFS(root1, root2):
    queue1 = deque([root1])
    
    queue2 = deque([root2])

    while queue1 and queue2:
        node1 = queue1.popleft()
        node2 = queue2.popleft()

        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.data != node2.data:
            return False
        
        queue1.append(node1.left)
        queue1.append(node1.right)
        queue2.append(node2.left)
        queue2.append(node2.right)

    # Both queues should be empty at the end
    return not queue1 and not queue2
        
def recursively(root1, root2):
    #case 1: when both trees are null
    if not root1 and not root2:
        return True
    #case 2: When one of the tree is empty
    if not root1 or not root2:
        return False
    #case 3: When both roots are different
    if root1.data != root2.data:
        return False
    return recursively(root1.left, root2.left) and recursively(root1.right, root2.right)
def main():
    print("Same binary Tree")
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))

    root3 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6))
    root4 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8) ))
    print(recursively(root1, root2))
    print(recursively(root3, root4))

    print(f"Using BFS: {is_same_tree_BFS(root1, root2)}")
    # Double Queue Utility
    # dq = deque([1,2,3,4])
    # dq.append(5)    #Append to right end [1,2,3,4,5]
    # dq.appendleft(0) #Append to left end [0,1,2,3,4,5]
    # dq.pop()           #Remove from right: returns 5
    # dq.popleft()        #Remove from left: reurn 0



if __name__ == "__main__":
    main()