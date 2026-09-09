class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self._size = 0

    def insert(self, word):
        if not word:
            raise ValueError("cannot insert an empty string into the trie")

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        if not node.is_word:
            self._size += 1
        node.is_word = True
        node.word = word

    def find_node(self, prefix: str):
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if node is None:
                return None
        return node

    def contains(self, word: str):
        node = self.find_node(word)
        return node is not None and node.is_word