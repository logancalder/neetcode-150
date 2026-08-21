class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = defaultdict(int)
        for char in s1:
            freq[char] += 1

        for i in range(len(s2)):
            seen = defaultdict(int)
            for j in range(i, i + len(s1), 1):
                if j >= len(s2):
                    break
                if s2[j] in freq:
                    seen[s2[j]] += 1
                else:
                    break
            print(f"{seen} , {freq}")
            if seen == freq:
                return True

        return False
