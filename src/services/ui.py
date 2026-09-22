import sys
from services.vocabulary import SpellChecker

class UI:
    """constructor of a basic UI for spell-checker working via interface"""
    def __init__(self):
        self.sp = SpellChecker()
        self.sp.load_from_file()

    def start(self):
        print("hello, it is spell-checker program")
        while True:
            self.menu()
            option = input("(1-5): ")
            print()

            if option == "1":
                self.print_voc()

            elif option == "2":
                self.add_new()

            elif option == "3":
                self.find_prefix()

            elif option == "4":
                self.check_word()

            elif option == "5":
                self.quit()

            else:
                print("invalid input, please try again")
                print()

    def menu(self):
        print("choose one of the following options:")
        print()
        print("1 - print vocabulary")
        print("2 - add new word to vocabulary")
        print("3 - search word based on its prefix")
        print("4 - check word spelling")
        print("5 - quit")
        print()

    def print_voc(self):
        print(f"\ncurrent dictionary has {len(self.sp)} word(s):")

        for word in self.sp.words():
            print(word)
        print()

    def add_new(self):
        word = input("\nenter a word to add: ").strip().lower()

        if not word:
            print("you cannot add empty string to vocabulary, sorry\n")
            return

        if self.sp.is_correct(word):
            print(f"the word '{word}' is already in the vocabulary..\n")
            return

        self.sp.add_to_file(word)
        print(f"'{word}' was successfully added to the vocabulary \n")

    def find_prefix(self):
        prefix = input("\nenter a prefix of word to find the words: ").strip().lower()

        if not prefix:
            print("you cannot find words starting with empty string, sorry\n")
            return
        res = self.sp.prefix_search(prefix)

        if not res:
            print(f"no words starting with '{prefix}' found :(\n")
            return

        for word in res:
            print(word)
        print()

    def check_word(self):
        word = input("\nenter a word to check: ").strip().lower()

        if not word:
            print("you cannot check spelling of empty string, sorry\n")
            return

        if self.sp.is_correct(word):
            print(f"'{word}' is spelled correctly :)\n")
            return

        suggestions = self.sp.suggest_similar(word)
        if not suggestions:
            print(f"ops, there are not spelling suggestions for '{word}'\n")

        print(f"possible suggetion(s) for '{word}': ")
        for pair in suggestions:
            print(pair)
        print()

    def quit(self):
        print("\n bye! :) \n")
        sys.exit()
