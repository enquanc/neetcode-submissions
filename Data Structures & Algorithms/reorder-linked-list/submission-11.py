# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # left = ListNode()
        # right = ListNode()

        # Reverse
        tmp = slow.next
        slow.next = None
        slow = tmp

        rev_LL = ListNode()
        rev = rev_LL
        prev, curr = None, slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev
        while second:
            if first:
            # add right and left part
                temp1 = first.next
                temp2 = second.next

                first.next = second
                second.next = temp1
                first = temp1
                second = temp2
                
            # add right part


        # return head
