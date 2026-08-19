class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for char in s:
            seen[char] += 1
        
        for char in t:
            seen[char] -= 1

        for key in seen:
            if seen[key] != 0:
                return False
        
        return True