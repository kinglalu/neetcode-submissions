class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False

        for string in s:
            if string == '(' or string == '[' or string == '{':
                stack.append(string)
                continue

            if len(stack) == 0:
                return False

            if string == ')' and stack[-1] == '(':
                stack.pop()
            elif string == ']' and stack[-1] == '[':
                stack.pop()
            elif string == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

        return len(stack) == 0

        
        