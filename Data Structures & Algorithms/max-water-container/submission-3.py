class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start at largest width
        # calculate area
            # compare area
            # store largest
        # pick shortest tower
            # move inward 

        if not heights:
            return 0
        
        l, r = 0, len(heights) - 1
        largest_area = min(heights[l], heights[r])

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > largest_area:
                largest_area = area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return largest_area
