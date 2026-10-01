# Implementation 
The program is a terminal based Finnish spell-checker so it suggests correct spelling when given a user’s misspelled word. However, it can work with other languages as well. You just need to load another txt wordlist.

The user can enter a single Finnish word, either correctly or incorrectly written. The program will first check whether the word exists in the dictionary. If the word is found, the program will report that the spelling is correct. If the word is not found, the program will search for similar words in the dictionary and suggest the closest alternatives based on their similarities (edit distances).

The dictionary is stored in Trie data structure and correctly spelled words are suggested using Damerau-Levenshtein distance calculation.

## General structure

The main program is started from `app.py`, which creates the terminal UI and runs the application.

The `SpellChecker` class connects the different parts of the program. Mostly it loads words from a text file into the Trie, checks whether a word is already in the vocabulary, adds new words and searches for spelling suggestions.

The `Trie` stores the dictionary words using search tree approach. The difference is that its nodes do not store their association key. Each edge is labeled with a character, and a path from the root spells out a prefix. The words with the same prefix share the same nodes (e.g. aamu, aamuisin, aamupala) and reuse the same path in the beginning (a-a-m-u).

There are currently two edit distance implementations. The first one is the Optimal String Alignment (OSA) distance in `osa.py`. The second one is the unrestricted Damerau–Levenshtein distance in `damerau_levenshtein.py`. The application currently uses the unrestricted Damerau–Levenshtein version for spelling suggestions generation. 
Both variants have 4 single-character operations: insertion, deletion, substitution and transposition. 
However, the main difference is that OSA restricts repeated editing of an already transposed substring, while unrestricted Damerau–Levenshtein does not. Therefore unrestricted variant can produce a smaller distance for some pairs of strings.
"ca" - "abc"
OSA: "ca" -> "a" -> "ab" -> "abc" 3
unrestricted DL: "ca" -> "ac" -> "abc" 2

Program uses smaller vocabulary `small_wordlist.txt` by deafult. This file contains 28 words. A larger `wordlist.txt` is also included in the project and contains 100000+ words.

The `UI` class is responsible for the terminal menu and user input. The user can print the vocabulary (1), add a new word (2), check a word (3) or quit the program (4).

## Achieved time and space complexities

### Trie 

#### word insertion to the Trie

Walks down the tree character by character, creating new nodes as needed, and marks the final node as `node.is_word = True` `node.word = word`. Therefore insertion time and space complexitites are both O(n) where n is string length (even in the worst case if the word has completely new prefix).

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True
        node.word = word
```
#### word search in the Trie

The word lookups also walk one node per character, therefore searching for a word of length n takes O(n) time regardless of how many words the trie holds.

```python
    def search(self, word):
        node = self.walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):
        return self.walk(prefix) is not None

    def walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

### Edit distance

#### OSA

The OSA algorithm uses dynamic programming to fill a matrix of size (m+1)×(n+1) cells where m and n are the lengths two compared strings. Each cell computes the minimum cost of insertions, deletions or substitutions in constant time O(1). Therefore the time complicity is O(mn).

```
m = length(word1)
n = length(word2)

create matrix (m+1)×(n+1)

start first row and first column

for i in range m:
    for j in range n:

        calculate substitution cost

        matrix[i][j] =
            min(insertion,
                deletion,
                substitution)

        if the two adjacent characters are transposed:
            transpose

return the last cell of the matrix
```

#### Damerau-Levemshtein distance

This variant uses the same type of dynamic programming matrix. However, it stores information about previous positions of characters in the `da` dictionary and uses `db` to remember the last matching position in the current row.

The implementation has matrix of size (m+2) × (n+2) cells and performs a constant amount of work at each cell. The lookup in `da` takes expected constant time O(1).  Therefore the time complicity is O(mn). The whole matrix is stored, so the space complexity is O(mn).

```
m = length(word1)
n = length(word2)

maxdistance = m + n

create matrix (m+2)×(n+2)

matrix[0][0] = maxdistance

initialize two first columns

create table for previous character positions

for i in range(word1):
    reset last matching position

    for j in range(word2):
        find previous occurrence of the character

        matrix[i+1][j+1] =
            min(insertion,
                deletion,
                substitution,
                transposition)

    update the previous position of the character

return the last cell of the matrix
```

## Possible shortcomings and suggestions for improvement

Firstly, the program can only check one word at once. I think that checking several words (and suggesting corrections for them if needed) at once would a great additional feature.

Secondly, every dictionary word is considered as a candidate for a misspelled word. The Trie makes exact word lookup efficient, but it is not currently used to eliminate candidates before calculating the edit distance.

Lastly, Finnish words usually have several inflected forms(e.g. different cases and verb conjugations etc). The current version of the application only checks dictionary forms of words, such as the nominative form of nouns and the infinitive form of verbs. To support other forms, the word list used by the spell checker would have to be much larger, and the search mechanism would have to be optimized so that the program would not have to go through the entire vocabulary for every input word.

## Use of large language models

* **Grammarly**: for checking spelling and punctuation when writing reports and other documents. Even though I did not use AI chat or AI detector there, the program still uses some LLM mechanisms to correct inputs. However, I did not always use it when writing and I did not also copy/pasted all its suggestions directly.

* **ChatGPT (v5?) Think-mode** At first week of the course I used ChatGPT to explore possible project ideas in addition to those were suggested in the course. However, I was satisfied with its suggestions. I also asked for ideas about different mechanisms, features, and libraries that could be implemented to make the spell-checker more interesting. I decided not to implement most of those in my project since I was not sure about difficulty of my project (except implementing unrestricted variant of DL distance in addition to OSA).


## Sources

* [Damerau–Levenshtein Distance: Transpositions, OSA & Algorithms (levenshtein.net)](https://www.levenshtein.net/damerau-levenshtein-distance)
* [Damerau–Levenshtein distance (Wikipedia)](https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance#Optimal_string_alignment_distance)
* [Trie Data Structure (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
* [Trie (Prefix Tree (CoddyTech)](https://coddy.tech/visualize/data-structures/trie)
* [Deep Dive into String Similarity: From Edit Distance to Fuzzy Matching Theory and Practice in Python (Medium, sec. 2)](https://medium.com/data-science-collective/deep-dive-into-string-similarity-from-edit-distance-to-fuzzy-matching-theory-and-practice-in-68e214c0cb1d)
