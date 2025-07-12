class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def remove_node(self, head: ListNode, n: int)->ListNode:
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n+1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next

        return dummy.next
    
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

# ----------- Main Function -------------
def main():
    # Input: list and position to remove from end
    values = [1, 2, 3, 4, 5]
    n = 5  # Remove 2nd node from end (i.e., 4)

    # Create linked list
    head = create_linked_list(values)
    print("Original List:")
    print_linked_list(head)

    # Remove node
    sol = Solution()
    updated_head = sol.remove_node(head, n)

    print("List After Removal:")
    print_linked_list(updated_head)

if __name__ == "__main__":
    main()