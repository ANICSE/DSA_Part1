class ListNode:
    def __init__(self, val = 0, Next = None):
        self.val = val
        self.next = Next

class Solution:
    def addNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total //10
            curr.next = ListNode(total%10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
#python-list to Linked List
def listToLinkedList(lst):
    dummy = ListNode(0)
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

#LinkedList to PythonList
def LinkedListtoLst(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def main():
    l1 = listToLinkedList([2, 4, 3])
    l2 = listToLinkedList([5, 6, 4])
    sol = Solution()
    results = sol.addNumbers(l1, l2)
    print(LinkedListtoLst(results))

if __name__ == "__main__":
    main()