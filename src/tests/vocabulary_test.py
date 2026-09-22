import hypothesis.strategies as st
from hypothesis import given, settings
import unittest

from services.vocabulary import SpellChecker
from services.trie import Trie

class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.voc = SpellChecker()
        self.voc.add("kissa")
        self.voc.add("koira")
        self.voc.add("omena")
        self.voc.add("kirje")
        self.voc.add("kirja")

    def test_word_added_and_contained(self):
        self.assertTrue(self.voc.is_correct("kissa"))
        self.assertTrue(self.voc.is_correct("kirje"))
        self.assertTrue(self.voc.is_correct("kirja"))
        self.assertTrue(self.voc.is_correct("koira"))
        self.assertTrue(self.voc.is_correct("omena"))

    def test_misspelled_word_is_not_recognized(self):
        self.assertFalse(self.voc.is_correct("kisa"))
        self.assertFalse(self.voc.is_correct("oomena"))

    def test_word_count_correct(self):
        voc_count = SpellChecker()
        n = 4
        self.assertEqual(len(voc_count), 0)
        self.assertNotEqual(len(voc_count), n)

        wordlist = ["one", "two", "three", "four", "five", "six"]
        for i in range(n):
            voc_count.add(wordlist[i])
        self.assertEqual(len(voc_count), n)

    def test_exact_match_is_suggested_with_distance_zero(self):
        suggestions = self.voc.suggest_similar("kissa")
        self.assertIn(("kissa", 0), suggestions)

    def test_single_substitution_corrected(self):
        suggestions = self.voc.suggest_similar("kessa")
        self.assertEqual(suggestions[0], ("kissa", 1))

    def test_single_adjacent_transposition_corrected(self):
        suggestions = self.voc.suggest_similar("kisas")
        self.assertEqual(suggestions[0], ("kissa", 1))

class TestSpellCheckerWithFiles(unittest.TestCase):
    def erase_last(self):
        with open("src/data/test_wordlist.txt", "r", encoding='UTF-8') as file:
            lines = file.readlines()
            lines = lines[:-1]
        with open("src/data/test_wordlist.txt", "w", encoding='UTF-8') as file:
            file.writelines(lines)

    def test_non_none_trie(self):
        self.non_none_voc = SpellChecker(trie=Trie())

    def setUp(self):
        self.voc_file = SpellChecker(path_wl="src/data/test_wordlist.txt")

    def test_empty_vocabulary(self):
        self.assertEqual(len(self.voc_file), 0)
    
    def test_load_from_file(self):
        self.voc_file.load_from_file()
        self.assertEqual(len(self.voc_file), 5)

    def test_words_foreach(self):
        self.voc_file.load_from_file()
        self.assertEqual(self.voc_file.words(), ["kirja", "kirje", "kissa", "koira", "omena"])

    def test_add_to_file(self):
        self.voc_file.load_from_file()
        self.voc_file.add_to_file("test")
        self.assertEqual(self.voc_file.words(), ["kirja", "kirje", "kissa", "koira", "omena", "test"])
        self.erase_last()

    def test_cannot_add_empty_str_to_file(self):
        self.voc_file.load_from_file()
        self.assertIsNone(self.voc_file.add_to_file(""))

    def test_cannot_add_same_word_twice(self):
        self.voc_file.load_from_file()
        self.assertTrue(self.voc_file.add_to_file("new"))
        self.assertFalse(self.voc_file.add_to_file("new"))
        self.assertEqual(self.voc_file.words(), ["kirja", "kirje", "kissa", "koira", "new", "omena"])
        self.erase_last()

class TestSpellCheckerWithHypothesis(unittest.TestCase):        
    def create_txt(self):
        with open("src/data/test_hyp.txt", "w", encoding="utf-8") as file:
            file.write("")

    def setUp(self):
        self.create_txt()
        self.voc_hyp = SpellChecker(path_wl="src/data/test_hyp.txt")

    @given(val=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu")),
                       min_size=10, max_size=30))
    @settings(max_examples=1000)
    def test_all_str_inserted_as_lowercase_hypothesis(self, val):
        self.voc_hyp.load_from_file()
        self.voc_hyp.add_to_file(val)
        val = val.strip().lower()
        self.assertTrue(self.voc_hyp.is_correct(val))
