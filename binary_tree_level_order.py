from typing import List
import collections
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val =val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level= []
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

def main():
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(17)
    print(f"Level order traversal {sol.levelOrder(root)}")

if __name__ == "__main__":
    main()
