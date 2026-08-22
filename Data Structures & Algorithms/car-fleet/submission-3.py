class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position,speed), reverse = True)

        num_groups = 0
        finish_time = 0

        for pair in paired:
            time = (target - pair[0]) / pair[1]
            if time > finish_time:
                num_groups += 1
                finish_time = time
        
        return num_groups
