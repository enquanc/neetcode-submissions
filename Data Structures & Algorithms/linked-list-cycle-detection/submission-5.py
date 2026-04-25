# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        path = set()

        prev, curr = None, head
        while curr:
            if curr not in path:
                path.add(curr)
            else:
                return True
            prev, curr = curr, curr.next
        return False
