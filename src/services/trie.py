class TrieNode:
    """class for single node of the trie
    Attributes:
            word: complete word spelled by the path from the root
            children: maps a letter to the child ``TrieNode`` reached by that
            letter
            is_word: shows if there is a such word
    """
    def __init__(self):
        self.word = None
        self.children = {}
        self.is_word = False

class Trie:
    """a trie that stores a set of dictionary words"""
    def __init__(self):
        self.root = TrieNode()
        self._size = 0

    def insert(self, word: str):
        """adds a word to the trie

        Args:
            word (str): a word (as non-empty string) to insert
        """
        if not word:
            return

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        self._size += 1
        node.is_word = True
        node.word = word

    def find_node(self, prefix: str):
        """searches 'prefix'/word in the trie

        Args:
            prefix (str): word to find

        Returns:
            bool: returns True if the word was previously inserted, 
            otherwise returns False
        """
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if node is None:
                return None
        return node

    def contains(self, word: str):
        """checks if dictionary contains the word

        Args:
            word (str): a word to find

        Returns:
            bool: returns True if the word was previously inserted, 
            otherwise returns False
        """
        node = self.find_node(word)
        return node is not None and node.is_word
    
    def __len__(self):
        """returns a number of words contained in the trie"""
        return self._size
