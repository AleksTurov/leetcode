class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def printList(head):
    current = head
    
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')

# Created list
values = [1, 2, 3, 4, 5]
head = createList(values)

# Input
printList(head)


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

solution = Solution()
middle = solution.middleNode(head)

printList(middle)


        

