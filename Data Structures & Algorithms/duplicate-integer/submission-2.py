class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for elt in nums:
            if elt in seen:
                return True
            seen.add(elt)
        return False
