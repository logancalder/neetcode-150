class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for string in strs:
            length = len(string)
            output += str(length) + "#" + string
        return output

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1

            temp = ""
            end = int(length) + i
            temp += s[i + 1:end + 1]
            result.append(temp)
            i = end
            i += 1
        return result
