class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        
    def walk(self,s :str):
        node = self.root
        for ch in s:
            if ch in node.children:
                node = node.children[ch]
            else:
                return None
        return node

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TreeNode()
            node = node.children[ch]
        node.is_end = True
            

    def search(self, word: str) -> bool:
        node = self.walk(word)
        if node == None:
            return False
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.walk(prefix) != None
        