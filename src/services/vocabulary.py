from trie import Trie

path_wl = "src/data/wordlist.txt"

class Vocabulary:
    def __init__(self, trie=Trie(), path_wl=path_wl):
        self.trie = trie
        self.path_wl = path_wl

    def compile_from_wl(self):
        with open(self.path_wl, "r", encoding='UTF-8') as file:
            for row in file:
                self.trie.insert(row.strip())

    def __len__(self):
        return len(self.trie)
