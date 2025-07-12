#Using Floyds Tortoise and Hare
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode)->bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    

#Helper function to create a linked list with optional cycle
def create_linked_list(values, pos=-1):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        node = ListNode(val)
        current.next = node
        current = node
        nodes.append(node)

    # Create cycle if pos is valid
    if pos != -1:
        current.next = nodes[pos]

    return head

# ----------- Main -------------
def main():
    # Test Case 1: List with cycle
    values = [3, 2, 0, -4]
    pos = 1  # Last node connects to node at index 1 (0-based)
    head = create_linked_list(values, pos)
    
    sol = Solution()
    print("Cycle Detected?" , sol.hasCycle(head))  # Expected: True

    # Test Case 2: List without cycle
    values = [1, 2, 3, 4]
    pos = -1  # No cycle
    head = create_linked_list(values, pos)
    
    print("Cycle Detected?" , sol.hasCycle(head))  # Expected: False

if __name__ == "__main__":
    main()