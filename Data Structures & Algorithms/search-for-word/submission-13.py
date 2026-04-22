class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        yes_flag = False
        def find(index, i, j, path):
                
            if board[i][j] == word[index]:
                if index== len(word) -1:
                    return True
                path.append([i,j])
                if i+1 < len(board) and [i+1, j] not in path:
                    if find(index+1, i+1, j, path):
                        return True

                if i-1 >= 0 and [i-1, j] not in path:
                    if find(index+1, i-1, j, path):
                        return True

                if j+1 < len(board[0]) and [i, j+1] not in path:
                    if find(index+1, i, j+1, path):
                        return True

                if j-1 >= 0 and [i, j-1] not in path:
                    if find(index+1, i, j-1, path):
                        return True
                path.pop()
            return

        for row in range(len(board)):
            for col in range(len(board[0])):
                if find(0, row, col, []):
                    return True
        return False
