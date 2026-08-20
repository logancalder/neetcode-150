class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        l = r = longest = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest