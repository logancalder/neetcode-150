class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if mid <= r
        # must be there
        # if mid >= l
        # must be there
        l, r, small = 0, len(nums) - 1, nums[0]

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                small = min(nums[r],small)
                l = m + 1
            else:
                small = min(nums[m],small)
                r = m - 1
            
        return small