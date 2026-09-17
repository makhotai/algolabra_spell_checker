from services.vocabulary import SpellChecker

class UI:
    def __init__(self):
        self.sp = SpellChecker()
        self.sp.load_from_file()
    
    def start(self):
        self.menu()
        option = input("(1-4): ")
        if option == "1":
            self.print_voc()

        elif option == "2":
            self.add_word()

        elif option == "3":
            self.check_word()
            
        elif option == "4":
            self.quit()
        
        else:
            print("invalid input, please try again")
            print()
    
    def menu(self):
        print("choose one of the following options:")
        print("1 - print vocabulary")
        print("2 - add new word to vocabulary")
        print("3 - check word spelling")
        print("4 - quit")
        print()
    
    def print_voc(self):
        pass
    
    def add_new(self):
        pass
    
    def check_word(self):
        pass
    
    def quit(self):
        pass