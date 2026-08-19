class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        seen = {}

        for string in strs:
            anagram = str(sorted(string))
            if anagram not in seen:
                seen[anagram] = [string]
            else:
                seen[anagram].append(string)
        
        output = []

        for key in seen:
            output.append(seen[key])

        return output