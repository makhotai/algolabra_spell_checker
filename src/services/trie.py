class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            raise ValueError("cannot insert an empty string into the trie")

        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()

            node = node.children[letter]

        node.word = word
