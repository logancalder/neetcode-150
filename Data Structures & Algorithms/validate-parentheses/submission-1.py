class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if char == ')':
                    if last != '(':
                        return False
                if char == ']':
                    if last != '[':
                        return False
                if char == '}':
                    if last != '{':
                        return False
        if stack:
            return False
        return True
                    
