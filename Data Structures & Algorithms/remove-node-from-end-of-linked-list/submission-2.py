# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        prev = None
        seen = {}
        current = head

        i = 0

        while current:
            seen[i] = (current.next, current, prev)
            prev = current
            if current.next:
                i += 1
            current = current.next
        
        remove_index = i - n + 1
        if not seen[remove_index][2]:
            return seen[remove_index][0]
        seen[remove_index][2].next = seen[remove_index][0]
        return head