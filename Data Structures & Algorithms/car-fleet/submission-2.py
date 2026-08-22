class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = []
        for i in range(len(position)):
            paired.append((position[i], speed[i]))
        paired = sorted(paired, reverse=True)

        times = []

        for pair in paired:
            times.append((target - pair[0]) / pair[1])
        
        num_groups = 1
        finish_time = times[0]

        for time in times[1:]:
            if time > finish_time:
                num_groups += 1
                finish_time = time
        
        return num_groups
