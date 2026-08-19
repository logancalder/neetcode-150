class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        heapq.heapify(nums)
        longest = current = 1
        previous = heapq.heappop(nums)

        while nums:
            num = heapq.heappop(nums)
            if num == previous:
                continue
            if num - 1 == previous:
                current += 1
                if current > longest:
                    longest = current
            else:
                current = 1
            previous = num

        return longest

