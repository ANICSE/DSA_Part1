class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root, result):
        if not root:
            return None
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

    def mergeSortedLists(self, list1, list2):
        merged = []
        i = j =0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i+=1
            else:
                merged.append(list2[j])
                j+=1
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged

    def sortedListtoBST(self,nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedListtoBST(nums[:mid])
        root.right = self.sortedListtoBST(nums[mid+1:])
        return root

    def mergeBSTs(self, root1, root2):
        list1 = []
        list2 = []
        #Do Inorder Traversal of both BST and store it in list
        self.inorder(root1, list1)
        self.inorder(root2, list2)
        merged = self.mergeSortedLists(list1, list2)
        return self.sortedListtoBST(merged)

def print_inorder(root):
    if not root:
        return None
    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)

def main():
    #BST1
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    #BST2
    root2 = TreeNode(7)
    root2.left = TreeNode(6)
    root2.right = TreeNode(9)

    sol = Solution()
    merge_root = sol.mergeBSTs(root1, root2)
    print("Inorder Traversal of the merged BST")
    print_inorder(merge_root)

if __name__ == "__main__":
    main()