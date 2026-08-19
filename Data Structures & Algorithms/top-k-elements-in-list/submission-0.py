import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go thru and sum up the frequencies
        # throw em in a max heap
        # return first k elts of max heap

        if not k:
            return []

        heap = []
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        for num in seen:
            heapq.heappush(heap, (-seen[num],num))

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output