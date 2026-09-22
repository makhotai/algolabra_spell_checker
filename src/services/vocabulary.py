from services.trie import Trie
from services.osa import distance

PATH_WL = "src/data/small_wordlist.txt"

class SpellChecker:
    """uses a Trie data structure as a base to generate
    a vocabulary and OSA distance function for spell-checker program
    """
    def __init__(self, trie=None, path_wl=PATH_WL):
        if trie is None:
            trie = Trie()
        self.trie = trie
        self.path_wl = path_wl

    def load_from_file(self):
        """loads words from wordlist.txt into the vocabulary"""
        with open(self.path_wl, "r", encoding='UTF-8') as file:
            for row in file:
                self.trie.insert(row.strip())

    def add(self, word: str):
        """adds a word to the vocabulary used by the spell checker"""
        return self.trie.insert(word.strip())

    def add_to_file(self, word: str):
        """inserts a word to the both txt file and vocabulary"""
        if not word:
            return None

        word = word.strip().lower()
        if self.is_correct(word) is False:
            self.trie.insert(word)
            with open(self.path_wl, "a", encoding='UTF-8') as file:
                file.write(word + "\n")
            return True
        return False

    def is_correct(self, word: str):
        """checks whether a word is present in the vocabulary"""
        return self.trie.contains(word)

    def words(self):
        """returns a list of all words contained in the vocabulary"""
        return self.trie.words()

    def suggest_similar(self, word: str):
        """suggest possible correct spelling of words based on their OSA distance"""
        max_distance = 2
        top_k = 5
        results = []

        for pair in self.trie.words():
            res = distance(word, pair)
            if res <= max_distance:
                results.append((pair, res))

        results.sort(key=lambda pair: pair[1])

        results = results[:top_k]
        return results

    def __len__(self):
        return len(self.trie)
