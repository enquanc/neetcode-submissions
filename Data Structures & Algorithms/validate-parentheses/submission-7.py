class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # print(s)
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if stack == []:
                    return False
                out = stack.pop()
                if  out == '(' and i == ')':
                    continue
                elif out == '[' and i == ']':
                    continue
                elif out == '{' and i == '}':
                    continue
                else:
                    return False
        if  stack == []:
            return True
        else:  return False
