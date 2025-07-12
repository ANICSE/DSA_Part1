class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reorder(self, head: ListNode)->None:
        if not head or not head.next:
            return
        
        #Step 1: Find the middle:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        #Step 2: Reverse the second half:
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #Step 3: Merge the two List
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second =tmp2
        
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

def main():
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    print("Original List:")
    print_linked_list(head)

    sol = Solution()
    sol.reorder(head)

    print("Reordered List:")
    print_linked_list(head)

if __name__ == "__main__":
    main()
