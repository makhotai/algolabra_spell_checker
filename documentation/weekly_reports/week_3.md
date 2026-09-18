# Weekly report
This week I mostly focused on developing tests and implementing the spell checker and its possible UI/functionality as classes, so that the user could use it through the terminal.

There was a little misunderstanding. I received feedback from the curator that I needed to implement a generator in the Trie class for looping through the words when calculating the distance between them. I googled some information about generators in Python and, based on the search results, I thought that I needed to make a for word in words loop that would "yield" each word back as a generator object instead of commonly returning them. After contacting the curator and receiving clarification, I simply made a loop in the Trie and combined it with the distance calculation in the SpellChecker's `suggest_similar()`.

I also added new word insertion feature to txt file that used by spell-checker. However, it inserts word to end of the list in txt file. It could be inserted alphabetically if the file would be rewrited completely after new word insertion but it would not be efficient... Nevertheless, spell-checker always returns current wordlist sorted alphabetically so I see no problem at this point. In addition, I decied to go with shorter wordlist for testing so it would be more convinient to test during development stage.

I did not add any docstrings to the current UI since I may want to replace it later.

### About UI
Since I focused more on testing and the algorithmic side of my program, the UI is currently in a somewhat unpolished state. However, it works :D. Obviously, I am going to improve some visual aspects of it next week.

You can test current program by running `app.py`

Currently its fuctionality includes: 1 - print vocabulary; 2 - add new word to vocabulary; 3 - check word spelling; 4 - quit. 

After launching, the program loads the starting vocabulary from `small_wordlist.txt`, which contains 28 words and then prints the menu.

I have note that adding a word (2) does not insert it into `small_wordlist.txt`. It only inserts the string into the current session through `Trie.words(), SpellChecker.words()`, so the text file stays the same. Therefore, after quitting the program, the added words will not be saved. I am going to add insertion into the file later.


## Questions for the course instructor
1. I would like to implement a search based on a prefix of the word so that the program would print words starting with it. I have an approximate idea of how to do it. However, I am not sure if it is reasonable to do this in this course, since I wanted to optionally try to implement the unrestricted variant of the Damerau–Levenshtein distance later, as I wanted at the beginning of the course. Am I allowed to implement prefix search instead without losing points, or should I keep the initial plan?

2. I am not sure whether I have to run any tests for `UI` class since I could not come up with any ideas. Should I provide some tests for `UI` as well? If yes, could you give me some hints about what I should test?

## Time spent

| date | time |
| ----- | ------------- |
| 16.9  | 1.5 h            |
| 17.9  | 6 h            |
| 18.9  | 6 h            |

**week total: 13.5 h**