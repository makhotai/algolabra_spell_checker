# Project specification
Study program: Bachelor’s in Computer Science/Tietojenkäsittelytieteen kandiohjelma (TKT).
The language used in the both project documentation and code is English. The programming language of the project is Python.
I can do peer review in both Finnish and Eglish languages and projects written in Python/R. 

## The topic of the project
This is a project implementing a program that suggests correct spelling when given a user’s misspelled word in Finnish.

### Implementation and the core of the project
The application will mainly be used through a terminal interface. The user can enter a single Finnish word, either correctly or incorrectly written. The program will first check whether the word exists in the dictionary. If the word is found, the program will report that the spelling is correct. If the word is not found, the program will search for similar words in the dictionary and suggest the closest alternatives based on their similarities (distances). The initial version will only check dictionary forms of words such as the nominative form of nouns and the infinitive form of verbs etc.

I will use the Optimal string alignment (OSA), restricted variant of Damerau–Levenshtein distance to measure the difference between words. The posible wordlist will be stored in a Trie data structure implemented from scratch. The program will use this approach to find and possibly rank the closest correctly spelled words as correction suggestions. Each line will contain one word. The words will be inserted into the Trie when the program starts.

So the core of the project is the implementation of the **Trie data structure** and **Optimal string alignment (OSA), restricted variant of Damerau–Levenshtein distance**, and using them together to find suitable spelling corrections for Finnish words.

### Expected time and space complexities
The OSA algorithm uses dynamic programming to fill a matrix of size (n+1)×(m+1) cells where m and n are the lengths two compared strings. Each cell computes the minimum cost of insertions, deletions or substitutions in constant time O(1). Therefore the time complicity is O(mn).

Insertion and searching in Trie are O(n) time and O(n) space where n is string length. Insertion of the whole dictionary in Trie is O(l) where l is total amount of dictionary characters.

### Possible extensions
As a possible extension I may implement and also compare the unrestricted Damerau–Levenshtein distance if the core implementation would be completed earlier.

## Sources:
* [Damerau–Levenshtein distance (Wikipedia)](https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance#Optimal_string_alignment_distance)
* [Damerau–Levenshtein distance (GeeksforGeeks)](https://www.geeksforgeeks.org/dsa/damerau-levenshtein-distance/)
* [Trie Data Structure (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
* [Trie Data Structure (GeeksforGeeks)](https://www.geeksforgeeks.org/dsa/trie-insert-and-search/)
* [Deep Dive into String Similarity: From Edit Distance to Fuzzy Matching Theory and Practice in Python (Medium, sec. 2)](https://medium.com/data-science-collective/deep-dive-into-string-similarity-from-edit-distance-to-fuzzy-matching-theory-and-practice-in-68e214c0cb1d)
* [Finnish word list](https://kaino.kotus.fi/lataa/nykysuomensanalista2024.txt)