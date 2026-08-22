# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []

        while head:
            stack.append(head)
            head = head.next
        
        head = top = stack.pop()

        while stack:
            head.next = stack.pop()
            head = head.next
        
        head.next = None
        
        return top

        
        