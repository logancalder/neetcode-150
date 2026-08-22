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
            i += 1
            if array:
                heapq.heappush(heap, (array.val, i, array))
        
        head = top = ListNode()

        while heap:
            dummy = heapq.heappop(heap)
            head.next = dummy[2]
            head = head.next

            if dummy[2].next:
                i += 1
                dummy = dummy[2].next
                heapq.heappush(heap, (dummy.val, i, dummy))
        
        return top.next