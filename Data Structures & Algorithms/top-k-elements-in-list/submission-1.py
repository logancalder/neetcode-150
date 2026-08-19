class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        heap = []

        for num in nums:
            seen[num] += 1
        
        return heapq.nlargest(k, seen, key=seen.get)