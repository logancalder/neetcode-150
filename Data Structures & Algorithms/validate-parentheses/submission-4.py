class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in pairs:
                if not stack or pairs[char] != last:
                    return False
                last = stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        return True
                    
