# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        i = 0
        for array in lists:
            while array:
                i += 1
                heapq.heappush(heap, (array.val, i, array))
                array = array.next
        
        head = top = ListNode()

        while heap:
            dummy = heapq.heappop(heap)
            head.next = dummy[2]
            head = head.next
        
        return top.next

