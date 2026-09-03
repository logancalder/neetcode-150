class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        i = 0
        for stone in stones:
            heapq.heappush(heap, (-stone, i))
            i += 1
        
        total = 0

        while len(heap) > 1:
            first = -heapq.heappop(heap)[0]
            second = -heapq.heappop(heap)[0]

            print(f"{first} {second}")

            if first != second:
                heapq.heappush(heap, (-abs(first - second), i))
                i += 1

        if heap:
            return -heap[0][0]
        
        return 0
        
