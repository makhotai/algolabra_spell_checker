import unittest
from services.vocabulary import SpellChecker

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
    def setUp(self):
        self.voc_file = SpellChecker(path_wl="src/data/test_wordlist.txt")

    def test_empty_vocabulary(self):
        self.assertEqual(len(self.voc_file), 0)
    
    def test_load_from_file(self):
        self.voc_file.load_from_file()
        self.assertEqual(len(self.voc_file), 5)
