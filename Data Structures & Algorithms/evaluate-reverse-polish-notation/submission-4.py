class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['-','+','/','*']
        operations = set(operations)
        process = []

        for token in tokens:
            if token not in operations:
                process.append(int(token))
            else:
                y, x = process.pop(), process.pop()
                if token == '-':
                    result = x - y
                if token == '+':
                    result = x + y
                if token == '*':
                    result = x * y
                if token == '/':
                    result = int(x / y)
                process.append(result)
                print(result)
        
        return process[0]

