# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        
        l, r, prev = head, head, None

        for i in range(n - 1):
            r = r.next
        
        while r.next:
            r = r.next
            prev = l
            l = l.next

        if prev:
            prev.next = l.next
        else:
            head = l.next
        return head
        



