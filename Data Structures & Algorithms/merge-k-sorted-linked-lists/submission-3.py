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
            val, idx, node = heapq.heappop(heap)
            head.next = node
            head = head.next

            if node.next:
                i += 1
                node = node.next
                heapq.heappush(heap, (node.val, i, node))
        
        return top.next