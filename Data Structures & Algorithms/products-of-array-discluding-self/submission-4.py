class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        product = 1
        seen_zero = False
        zero_indices = 0

        for i, num in enumerate(nums):
            if num == 0:
                seen_zero = True
                zero_indices += 1
            else:
                product *= num
        
        for num in nums:
            if zero_indices > 1:
                result.append(0)
            elif num == 0:
                result.append(product)
            elif seen_zero:
                result.append(0)
            else:
                result.append(product // num)

        return result