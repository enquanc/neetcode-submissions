class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        stack = []
        for p in path_list:
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)