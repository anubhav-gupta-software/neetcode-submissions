class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}': '{'}
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack or mapping[s[i]] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return not stack

