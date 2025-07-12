class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution: 
    def reverseIteratively(self, head: ListNode)->ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr =nxt
    
        return prev
    
# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# ---------- Main ----------
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]  # Example list
    head = create_linked_list(values)
    print("Original List:")
    print_linked_list(head)

    sol = Solution()
    reversed_head = sol.reverseIteratively(head)

    print("Reversed List:")
    print_linked_list(reversed_head)