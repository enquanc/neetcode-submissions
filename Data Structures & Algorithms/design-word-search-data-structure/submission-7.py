class Node():
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node =  self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end                # 字串用完時，要檢查什麼？
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i+1):               # 遞迴呼叫，成功就立刻回傳
                        return True
                return False
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i+1)

        return dfs(self.root, 0)
