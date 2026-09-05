class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for each point, calc dist
        # add to heap by distance
        # pop first k entries
        heap = []

        for point in points:
            distance = math.sqrt((point[0]) ** 2 + (point[1]) ** 2)
            heapq.heappush(heap, (distance, point))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result