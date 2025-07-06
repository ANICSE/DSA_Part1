from typing import List
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def merge_k_linked_list(self, lists: List[ListNode])->ListNode:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            combine_list = []

            for i in range (0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                combine_list.append(self.mergeList(l1,l2))

            lists = combine_list
        return lists[0]
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next
    
def print_list(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def main():
    sol = Solution()
    # List 1: 1 -> 3 -> 5
    l1 = ListNode(1, ListNode(3, ListNode(5)))

    # List 2: 2 -> 4 -> 6
    l2 = ListNode(2, ListNode(4, ListNode(6)))

    l3 = ListNode(1, ListNode(5, ListNode(7))) 

    list_of_Lists= [l1, l2, l3]
    # Merge and print
    merged = sol.merge_k_linked_list(list_of_Lists)
    print("Merged List:")
    print_list(merged)

if __name__ == "__main__":
    main()