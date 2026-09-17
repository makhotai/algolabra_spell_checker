from services.trie import Trie
from services.osa import distance

path_wl = "src/data/wordlist.txt"

class SpellChecker:
    """uses Trie-data structure as a base to generate
    a vocabulary for spell-checker programm
    """
    def __init__(self, trie=None, path_wl=path_wl):
        if trie is None:
            trie = Trie()
        self.trie = trie
        self.path_wl = path_wl

    def compile_from_wl(self):
        """generates a ready-to-use vocabulary from wordlist.txt"""
        with open(self.path_wl, "r", encoding='UTF-8') as file:
            for row in file:
                self.trie.insert(row.strip())

    def add(self, word: str):
        self.trie.insert(word.strip())

    def is_correct(self, word: str):
            return self.trie.contains(word)

    def words(self):
            return self.trie.words()

    def __len__(self):
        return len(self.trie)
