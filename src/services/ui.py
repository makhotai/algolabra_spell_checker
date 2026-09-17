from services.vocabulary import SpellChecker

class UI:
    def __init__(self):
        self.sp = SpellChecker()
        self.sp.load_from_file()
    
    def start(self):
        pass
    
    def menu(self):
        pass
    
    def print_voc(self):
        pass
    
    def add_new(self):
        pass
    
    def check_word(self):
        pass
    
    def quit(self):
        pass