class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for string in strs:
            anagram = str(sorted(string))
            seen[anagram].append(string)
        
        output = []
        for key in seen:
            output.append(seen[key])
        return output