from trie import Trie

path_wl = "src/data/wordlist.txt"

class Vocabulary:
    """uses Trie-data structure as a base to generate
    a vocabulary for spell-checker programm
    """
    def __init__(self, trie=Trie(), path_wl=path_wl):
        self.trie = trie
        self.path_wl = path_wl

    def compile_from_wl(self):
        """generates a ready-to-use vocabulary from wordlist.txt"""
        with open(self.path_wl, "r", encoding='UTF-8') as file:
            for row in file:
                self.trie.insert(row.strip())

    def __len__(self):
        return len(self.trie)
