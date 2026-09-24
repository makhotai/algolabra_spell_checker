# Weekly report 2
This week I started coding and thinking about the structure of my project. I wrote the initial code for OSA and Trie. I have not written the full OSA class with all the necessary methods yet, but it already calculates the distance between strings correctly. Therefore, I am planning to finish and properly structure the OSA implementation next week.

Mostly this week development was focused on Trie data-structure code (word insertion and search).I decided to make a separate script for the vocabulary that will be used by the program and generated from `wordlist.txt`. I would like to implenet feature that allows user to add a word to `wordlist.txt` in alpabeth order so the word would be saved and used later.

Secondly, I started using coverage-tool and unit tests. This testing approach seemed a little bit complicated at first, but in the end it was very useful. I tried to develop tests and its inputs as diversive as possible at this stage. As a result, I found that the same word could be inserted more than once. Unfortunately, I have not develop any tests for vocabulary.py yet, but I am going to work on them next week.

Lastly, I started writing docstrings in my code. I haven't also documented everything yet.

## Questions for the course instructor
I used this [referenssisovellus](https://github.com/ohjelmistotekniikka-hy/python-todo-app/tree/master) as a reference for docstrings, file structure etc. Based on this example I should write docstring almost to everything (even to such methods as `__init__` or `__len__`). I am really not sure whether I should document my code in the same very precise way or not...

## Time spent

| date | time |
| ----- | ------------- |
| 7.9  | 0.5 h            |
| 8.9  | 1 h            |
| 9.9  | 5 h            |
| 10.9  | 3 h            |
| 11.9  | 4 h            |

**week total: 13.5 h**