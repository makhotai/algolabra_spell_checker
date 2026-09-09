node_count = 0 # for checking
word_count = 0
path_wl = "src/data/wordlist.txt"

class Node:
    def __init__(self):
        self.word = None
        self.children = {}
        
        global node_count
        node_count += 1
    
    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()

            node = node.children[letter]

        node.word = word

trie = Node()
with open(path_wl, "r", encoding='UTF-8') as file:
    for row in file:
        trie.insert(row.strip())
        word_count += 1

print(f" {word_count} words, {node_count} nodes")
