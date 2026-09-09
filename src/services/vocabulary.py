from trie import Trie

path_wl = "src/data/wordlist.txt"

trie = Trie()
with open(path_wl, "r", encoding='UTF-8') as file:
    for row in file:
        trie.insert(row.strip())
