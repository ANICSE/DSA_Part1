from typing import List, Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def step_step(self, root : Optional[TreeNode], startVal: int, target: int)-> str:
        def dfs(node, path, target):
            if not node:
                return False
            if node.val == target:
                return path
            
            path.append("L")
            res = dfs(node.left, path, target)
            if res:
                return res            
            path.pop() #backtrack to last node if target not found

            path.append('R')
            res = dfs(node.right, path, target)
            if res:
                return res
            path.pop() #backtrack to the last node

            return "" #Not foud in either subtree
        
        start_path = dfs(root, [], startVal)
        target_path = dfs(root, [], target)

        #find the index of the Longest Common ANcestor
        i = 0
        while i < min(len(start_path), len(target_path)):
            if start_path[i]!=target_path[i]:
                break
            i+= 1
        # Once ith index is found we concatenate
        return "".join(["U"] * len(start_path[i:]) + target_path[i:])
        


def main():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(8)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(sol.step_step(root, startVal=4, target=5))

if __name__ == "__main__":
    main()