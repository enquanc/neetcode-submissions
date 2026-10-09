class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            stack.append(i)
            if stack[-1] == ")" or stack[-1] =='}' or stack[-1] ==']':
                stack.pop()
                if stack == []:
                    return False
                output = stack.pop()
                if output == "(" and i == ')':
                    continue
                elif output == "[" and i == ']':
                    continue
                elif output == "{" and i == '}':
                    continue
                return False
        if stack != []:
            return False
        return True
