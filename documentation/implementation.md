# Implementation 
The program is a terminal based Finnish spell-checker so it suggests correct spelling when given a user’s misspelled word. However, it can work with other languages as well. You just need to load another txt wordlist.

The user can enter a single Finnish word, either correctly or incorrectly written. The program will first check whether the word exists in the dictionary. If the word is found, the program will report that the spelling is correct. If the word is not found, the program will search for similar words in the dictionary and suggest the closest alternatives based on their similarities (edit distances).

The dictionary is stored in Trie data structure and correctly spelled words are suggested using Damerau-Levenshtein distance. **TBA**

## General structure

The main program is started from `app.py`, which creates the terminal UI and runs the application.

The `SpellChecker` class connects the different parts of the program. Mostly it loads words from a text file into the Trie, checks whether a word is already in the vocabulary, adds new words and searches for spelling suggestions.

The `Trie` stores the dictionary words using search tree approach. **TBA**

There are currently two edit distance implementations. The first one is the Optimal String Alignment (OSA) distance in `osa.py`. The second one is the unrestricted Damerau–Levenshtein distance in `damerau_levenshtein.py`. The application currently uses the unrestricted Damerau–Levenshtein version for spelling suggestions generation. **TBA**

Program uses smaller vocabulary `small_wordlist.txt` by deafult. This file contains 28 words. A larger `wordlist.txt` is also included in the project and contains 100000+ words.

The `UI` class is responsible for the terminal menu and user input. The user can print the vocabulary (1), add a new word (2), check a word (3) or quit the program (4).

## Achieved time and space complexities

**TBA**

## Possible shortcomings and suggestions for improvement

**TBA**

## Use of large language models

**TBA**

## Sources

**TBA**