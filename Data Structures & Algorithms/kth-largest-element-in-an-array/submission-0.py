class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for elt in nums:
            heapq.heappush(heap, elt)
        
        for i in range(len(nums) - k):
            heapq.heappop(heap)
        
        return heap[0]
