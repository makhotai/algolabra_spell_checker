# User guide

## Running the program
To run the program start the `app.py` file.

First, the program asks you to choose the dictionary to use. There are two options: `src/data/small_wordlist.txt` and `src/data/wordlist.txt`. Honestly, for the first use I would recommend to use the smaller, since it is easier to follow the logic and functions of the program.

Current version has four functionalities: print whole current vocabulary word by word (1), add a new word (2), check a word (3) or quit the program (4). Just type the number of the feature in terminal.

### Adding a new word

You can only add a new word to a dictionary if it does not already contain this word. An empty string cannot be added. The program parses your input and writes the string in lowercase to the last row of currently used `txt` file. 

Unfortunately, the program cannot delete an inserted word from the file. However, you can easily delete it manually since all user-added words are located at the end of the file ;)

### Checking the spelling of a word

The spell checker checks one word at a time.

If the word is in the dictionary, the program will report that the spelling is correct.

If the word is not found, the program will suggest the closest words from the dictionary.

To check the word you need to type the word either correctly or wrongly spelled. If the word is spelled correctly (the dictionary contains it) the program will report that the spelling is correct. Otherwise the program will suggest the closest words from the dictionary.