class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            current = temperatures[i]
            while j < n:
                if temperatures[j] > current:
                    res[i] = j - i
                    break
                elif res[j] == 0:
                    break

                j += res[j]
            if j >= n:
                res[i] = 0
        
        return res