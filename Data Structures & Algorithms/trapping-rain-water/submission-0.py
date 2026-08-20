class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        biggest_left = [0]
        biggest_right = []
        water_count = 0

        largest_left = 0
        for i in range(1, len(height), 1):
            if height[i-1] > largest_left:
                largest_left = height[i-1]
            biggest_left.append(largest_left)

        largest_right = 0
        for i in range(len(height) - 2, -1, -1):
            if height[i + 1] > largest_right:
                largest_right = height[i + 1]
            biggest_right.append(largest_right)

        biggest_right.append(0)
        biggest_right.reverse()

        for i in range(1, len(height), 1):
            volume = min(biggest_left[i], biggest_right[i]) - height[i]
            if volume > 0:
                water_count += volume
        
        return water_count
            