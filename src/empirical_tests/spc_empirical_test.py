import time

from services.trie import Trie
from services.damerau_levenshtein import distance_full

PATH_ENG = "src/data/words.txt"

class SPC_Empirical:
    """Simplified sample spell-checker class for testing 
    most commonly mispelled words in English
    """
    def __init__(self, trie=None, path_wl=PATH_ENG):
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


    def is_correct(self, word: str):
        """checks whether a word is present in the vocabulary"""
        return self.trie.contains(word)

    def words(self):
        """returns a list of all words contained in the vocabulary"""
        return self.trie.words()

    def suggest_similar_full(self, word: str):
        """suggest possible correct spelling of words 
        based on their Damerau-Levenshtein distance distance
        """
        max_distance = 2
        top_k = 5
        results = []

        for pair in self.trie.words():
            res = distance_full(word, pair)

            if res <= max_distance:
                prefix_length = self.same_prefix(word, pair)
                results.append((pair, res, prefix_length))

        results.sort(key=lambda pair: (pair[1], -pair[2], pair[0]))

        results = results[:top_k]
        sug = []
        for pair in results:
            sug.append((pair[0], pair[1]))
        return sug

    def same_prefix(self, word1: str, word2: str):
        """counts the number of similar symbols in the beginning of two strings"""
        count = 0
        m = len(word1)
        n = len(word2)

        for i in range(min(m, n)):
            if word1[i] != word2[i]:
                break
            count += 1

        return count

    def check_incorrect_file(self):
        """checks misspelled words from a file and saves suggestions to a new file"""
        path_incorrect = "src/data/incorrect.txt"
        path_results = "src/data/suggestions.txt"
        with open(path_incorrect, "r", encoding='UTF-8') as file:
            words = file.readlines()
        with open(path_results, "w", encoding='UTF-8') as file:
            for row in words:
                word = row.strip().lower()
                if not word:
                    continue
                suggestions = self.suggest_similar_full(word)
                file.write(f"suggestions for '{word}':\n")
                if suggestions:
                    for suggestion, dist in suggestions:
                        file.write(f"{suggestion} (distance: {dist})\n")
                else:
                    file.write("no suggestions found\n")
                file.write("\n")

    def __len__(self):
        return len(self.trie)

if __name__ == "__main__":
    sp = SPC_Empirical()
    sp.load_from_file()

    start = time.time()
    sp.check_incorrect_file()
    end = time.time()
    yht = end - start

    print(yht)
