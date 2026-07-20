# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = ListNode(None, next=head)
        fast = curr
        slow = curr
        for i in range(n):
            fast = fast.next
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return curr.next

