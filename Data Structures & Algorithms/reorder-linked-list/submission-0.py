# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow now = mid

        prev, curr = None, slow

        while curr: # flip 2nd half
            dummy = curr.next
            curr.next = prev
            prev = curr
            curr = dummy

        while prev.next:
            head.next, head = prev, head.next
            prev.next, prev = head, prev.next
        


            
            