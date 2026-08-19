class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            if (num - 1) not in seen:
                length = 1
                while (num + length) in seen:
                    length += 1
                if length > longest:
                    longest = length

        return longest