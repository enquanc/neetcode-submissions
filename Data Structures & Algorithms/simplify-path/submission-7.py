class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        stack = []
        for p in path_list:
            if p == '.':
                pass
            elif p == '..':
                if stack ==[]:
                    pass
                else:
                    stack.pop()
            elif p=='':
                pass
            else:
                stack.append(p)
        result = ''
        for s in stack:
            result = result + '/'
            result = result + s
        if stack == []:
            return '/'
        return result