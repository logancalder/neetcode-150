class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        seen = defaultdict(int)

        for task in tasks:
            seen[task] += 1
        
        maxf = 0

        for task in seen:
            maxf = max(seen[task], maxf)

        count_longest = 0
        
        for task in seen:
            if seen[task] == maxf:
                count_longest += 1

        return max((n + 1) * (maxf - 1) + count_longest, len(tasks))