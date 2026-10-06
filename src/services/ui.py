import sys
from services.spell_checker import SpellChecker

class UI:
    """constructor of a basic UI for spell-checker working via interface"""
    def __init__(self):
        voc = self.choose_voc()
        self.sp = SpellChecker(path_wl=voc)
        self.sp.load_from_file()

    def choose_voc(self):
        print("\nhello, it is spell-checker program\n")

        var = 0
        while var != "1" or var != "2":
            print("which dictionary do you want to use?")
            print("1. small testing version (28 Finnish words)")
            print("2. larger version (10 000+ Finnish words)")
            var = input("choose 1 or 2: ")
            print()
            if var == "1":
                return "src/data/small_wordlist.txt"
            elif var == "2":
                return "src/data/wordlist.txt"

    def start(self):
        while True:
            self.menu()
            option = input("(1-4): ")
            print()

            if option == "1":
                self.print_voc()

            elif option == "2":
                self.add_new()

            elif option == "3":
                self.check_word()

            elif option == "4":
                self.quit()

            else:
                print("invalid input, please try again")
                print()

    def menu(self):
        print("choose one of the following options:")
        print()
        print(f"1 - print vocabulary ({len(self.sp)} words)")
        print("2 - add new word to vocabulary")
        print("3 - check word spelling")
        print("4 - quit")
        print()

    def print_voc(self):
        print(f"\ncurrent dictionary has {len(self.sp)} word(s):")

        for word in self.sp.words():
            print(word)
        input("\npress enter to proceed")
        print()

    def add_new(self):
        word = input("\nenter a word to add: ").strip().lower()

        if not word:
            print("you cannot add empty string to vocabulary, sorry\n")
            input("press enter to proceed\n")
            return

        if self.sp.is_correct(word):
            print(f"the word '{word}' is already in the vocabulary..\n")
            input("press enter to proceed\n")
            return

        self.sp.add_to_file(word)
        print(f"'{word}' was successfully added to the vocabulary \n")

    def check_word(self):
        word = input("\nenter a word to check: ").strip().lower()

        if not word:
            print("you cannot check spelling of empty string, sorry\n")
            input("press enter to proceed\n")
            return

        if self.sp.is_correct(word):
            print(f"'{word}' is spelled correctly :)\n")
            input("press enter to proceed\n")
            return

        suggestions = self.sp.suggest_similar_full(word)
        if not suggestions:
            print(f"oops, there are not spelling suggestions for '{word}'\n")
            input("press enter to proceed\n")
            return

        print(f"possible suggetion(s) for '{word}': ")
        for pair in suggestions:
            print(pair)
        input("\npress enter to proceed")
        print()

    def quit(self):
        print("\n bye! :) \n")
        sys.exit()
