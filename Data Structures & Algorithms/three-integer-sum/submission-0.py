class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)

        triplets = set()
        results = []

        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            if l == r:
                break

            while l < r:
                if num + nums[l] + nums[r] == 0:
                    triplet = tuple([num,nums[l],nums[r]])
                    if triplet not in triplets:
                        results.append([num,nums[l],nums[r]])
                        triplets.add( tuple([num,nums[l],nums[r]]) )
                if num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        
        return results
        
            